# Dev: Alex Dzurec
# Created: 10/17/2025
# AI Tool Used: Gemini 2.5 Pro
# Refactored with xmltodict on 10/25/2025
# Simplified on 10/25/2025

"""
A simplified Nmap XML parser using xmltodict, extracting host, service, 
and vulnerability information.
"""

import xmltodict
import re
import pprint
from typing import List, Dict, Any, Optional, Union
import json

# --- Helper Function ---
def _ensure_list(item: Optional[Union[Dict, List]]) -> List:
    """Ensures the input item is a list. If None, returns empty list."""
    if item is None:
        return []
    if isinstance(item, list):
        return item
    return [item] # Wrap single dict in a list

# --- Vulnerability Parsing (Unchanged) ---
def _parse_vulscan_output(raw_text: Optional[str]) -> List[Dict[str, str]]:
    """
    Parses the raw text output from the vulscan.nse script into a structured list.
    """
    if not raw_text:
        return []

    vulnerabilities = []
    sections = raw_text.strip().split('\n\n')
    vuln_pattern = re.compile(r'\[(.*?)\]\s*(.*)')

    for section in sections:
        lines = section.split('\n')
        if not lines: continue # Skip empty sections
        db_name_line = lines[0].split('-')[0].strip()

        for line in lines[1:]:
            match = vuln_pattern.match(line.strip())
            if match:
                vuln_id, description = match.groups()
                vulnerabilities.append({
                    'database': db_name_line,
                    'id': vuln_id.strip(),
                    'description': description.strip()
                })
    return vulnerabilities

# --- Main Parsing Function (Simplified) ---
def parse_nmap_xml(xml_file: str) -> List[Dict[str, Any]]:
    """
    Parses an Nmap XML file by converting it to a dictionary first.
    Simplified logic using .get() and a list helper.
    """
    all_services_data = []
    
    try:
        with open(xml_file, 'r', encoding='utf-8') as f:
            nmap_data = xmltodict.parse(f.read())
    except (IOError, xmltodict.expat.ExpatError) as e:
        print(f"Error reading or parsing XML file: {e}")
        return []

    # Use .get() chaining and the helper to safely get the list of hosts
    hosts = _ensure_list(nmap_data.get('nmaprun', {}).get('host'))

    for host in hosts:
        # --- 1. Extract host-level data ---
        host_ip = None
        # Find IPv4 address within the list of addresses
        for addr in _ensure_list(host.get('address')):
            if addr.get('@addrtype') == 'ipv4':
                host_ip = addr.get('@addr')
                break # Found IPv4, stop looking

        hostname = None
        # Get the first hostname if available
        hostname_list = _ensure_list(host.get('hostnames', {}).get('hostname'))
        if hostname_list:
            hostname = hostname_list[0].get('@name')

        host_details = {
            'host_ip': host_ip,
            'hostname': hostname
        }

        # --- 2. Extract port-level data ---
        ports = _ensure_list(host.get('ports', {}).get('port'))

        for port in ports:
            service_details = host_details.copy() # Start with host info

            # Basic port info
            service_details['port'] = port.get('@portid')
            service_details['protocol'] = port.get('@protocol')

            # Service info (handle missing service tag gracefully)
            service_info = port.get('service', {}) or {} # Ensure it's a dict
            service_details['service_name'] = service_info.get('@name')
            service_details['service_product'] = service_info.get('@product')
            service_details['service_version'] = service_info.get('@version')

            # --- 3. Extract script (vulscan) data ---
            raw_output = None
            # Find the vulscan script output
            for script in _ensure_list(port.get('script')):
                 if script.get('@id') == 'vulscan':
                    raw_output = script.get('@output')
                    break # Found vulscan, stop looking

            # Parse the raw vulscan output
            service_details['vulnerabilities'] = _parse_vulscan_output(raw_output)
            
            all_services_data.append(service_details)

    return all_services_data

# --- Database Placeholder (Unchanged) ---
def store_in_database(service_data: Dict[str, Any]):
    """ Placeholder function for database storage. """
    print("--- Storing data for service: ---")
    pprint.pprint(service_data)
    print("-" * 35 + "\n")

# --- Main Execution ---
if __name__ == '__main__':
    NMAP_OUTPUT_FILE = 'example_output.xml' 
    
    parsed_data = parse_nmap_xml(NMAP_OUTPUT_FILE)
    
    if not parsed_data:
        print("No data was parsed from the XML file.")
    else:
        print(f"Successfully parsed data for {len(parsed_data)} services.\n")
        
        # Output as JSON:
        json_output = json.dumps(parsed_data, indent=4)
        print(json_output)

        # Use the placeholder database function:
        for service in parsed_data:
            store_in_database(service)