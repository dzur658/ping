# importing full files to hopefully help with exe conversion?
# NOTE: even though only 2 scripts are imported here, all the scripts
# are necessary as these script will call the other subscripts in the branch.
import nmap_labex_parser
import sqlite_insertion

# standard library imports
import json
import sqlite3

# hard code file names for simplicity (also not really necessary to change)
# NOTE: in python you can drop relative or absolute paths into these strings, and
# everything will still function properly.
XML_FILE = "samples/output_windows_all_scripts.xml"
JSON_FILE = "extracted_data.json"
DB_FILE = "network_scans.db"

# first extract xml
extracted_data = nmap_labex_parser.parse_nmap_xml(XML_FILE)

# dump to json for next step (if there is a need to debug)
# with open(JSON_FILE, 'w') as json_file:
#     json.dump(extracted_data, json_file, indent=4)

try:
    # now insert into sqlite
    conn = sqlite3.connect(DB_FILE)

    # ensure tables exist, or create them if not
    sqlite_insertion.create_tables(conn)

    # insert the parsed data
    sqlite_insertion.insert_data_from_json(conn, extracted_data)

except sqlite3.Error as e:
    print(f"SQLite error: {e}")
finally:
    # ensures connection closes although python does this automatically
    # in normal circumstances
    if conn:
        conn.close()