#!/usr/bin/env python3

# Author: Alex Dzurec
# Date Created: 10/28/2025
# Model Used for Generation: Gemini 2.5 Pro
# Code Completions: GitHub Copilot, GPT-4.1

"""
    Creates the 4-table schema if it doesn't already exist.
"""
def create_tables(conn):
    cursor = conn.cursor()
    
    # I've corrected the typos from the diagram (e.g., serviceProduct)
    # Using 'IF NOT EXISTS' is safe to run every time.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Scan (
        scanId INTEGER PRIMARY KEY,
        startTime INTEGER NOT NULL,
        version TEXT,
        nmapArgs TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hosts (
        hostId INTEGER PRIMARY KEY,
        scanId INTEGER NOT NULL,
        ipAddress TEXT NOT NULL,
        hostnames TEXT,
        status TEXT,
        inferOs TEXT,
        FOREIGN KEY (scanId) REFERENCES Scan (scanId)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS services (
        serviceId INTEGER PRIMARY KEY,
        hostId INTEGER NOT NULL,
        port INTEGER NOT NULL,
        protocol TEXT,
        state TEXT,
        serviceName TEXT,
        serviceProduct TEXT,
        serviceVersion TEXT,
        FOREIGN KEY (hostId) REFERENCES hosts (hostId)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vulnerabilities (
        vulnId INTEGER PRIMARY KEY,
        serviceId INTEGER NOT NULL,
        cveSource TEXT,
        cveId TEXT,
        description TEXT,
        FOREIGN KEY (serviceId) REFERENCES services (serviceId)
    );
    """)
    
    conn.commit()
    # print("Tables ensured to exist.")