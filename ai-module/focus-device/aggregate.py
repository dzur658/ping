# create the master list of all devices to focus on for training
import pandas as pd

file_names = [
    "cameras.csv",
    "nas.csv",
    "primary_devices.csv",
    "printers.csv",
    "routers.csv",
    "smart_hubs.csv",
    "smart_tvs.csv"
]

dfs = []
for file_name in file_names:
    df = pd.read_csv(file_name)
    print(f"File: {file_name}, Columns: {df.columns.tolist()}")
    dfs.append(df)

master_df = pd.concat(dfs, ignore_index=True)
master_df.to_csv("master_devices.csv", index=False)

print("\nMaster DataFrame Head:")
print(master_df.head())
print(f"\nTotal rows: {len(master_df)}")