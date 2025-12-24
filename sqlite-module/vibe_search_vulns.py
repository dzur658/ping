import json
import os
import sys
import xml.etree.ElementTree as ET
from typing import Any, Dict, List, Optional

import search_vulns
from search_vulns import core as search_vulns_core


class SearchVulnsClient:
	"""Thin wrapper around the search_vulns library with basic normalization and caching."""

	def __init__(self) -> None:
		# Simple in-memory cache to avoid repeated identical queries
		self._cache: Dict[str, List[Dict[str, Any]]] = {}

	def search(self, query: str) -> List[Dict[str, Any]]:
		if not query:
			return []

		if query in self._cache:
			return self._cache[query]

		try:
			# Use the core.search_vulns API, which returns a dict with a 'vulns' list
			result_obj = search_vulns_core.search_vulns(query)
			data = result_obj.get("vulns", []) if isinstance(result_obj, dict) else []
		except Exception:
			data = []

		self._cache[query] = data
		return data


def cpe_to_query(cpe: str) -> Optional[str]:
	"""Convert a CPE URI into a human-ish query string for search_vulns.

	Supports both CPE 2.2 (e.g., cpe:/a:vendor:product:version) and
	CPE 2.3 (e.g., cpe:2.3:a:vendor:product:version:...).
	"""

	if not cpe or not cpe.startswith("cpe:"):
		return None

	parts = cpe.split(":")
	vendor = ""
	product = ""
	version = ""

	try:
		# CPE 2.2 style: cpe:/a:vendor:product:version
		if len(parts) >= 4 and parts[1].startswith("/"):
			# parts[1] is like "/a" or "/o"; we don't use it directly here
			vendor = parts[2]
			product = parts[3]
			if len(parts) >= 5:
				version = parts[4]

		# CPE 2.3 style: cpe:2.3:a:vendor:product:version:...
		elif len(parts) >= 6 and parts[1] == "2.3":
			# parts[2] is the part (a/o/h)
			vendor = parts[3]
			product = parts[4]
			version = parts[5]
		else:
			return None
	except IndexError:
		return None

	if not product:
		return None

	def humanize(value: str) -> str:
		return value.replace("_", " ").replace("-", " ").strip()

	vendor_h = humanize(vendor) if vendor else ""
	product_h = humanize(product)
	version_h = humanize(version) if version and version != "*" else ""

	tokens: List[str] = []
	if vendor_h:
		tokens.append(vendor_h)
	tokens.append(product_h)
	if version_h:
		tokens.append(version_h)

	query = " ".join(tokens).strip()
	return query or None


class CPEVulnerabilityScanner:
	"""Scan an Nmap XML file for CPEs and query search_vulns for vulnerabilities."""

	def __init__(self) -> None:
		self.client = SearchVulnsClient()

	def _normalize_vuln(self, raw_vuln: Any) -> Dict[str, Any]:
		"""Normalize search_vulns result structure into a compact dict.

		search_vulns may return vulnerability entries as dicts, strings, or
		other lightweight objects. This helper tries to handle all of them
		gracefully without raising type errors.
		"""

		# If it's already a mapping-like object, use the rich fields
		if isinstance(raw_vuln, dict):
			cvss = raw_vuln.get("cvss", {})
			severity: Any = "Unknown"
			if isinstance(cvss, dict):
				severity = cvss.get("score") or cvss.get("base_score") or "Unknown"

			vuln_id = (
				raw_vuln.get("id")
				or raw_vuln.get("cve_id")
				or raw_vuln.get("vuln_id")
				or "Unknown ID"
			)

			return {
				"id": vuln_id,
				"title": raw_vuln.get("summary")
				or raw_vuln.get("title")
				or raw_vuln.get("name")
				or "Vulnerability",
				"cve": raw_vuln.get("cve_id") or raw_vuln.get("id") or vuln_id,
				"severity": severity,
			}

		# Fallback: treat the entry as a simple textual label/ID
		if isinstance(raw_vuln, str):
			text = raw_vuln.strip() or "Unknown vulnerability"
		else:
			text = str(raw_vuln) or "Unknown vulnerability"

		return {
			"id": text,
			"title": text,
			"cve": text,
			"severity": "Unknown",
		}

	def _extract_hosts_with_cpes(self, xml_file: str) -> List[Dict[str, Any]]:
		"""Parse Nmap XML and extract OS and service CPEs for each host."""

		tree = ET.parse(xml_file)
		root = tree.getroot()

		hosts: List[Dict[str, Any]] = []

		for host in root.findall("host"):
			ip: Optional[str] = None
			ip_type: Optional[str] = None

			for addr in host.findall("address"):
				addr_type = addr.get("addrtype")
				if addr_type in ("ipv4", "ipv6") and ip is None:
					ip = addr.get("addr")
					ip_type = addr_type

			if not ip:
				# Skip hosts without an IP address
				continue

			host_entry: Dict[str, Any] = {
				"ip": ip,
				"ip_type": ip_type,
				"os_cpes": [],
				"service_cpes": [],
			}

			# OS CPEs from <os><osclass><cpe>
			os_node = host.find("os")
			os_cpes: List[str] = []
			if os_node is not None:
				for osclass in os_node.findall("osclass"):
					for cpe_el in osclass.findall("cpe"):
						cpe_text = (cpe_el.text or "").strip()
						if cpe_text:
							os_cpes.append(cpe_text)

			# Deduplicate OS CPEs while preserving a stable order
			seen_os = set()
			unique_os_cpes: List[str] = []
			for c in os_cpes:
				if c not in seen_os:
					seen_os.add(c)
					unique_os_cpes.append(c)
			host_entry["os_cpes"] = unique_os_cpes

			# Service CPEs from <ports><port><service><cpe>
			ports_node = host.find("ports")
			service_cpes: List[Dict[str, Any]] = []
			if ports_node is not None:
				for port in ports_node.findall("port"):
					service = port.find("service")
					if service is None:
						continue

					for cpe_el in service.findall("cpe"):
						cpe_text = (cpe_el.text or "").strip()
						if not cpe_text:
							continue

						service_cpes.append(
							{
								"port": port.get("portid"),
								"protocol": port.get("protocol"),
								"service_name": service.get("name"),
								"product": service.get("product"),
								"version": service.get("version"),
								"cpe": cpe_text,
							}
						)

			host_entry["service_cpes"] = service_cpes

			hosts.append(host_entry)

		return hosts

	def scan_xml_for_cpe_vulns(self, xml_file: str) -> List[Dict[str, Any]]:
		"""End-to-end: extract CPEs from Nmap XML and query search_vulns.

		Returns a list of per-host dicts with:
		  - ip, ip_type
		  - os_cpes, service_cpes
		  - vulnerabilities: deduplicated list of normalized vuln dicts
		"""

		if not os.path.exists(xml_file):
			raise FileNotFoundError(f"Nmap XML file not found: {xml_file}")

		hosts = self._extract_hosts_with_cpes(xml_file)
		report: List[Dict[str, Any]] = []

		for host in hosts:
			ip = host["ip"]

			# Map from query string -> list of context strings
			query_contexts: Dict[str, List[str]] = {}

			# OS CPEs
			for cpe_text in host.get("os_cpes", []):
				query = cpe_to_query(cpe_text)
				if not query:
					continue
				context = f"OS CPE {cpe_text} on host {ip}"
				query_contexts.setdefault(query, []).append(context)

			# Service CPEs
			for svc in host.get("service_cpes", []):
				cpe_text = svc.get("cpe")

				# Prefer the richer Nmap service product/version string as the query,
				# using the CPE mainly as the selector for relevance and for context.
				product = (svc.get("product") or "").strip()
				version = (svc.get("version") or "").strip()

				if product:
					query_parts = [product]
					if version and version.lower() != "unknown":
						query_parts.append(version)
					query = " ".join(query_parts)
				else:
					# Fallback to a query derived from the CPE if we lack a product name
					query = cpe_to_query(cpe_text)

				if not query:
					continue
				port = svc.get("port")
				proto = svc.get("protocol")
				svc_name = svc.get("service_name")
				context = (
					f"Service CPE {cpe_text} on host {ip}, "
					f"port {port}/{proto} ({svc_name})"
				)
				query_contexts.setdefault(query, []).append(context)

			# For each unique query, call search_vulns and aggregate/deduplicate vulns
			vulns_by_id: Dict[str, Dict[str, Any]] = {}

			for query, contexts in query_contexts.items():
				results = self.client.search(query)
				if not results:
					continue

				for raw in results:
					normalized = self._normalize_vuln(raw)
					vuln_id = normalized["id"]
					if not vuln_id:
						continue

					if vuln_id not in vulns_by_id:
						# Attach all known contexts for this query initially
						entry = dict(normalized)
						entry["contexts"] = list(dict.fromkeys(contexts))
						vulns_by_id[vuln_id] = entry
					else:
						# Merge contexts
						existing = vulns_by_id[vuln_id]
						existing_contexts = existing.setdefault("contexts", [])
						for ctx in contexts:
							if ctx not in existing_contexts:
								existing_contexts.append(ctx)

			host_report = {
				"ip": host["ip"],
				"ip_type": host.get("ip_type"),
				"os_cpes": host.get("os_cpes", []),
				"service_cpes": host.get("service_cpes", []),
				"vulnerabilities": list(vulns_by_id.values()),
			}

			report.append(host_report)

		return report


def main(argv: List[str]) -> int:
	if len(argv) != 2:
		print(f"Usage: {argv[0]} <nmap_xml_file>", file=sys.stderr)
		return 1

	xml_file = argv[1]

	scanner = CPEVulnerabilityScanner()
	try:
		results = scanner.scan_xml_for_cpe_vulns(xml_file)
	except FileNotFoundError as e:
		print(str(e), file=sys.stderr)
		return 1
	except ET.ParseError as e:
		print(f"Error parsing XML: {e}", file=sys.stderr)
		return 1
	# except Exception as e:
	# 	print(f"Unexpected error: {e}", file=sys.stderr)
	# 	return 1

	# JSON-only output to stdout for the demo
	print(json.dumps(results, indent=2))
	return 0


if __name__ == "__main__":
	raise SystemExit(main(sys.argv))

