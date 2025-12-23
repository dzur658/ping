import pandas as pd
import sqlite3
import requests

def build_database():
    # 1. Download the official Exploit-DB CSV
    url = "https://gitlab.com/exploit-database/exploitdb/-/raw/main/files_exploits.csv"
    print("Downloading Exploit-DB CSV...")
    df = pd.read_csv(url)

    # 2. Filter for "Remote" exploits only (since you are scanning over network)
    #    and remove ancient noise to save space (optional)
    df = df[df['type'].isin(['Remote', 'webapps'])] 

    # 3. Save to SQLite
    conn = sqlite3.connect('./vulnerabilities_database/vulnerabilities.db')
    df.to_sql('exploits', conn, if_exists='replace', index=False)
    
    # 4. Create an index for fast searching on "description"
    conn.execute("CREATE INDEX idx_desc ON exploits(description)")
    conn.close()
    print("vulnerabilities.db build complete.")

if __name__ == "__main__":
    build_database()