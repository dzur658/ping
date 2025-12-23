import xml.etree.ElementTree as ET
import sqlite3
import re

# 1. Load your local database
DB_PATH = './vulnerabilities-database/vulnerabilities.db'
XML_TO_PARSE = 'output_windows_all_scripts.xml'

def get_exploits_from_db(product, version):
    """
    Searches the local DB for exploits matching the product and version.
    Returns a list of dictionaries.
    """
    if not product or not version:
        return []

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # STRATEGY: "Fuzzy" matching. 
    # If Nmap finds "Apache httpd 2.4.49", we search for:
    # Title contains "Apache" AND Title contains "2.4.49"
    # AND type is 'remote' or 'webapps' (exclude local stuff)
    
    query = """
        SELECT id, description, type 
        FROM exploits 
        WHERE description LIKE ? 
          AND description LIKE ? 
          AND type IN ('remote', 'webapps')
    """
    
    # Add wildcards for the SQL LIKE operator
    param_product = f"%{product}%"
    param_version = f"%{version}%"
    
    cursor.execute(query, (param_product, param_version))
    results = cursor.fetchall()
    conn.close()

    # Format for the LLM
    mapped_exploits = []
    for row in results:
        mapped_exploits.append({
            "id": row[0],
            "description": row[1],
            "type": row[2]
        })
    return mapped_exploits

def parse_nmap_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    devices_report = []

    for host in root.findall('host'):
        ip = host.find('address').get('addr')
        
        # Get OS / Device Name (from your custom scripts or -O)
        device_name = "Unknown Device"
        os_elem = host.find('os/osmatch')
        if os_elem:
            device_name = os_elem.get('name')
            
        # Check specific ports/services
        services = []
        ports = host.find('ports')
        if ports:
            for port in ports.findall('port'):
                service = port.find('service')
                if service is not None:
                    product = service.get('product') # e.g. "Apache httpd"
                    version = service.get('version') # e.g. "2.4.49"
                    
                    if product and version:
                        # === THE MATCHING HAPPENS HERE ===
                        print(f"Testing Product: {product}, Version: {version} on IP: {ip}")
                        vulns = get_exploits_from_db(product, version)
                        
                        if vulns:
                            services.append({
                                "port": port.get('portid'),
                                "product": product,
                                "version": version,
                                "vulnerabilities": vulns
                            })

        if services:
            devices_report.append({
                "ip": ip,
                "device": device_name,
                "risks": services
            })
            
    return devices_report

# Example Usage
if __name__ == "__main__":
    scan_data = parse_nmap_xml(XML_TO_PARSE)
    
    # Print clean JSON for your LLM or Frontend
    import json
    print(json.dumps(scan_data, indent=2))