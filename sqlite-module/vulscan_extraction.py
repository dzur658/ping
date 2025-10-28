# Author: Alex Dzurec
# Date Created: 10/28/2025
# Model Used for Generation: Gemini 2.5 Pro
# Code Completions: GitHub Copilot, GPT-4.1

import re
from typing import List, Dict

"""
    Parses Nmap/Vulscan output text to extract vulnerability details:
    database source, ID, and description.

    Args:
        text_block: A string containing the formatted vulscan output.

    Returns:
        A list of dictionaries, each with 'database', 'id', and 'description'.
"""
def extract_vuln_details(text_block: str) -> List[Dict[str, str]]:
    vulnerabilities = []
    current_db = "Unknown" # Default if no header is found first

    # Regex for DB header lines (e.g., "MITRE CVE - https://...")
    # Captures the DB name before " - http"
    db_header_pattern = re.compile(r'^([^-]+) - https?://.*:$')

    # Regex for vulnerability lines (e.g., "[CVE-XXXX] Description...")
    # Captures ID inside [] and the rest of the line as description
    vuln_pattern = re.compile(r'^\[(.*?)\]\s*(.*)')

    for line in text_block.strip().split('\n'):
        line = line.strip()
        if not line:
            continue

        # 1. Check if the line is a database header
        header_match = db_header_pattern.match(line)
        if header_match:
            current_db = header_match.group(1).strip() # Update DB source
            continue # Don't process header line as a vulnerability

        # 2. Check if the line is a vulnerability entry
        vuln_match = vuln_pattern.match(line)
        if vuln_match:
            vuln_id, description = vuln_match.groups()
            # Append using the *last seen* database name
            vulnerabilities.append({
                'database': current_db,
                'id': vuln_id.strip(),
                'description': description.strip()
            })

    # returns a list of dictionaries
    return vulnerabilities