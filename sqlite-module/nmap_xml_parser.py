# Dev: Alex Dzurec
# Created: 10/17/2025
# AI Tool Used: Gemini 2.5 Pro

"""
A modular Nmap XML parser for extracting host, service, and vulnerability
information and preparing it for database storage.

Modularity is achieved via the XML_MAPPING dictionary. To parse new XML 
attributes or elements, simply add a new key-value pair to the dictionary.
The key is the desired field name, and the value is the relative XPath to 
the data from a <port> element.
"""

import xml.etree.ElementTree as ET
import re
import pprint
from typing import List, Dict, Any, Optional

# This mapping dictionary is the core of the modular design.
# To extract a new piece of data, add an entry here.
# Key: The name you want for the data field.
# Value: The relative XPath from a <port> element to the data.
# Note: Use './' for elements/attributes of the port itself.
#       Use '../' to access parent <host> level elements/attributes.

# Define separate, clearer mappings for host-level and port-level data
HOST_MAPPING = {
    'host_ip': './address[@addrtype="ipv4"]/@addr',
    'hostname': './hostnames/hostname/@name',
}
PORT_MAPPING = {
    'port': './@portid',
    'protocol': './@protocol',
    'service_name': './service/@name',
    'service_product': './service/@product',
    'service_version': './service/@version',
    'vulscan_output': "./script[@id='vulscan']/@output"
}

"""
    Parses the raw text output from the vulscan.nse script into a structured list.

    Args:
        raw_text: The string content from the 'output' attribute of a vulscan script tag.

    Returns:
        A list of dictionaries, where each dictionary represents a single vulnerability.
"""
def _parse_vulscan_output(raw_text: Optional[str]) -> List[Dict[str, str]]:
    # Check to ensure input has properly been passed
    if not raw_text:
        return []

    # Initialize vulnerability list
    vulnerabilities = []
    # Split the raw text into sections for each vulnerability database (e.g., MITRE CVE, VulDB).
    sections = raw_text.strip().split('\n\n')
    
    # Regex pattern to capture vulnerability ID (CVE) and description.
    vuln_pattern = re.compile(r'\[(.*?)\]\s*(.*)')

    # loop through each section
    for section in sections:
        # detect and split on separate lines in each section
        lines = section.split('\n')
        # The first line contains the database name and URL.
        db_name_line = lines[0].split('-')[0].strip()

        # Loop through each line in the section after the first
        for line in lines[1:]:
            # Use the regex pattern to extract vulnerability details (CVE ID and description).
            # Then clean the output.
            match = vuln_pattern.match(line.strip())
            # Activate if the line matches the expected format
            if match:
                # Unpack regex tuple
                vuln_id, description = match.groups()
                # Create a dictionary to store details in the vulnerabilities list
                vulnerabilities.append({
                    # MITRE, VulDB, etc. (db of origin for CVE)
                    'database': db_name_line,
                    # CVE ID
                    'id': vuln_id.strip(),
                    # Description of the vulnerability from xml
                    'description': description.strip()
                })
    # RReturn all found vulnerabilities
    return vulnerabilities

"""
    Parses an Nmap XML file to extract details for each service on each host.

    This function iterates through each host and port defined in the XML file,
    using the XML_MAPPING dictionary to dynamically extract the desired data.

    Args:
        xml_file: The path to the Nmap XML output file.

    Returns:
        A list of dictionaries, where each dictionary contains the parsed
        details for a single service (port) on a host.
"""
def parse_nmap_xml(xml_file: str) -> List[Dict[str, Any]]:
    # Attempt to parse XML file, throw an exception if it fails
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"Error reading or parsing XML file: {e}")
        return []

    # List to hold all parsed service data
    all_services_data = []
    
    # Iterate over each host found in the scan
    for host in root.findall('host'):
        
        # 1. Extract host-level data (host ip and hostname) ONCE per host
        host_details = {}
        for field_name, xpath in HOST_MAPPING.items():
            path, _, attrib = xpath.rpartition('/@')
            element = host.find(path)
            if element is not None:
                value = element.get(attrib) if attrib else element.text
                host_details[field_name] = value.strip() if value else None
            else:
                host_details[field_name] = None
        
        # Iterate over each port found for the current host
        for port in host.findall('.//port'):
            
            # 2. Start with a copy of the host data
            service_details = host_details.copy()
            
            # 3. Add port-specific data
            for field_name, xpath in PORT_MAPPING.items():
                path, _, attrib = xpath.rpartition('/@')
                element = port.find(path)
                if element is not None:
                    value = element.get(attrib) if attrib else element.text
                    service_details[field_name] = value.strip() if value else None
                else:
                    service_details[field_name] = None
            
            # 4. Special handling for vulscan output (same as before)
            if service_details.get('vulscan_output'):
                raw_output = service_details.pop('vulscan_output')
                service_details['vulnerabilities'] = _parse_vulscan_output(raw_output)
            
            all_services_data.append(service_details)

    return all_services_data

"""
    Placeholder function to handle storing parsed data in an SQLite database.

    This function would contain the logic to connect to an SQLite database,
    create the necessary tables if they don't exist, and insert or update
    the records with the provided service data.

    Args:
        service_data: A dictionary containing all details for a single service.
"""
def store_in_database(service_data: Dict[str, Any]):
    # TODO: Implement the actual SQLite database storage logic here.
    # This would involve:
    # 1. Connecting to the database: conn = sqlite3.connect('vulnerabilities.db')
    # 2. Creating a cursor: cur = conn.cursor()
    # 3. Defining table schemas (e.g., for hosts, services, vulnerabilities).
    # 4. Executing INSERT or UPDATE statements.
    #    For example:
    #    cur.execute("INSERT INTO services (...) VALUES (?, ?, ...)", (service_data['host_ip'], ...))
    # 5. Committing the changes: conn.commit()
    # 6. Closing the connection: conn.close()
    
    print("--- Storing data for service: ---")
    pprint.pprint(service_data)
    print("-" * 35 + "\n")


if __name__ == '__main__':
    # Point to the nmap output file (XML format)
    NMAP_OUTPUT_FILE = 'example_output.xml'
    
    # 1. Parse the XML data
    parsed_data = parse_nmap_xml(NMAP_OUTPUT_FILE)
    
    if not parsed_data:
        print("No data was parsed from the XML file.")
    else:
        print(f"Successfully parsed data for {len(parsed_data)} services.\n")
        # 2. Iterate and "store" each result (currently prints to console)
        for service in parsed_data:
            store_in_database(service)