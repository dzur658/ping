#!/usr/bin/env python3

# Author: Alex Dzurec
# Date Created: 10/28/2025
# Adapted from source: https://labex.io/tutorials/nmap-how-to-analyze-nmap-scan-results-in-xml-format-415516
# Code Completions: GitHub Copilot, GPT-4.1

import xml.etree.ElementTree as ET
import sys
import json

from vulscan_extraction import extract_vuln_details

def parse_nmap_xml(xml_file):
    try:
        extracted_data = {}

        ## Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        ## Print scan information
        print("Nmap Scan Report")
        print("=" * 50)
        print(f"Scan started at: {root.get('startstr')}")
        print(f"Nmap version: {root.get('version')}")
        print(f"Nmap command: {root.get('args')}")
        print("=" * 50)

        # Add nmap info to extracted data
        extracted_data['nmap_info'] = {
            'startstr': root.get('startstr'),
            'version': root.get('version'),
            'args': root.get('args')
        }

        ## Process each host in the scan
        for host in root.findall('host'):

            ## Get host addresses
            for addr in host.findall('address'):

                # distinguish between ipv4 and ipv6
                if addr.get('addrtype') == 'ipv4':
                    ip_address = addr.get('addr')
                    print(f"\nHost: {ip_address}")

                    # Put ip addr in dictionary
                    extracted_data[ip_address] = {}
                    extracted_data[ip_address]["ip_type"] = "ipv4"
                elif addr.get('addrtype') == 'ipv6':
                    ip_address = addr.get('addr')
                    print(f"\nHost: {ip_address}")

                    # Put ip addr in dictionary
                    extracted_data[ip_address] = {}
                    extracted_data[ip_address]["ip_type"] = "ipv6"

            ## Get hostname if available

            # default value
            extracted_data[ip_address]["hostnames"] = []

            hostnames = host.find('hostnames')
            if hostnames is not None:
                for hostname in hostnames.findall('hostname'):
                    print(f"Hostname: {hostname.get('name')}")
                    
                    # add hostnames to extracted data
                    extracted_data[ip_address]["hostnames"].append(hostname.get('name'))

            ## Get host status
            status = host.find('status')
            if status is not None:
                print(f"Status: {status.get('state')}")

                # append host status to extracted data
                extracted_data[ip_address]["status"] = status.get('state')

            ## Process ports
            ports = host.find('ports')
            if ports is not None:
                print("\nOpen Ports:")
                print("-" * 50)
                print(f"{'PORT':<10}{'STATE':<10}{'SERVICE':<15}{'VERSION'}")
                print("-" * 50)

                for port in ports.findall('port'):
                    port_id = port.get('portid')

                    # Add port_id to extracted data
                    extracted_data[ip_address][port_id] = {}

                    protocol = port.get('protocol')

                    # add protocol to extracted data
                    extracted_data[ip_address][port_id]['protocol'] = protocol

                    ## Get port state
                    state = port.find('state')
                    port_state = state.get('state') if state is not None else "unknown"

                    ## Skip closed ports
                    if port_state != "open":
                        continue

                    # add port state to extracted data
                    extracted_data[ip_address][port_id]['state'] = port_state if state is not None else "unknown"

                    ## Get service information
                    service = port.find('service')
                    if service is not None:
                        service_name = service.get('name', '')
                        service_product = service.get('product', '')
                        service_version = service.get('version', '')
                        service_info = f"{service_product} {service_version}".strip()

                        # add extracted data
                        extracted_data[ip_address][port_id][service_name] = {
                            'product': service_product,
                            'version': service_version
                        }
                    else:
                        service_name = ""
                        service_info = ""

                    ## Extract vulscan script output if available
                    vulscan = port.find("script[@id='vulscan']")
                    if vulscan is not None:
                        vulscan_extracted = extract_vuln_details(vulscan.get('output'))
                        print("\nVulnerabilities Found:")
                        print("-" * 50)
                        for vuln in vulscan_extracted:
                            print(vuln)
                        print("-" * 50)

                        # Add vulscan data to extracted data
                        extracted_data[ip_address][port_id]['vulscan'] = vulscan_extracted

                    print(f"{port_id}/{protocol:<5} {port_state:<10}{service_name:<15}{service_info}")

            ## Get OS detection information
            os = host.find('os')
            if os is not None:
                print("\nOS Detection:")
                for osmatch in os.findall('osmatch'):
                    print(f"OS: {osmatch.get('name')} (Accuracy: {osmatch.get('accuracy')}%)")

                    # Add osmatch to extracted data
                    extracted_data[ip_address]['osmatch'] = {
                        'name': osmatch.get('name'),
                        'accuracy': osmatch.get('accuracy')
                    }

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

    return extracted_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <nmap_xml_file>")
        sys.exit(1)

    xml_file = sys.argv[1]
    
    result = parse_nmap_xml(xml_file)
    if result:
        print("\nExtraction completed successfully.")
        with open("extracted_data.json", "w") as f:
            json.dump(result, f, indent=4)
        print("Extracted data saved to extracted_data.json")
    else:
        print("Extraction failed.")
    
