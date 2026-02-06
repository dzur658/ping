#!/usr/bin/env python3

# Author: Alex Dzurec
# Date Created: 10/28/2025
# Adapted from source: https://labex.io/tutorials/nmap-how-to-analyze-nmap-scan-results-in-xml-format-415516
# Code Completions: GitHub Copilot, GPT-4.1

import xml.etree.ElementTree as ET
import sys
import json

from vulscan_extraction import extract_vuln_details

CUSTOM_SCRIPTS = ['console-detect-ouis.nse', 
                  'echo-detect-ouis.nse', 
                  'roku-detect-ouis.nse', 
                  'router-detect.nse', 
                  'camera-detect-ouis.nse',
                  ]

def parse_nmap_xml(xml_file):
    try:
        extracted_data = {}

        ## Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Add nmap info to extracted data
        extracted_data['nmap_info'] = {
            'startstr': root.get('startstr'),
            'version': root.get('version'),
            'args': root.get('args')
        }

        ## Process each host in the scan
        for host in root.findall('host'):
             ## Ensure host is up before proceeding
            status = host.find('status')
            if status is None or status.get('state') != 'up':
                continue

            # One address per host
            ip_address = None

            ## Get host addresses
            for addr in host.findall('address'):
                
                if addr.get('addrtype') in ['ipv4', 'ipv6'] and ip_address is None:
                    # Device will be classified by the first ip address nmap found associated with it
                    ip_address = addr.get('addr')

                    extracted_data[ip_address] = {}
                    extracted_data[ip_address]["ip_type"] = addr.get('addrtype')
                
                if addr.get('addrtype') == 'mac':
                    # add mac address to extracted data
                    extracted_data[ip_address]["mac_address"] = addr.get('addr')
                    extracted_data[ip_address]["mac_vendor"] = addr.get('vendor', 'Unknown')
            
            # Skip hosts with no address found
            if ip_address is None:
                continue 

            ## Get hostname if available

            # default value
            extracted_data[ip_address]["hostnames"] = []

             # append host status to extracted data
            extracted_data[ip_address]["status"] = status.get('state')

            hostnames = host.find('hostnames')
            if hostnames is not None:
                for hostname in hostnames.findall('hostname'):
                    # add hostnames to extracted data
                    extracted_data[ip_address]["hostnames"].append(hostname.get('name'))

            ## Process ports
            ports = host.find('ports')
            if ports is not None:
                # Loop through each port
                for port in ports.findall('port'):
                    port_id = port.get('portid')

                    protocol = port.get('protocol')

                    ## Get port state
                    state = port.find('state')
                    port_state = state.get('state') if state is not None else "unknown"

                    ## Skip closed ports
                    if port_state != "open":
                        continue

                    # Add port_id to extracted data
                    extracted_data[ip_address][port_id] = {}
                    
                    # add protocol to extracted data
                    extracted_data[ip_address][port_id]['protocol'] = protocol

                    # add port state to extracted data
                    extracted_data[ip_address][port_id]['state'] = port_state if state is not None else "unknown"

                    ## Get service information
                    service = port.find('service')
                    if service is not None:
                        service_name = service.get('name', '')
                        service_product = service.get('product', '')
                        service_version = service.get('version', '')

                        # add extracted data
                        # extracted_data[ip_address][port_id][service_name] = {
                        #     'product': service_product,
                        #     'version': service_version
                        # }

                        extracted_data[ip_address][port_id]['service_name'] = service_name
                        extracted_data[ip_address][port_id]['service_product'] = service_product
                        extracted_data[ip_address][port_id]['service_version'] = service_version
                    else:
                        service_name = ""

                    ## Extract vulscan script output if available
                    vulscan = port.find("script[@id='vulscan']")
                    if vulscan is not None:
                        vulscan_extracted = extract_vuln_details(vulscan.get('output'))

                        # Add vulscan data to extracted data
                        extracted_data[ip_address][port_id]['vulscan'] = vulscan_extracted


            ## Get OS detection information
            os = host.find('os')
            if os is not None:

                # Initialize osmatch list
                extracted_data[ip_address]['osmatch'] = []

                for portused in os.findall('portused'):
                    for osmatch in os.findall('osmatch'):
                        # print(f"OS: {osmatch.get('name')} (Accuracy: {osmatch.get('accuracy')}%)")

                        # Add osmatch to extracted data
                        match_data = {
                            'name': osmatch.get('name'),
                            'accuracy': osmatch.get('accuracy')
                        }

                        extracted_data[ip_address]['osmatch'].append(match_data)
                        for osclass in os.findall('osclass'):
                            os_type = osclass.get('type')
                            os_vendor = osclass.get('vendor')
                            os_family = osclass.get('family')
                            os_gen = osclass.get('gen')

                            # Add osclass data to extracted data
                            class_data = {
                                'type': os_type,
                                'vendor': os_vendor,
                                'family': os_family,
                                'gen': os_gen,
                                'cpe': []
                            }

                            extracted_data[ip_address]['osmatch'].append(class_data)

                            for cpe in osclass.findall('cpe'):
                                cpe_text = str(cpe.text)
                                class_data['cpe'].append(cpe_text)

                            extracted_data[ip_address]['osmatch'].append(class_data)
            
            ## Get custom nmap json strings
            hostscript = host.find('hostscript')
            if hostscript is not None:
                extracted_data[ip_address]['hostscripts'] = {}
                for script in hostscript.findall('script'):
                    script_id = script.get('id')
                    script_output = script.get('output')

                    # safety check to ensure output exists
                    if script_output:
                        try:
                            # Add hostscript data to extracted data as json string
                            extracted_data[ip_address]['hostscripts'][script_id] = json.loads(script_output.strip())
                        except json.JSONDecodeError as e:
                            print(f"Error decoding JSON for script {script_id}: {e}")
                            print(f"Script output: {script_output}")

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
        with open("extracted_data.json", "w") as f:
            json.dump(result, f, indent=4)
        sys.exit(0)
    else:
        print("Extraction failed.")
        sys.exit(1)