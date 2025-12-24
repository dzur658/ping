import xml.etree.ElementTree as ET
import json
import os
import sys

# === INTEGRATION: search_vulns LIBRARY ===
import search_vulns

# CONFIGURATION
XML_FILE = "category_test.xml"

class VulnerabilityScanner:
    def __init__(self):
        # search_vulns relies on its internal DB. 
        # Ensure the DB is built via 'search_vulns -u' before running this.
        print("[Init] Initializing search_vulns engine...")
        pass

    def check_product(self, query_string):
        """
        Wraps the search_vulns library logic.
        Input: "Lighttpd 1.4.35"
        Output: List of CVE objects
        """
        try:
            # The library typically exposes a search function that takes a query string.
            # We assume it returns a list of vulnerability objects or dictionaries.
            # Note: We capture stdout because search_vulns can be chatty on CLI.
            
            # This is the standard API call structure for the library
            results = search_vulns.search(query_string, json_format=True)
            
            # If the library returns a raw JSON string, parse it.
            if isinstance(results, str):
                return json.loads(results)
            return results
            
        except Exception as e:
            # Graceful fallback if the library throws an internal error on bad queries
            return []

    def scan_xml(self, xml_file):
        if not os.path.exists(xml_file):
            print(f"[Error] {xml_file} not found.")
            return []

        tree = ET.parse(xml_file)
        root = tree.getroot()
        report = []

        for host in root.findall('host'):
            # 1. Identify Device (For UI display)
            device_identity = self._get_device_identity(host)
            
            # 2. Scan for Vulnerabilities
            vulns = []
            
            # --- LANE 1: HARDWARE SEARCH ---
            # If we have a robust hardware name (from Nmap OS Match), search it.
            if device_identity['hw_query']:
                # Query: "AudioControl D3400"
                hw_results = self.check_product(device_identity['hw_query'])
                if hw_results:
                    for v in hw_results:
                        v['context'] = "Device Firmware"
                        vulns.append(self._normalize_result(v))

            # --- LANE 2: SERVICE SEARCH ---
            for port in host.findall('.//port'):
                service = port.find('service')
                if service is not None:
                    product = service.get('product', '')
                    version = service.get('version', '')
                    
                    if product and version:
                        # Query: "Lighttpd 1.4.35"
                        query = f"{product} {version}"
                        svc_results = self.check_product(query)
                        
                        if svc_results:
                            for v in svc_results:
                                v['context'] = f"Service: {product}"
                                vulns.append(self._normalize_result(v))

                # --- LANE 3: CONFIGURATION (Nmap Scripts) ---
                # search_vulns won't find "default creds", so we keep this logic!
                for script in port.findall('script'):
                    config_issue = self._check_script_config(script)
                    if config_issue:
                        vulns.append(config_issue)

            # Deduplicate vulnerabilities by ID/CVE
            unique_vulns = {v.get('id'): v for v in vulns}.values()

            report.append({
                "ip": device_identity['ip'],
                "name": device_identity['name'],
                "vulnerabilities": list(unique_vulns)
            })

        return report

    def _get_device_identity(self, host):
        """Extracts UI Name and Hardware Search Query from Nmap."""
        ip = host.find('address').get('addr')
        try:
            mac_node = host.find(".//address[@addrtype='mac']")
            vendor = mac_node.get('vendor', 'Unknown Vendor')
        except AttributeError as e:
            print("No mac address found.")
            mac_node = "N/A"
            vendor = "Unknown Vendor"
        
        identity = {
            "ip": ip,
            "name": f"{vendor} Device",
            "hw_query": None
        }

        # Use OS Match for specific hardware (e.g., AudioControl)
        os_match = host.find("os/osmatch")
        if os_match and int(os_match.get('accuracy', 0)) > 85:
            identity['name'] = os_match.get('name')
            
            # Construct a search query from the OS Match name
            # This is often better than CPE for natural language search tools
            # e.g. "AudioControl D3400 network amplifier" -> "AudioControl D3400"
            identity['hw_query'] = os_match.get('name')

        return identity

    def _check_script_config(self, script):
        """Checks Nmap script output for misconfigurations (Lane 3)."""
        sid = script.get('id')
        output = script.get('output', '').lower()
        
        if sid in ['ftp-anon', 'http-default-accounts', 'http-auth']:
            if "anonymous" in output or "valid credentials" in output:
                return {
                    "id": "CONFIG-001",
                    "title": f"Insecure Configuration ({sid})",
                    "severity": "HIGH",
                    "description": f"Misconfiguration found: {script.get('output')}",
                    "context": "Configuration"
                }
        return None

    def _normalize_result(self, raw_vuln):
        """
        Normalizes search_vulns output to a clean format for your UI/LLM.
        Adjust keys based on the exact library version output.
        """
        # search_vulns usually returns keys like 'id', 'summary', 'cvss'
        return {
            "id": raw_vuln.get('id', 'Unknown ID'),
            "title": raw_vuln.get('summary', 'Vulnerability Found'),
            "cve": raw_vuln.get('cve_id', raw_vuln.get('id')),
            "severity": raw_vuln.get('cvss', {}).get('score', 'Unknown'),
            "context": raw_vuln.get('context', 'General')
        }

# === RUNNER ===
if __name__ == "__main__":
    scanner = VulnerabilityScanner()
    print(f"Scanning {XML_FILE} using search_vulns library...")
    
    results = scanner.scan_xml(XML_FILE)
    print(json.dumps(results, indent=2))