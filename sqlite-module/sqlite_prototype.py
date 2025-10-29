#!/usr/bin/env python3

# Author: Alex Dzurec
# Date Created: 10/28/2025
# Model Used for Generation: Gemini 2.5 Pro
# Code Completions: GitHub Copilot, GPT-4.1

import sqlite3
import json
import sys
from datetime import datetime

# internal scripts
from sqlite_creation import create_tables

# Define the database file name
DB_FILE = "network_scans.db"

"""
    Parses the full JSON object and inserts it into the SQLite database.
    This all happens in one "transaction" to be safe and fast.
"""
def insert_data_from_json(conn, json_data):
    cursor = conn.cursor()
    
    try:
        # === 1. INSERT THE SCAN (PARENT) ===
        
        nmap_info = json_data['nmap_info']
        
        # Convert the string timestamp to an integer
        # Format: "Tue Sep 30 16:40:48 2025"
        string_format = "%a %b %d %H:%M:%S %Y"
        dt_object = datetime.strptime(nmap_info['startstr'], string_format)
        timestamp_int = int(dt_object.timestamp())
        
        cursor.execute(
            "INSERT INTO Scan (startTime, version, nmapArgs) VALUES (?, ?, ?)",
            (timestamp_int, nmap_info['version'], nmap_info['args'])
        )
        # Get the ID of the scan we just inserted
        scan_id = cursor.lastrowid
        
        # === 2. LOOP AND INSERT HOSTS ===
        
        # Iterate through all items, but skip the 'nmap_info' key
        for ip_address, host_data in json_data.items():
            # Skips the nmap_info section (we only need this once per scan)
            if ip_address == 'nmap_info':
                continue
            
            # Convert lists/objects to JSON strings for storage (if none an empty list will be returned)
            hostnames_json = json.dumps(host_data.get('hostnames', []))
            osmatch_json = json.dumps(host_data.get('osmatch', []))
            
            cursor.execute(
                "INSERT INTO hosts (scanId, ipAddress, hostnames, status, inferOs) VALUES (?, ?, ?, ?, ?)",
                (scan_id, ip_address, hostnames_json, host_data.get('status'), osmatch_json)
            )
            # Get the ID of the host we just inserted
            host_id = cursor.lastrowid
            
            # === 3. LOOP AND INSERT SERVICES ===
            
            for port_id, port_data in host_data.items():
                # This is a check to see if the item is a port dictionary
                # It filters out keys like 'hostnames', 'status', etc.
                if isinstance(port_data, dict) and 'protocol' in port_data:
                    
                    cursor.execute(
                        """
                        INSERT INTO services (hostId, port, protocol, state, serviceName, serviceProduct, serviceVersion)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            host_id,
                            int(port_id),
                            port_data.get('protocol'),
                            port_data.get('state'),
                            port_data.get('service_name'),
                            port_data.get('service_product'),
                            port_data.get('service_version')
                        )
                    )
                    # Get the ID of the service we just inserted
                    service_id = cursor.lastrowid
                    
                    # === 4. LOOP AND INSERT VULNERABILITIES ===
                    
                    if 'vulscan' in port_data and isinstance(port_data['vulscan'], list):
                        # Iterate directly over the list of vulnerability dictionaries
                        for vuln in port_data['vulscan']:
                            # Extract data using .get() for safety
                            source = vuln.get('database') 
                            vuln_id = vuln.get('id')
                            description = vuln.get('description')

                            # Make sure we have at least an ID or description before inserting (safety check)
                            if source and (vuln_id or description):
                                cursor.execute(
                                    """
                                    INSERT INTO vulnerabilities (serviceId, cveSource, cveId, description)
                                    VALUES (?, ?, ?, ?)
                                    """,
                                    (service_id, source, vuln_id, description) 
                                )
                                
        # All data has been inserted, so we "commit" the changes
        conn.commit()
        print(f"Successfully inserted all data for Scan ID: {scan_id}")

    except Exception as e:
        # If any error occurs, "roll back" all changes
        print(f"An error occurred: {e}")
        print("Rolling back all changes.")
        conn.rollback()

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <extracted_data.json>")
        sys.exit(1)
        
    json_file = sys.argv[1]
    
    conn = None
    try:
        # Load the JSON data from the file
        with open(json_file, 'r') as f:
            data = json.load(f)
            
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_FILE)
        
        # Ensure tables exist
        create_tables(conn)
        
        # Insert the data
        insert_data_from_json(conn, data)
        
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{json_file}'.")
    except sqlite3.Error as e:
        print(f"A database error occurred: {e}")
    finally:
        # Always close the connection
        if conn:
            conn.close()

if __name__ == "__main__":
    main()