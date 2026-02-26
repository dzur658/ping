import json
import os

def write_out(data, output_path="output.jsonl"):
    """
    Writes the given data to a JSONL file at the specified output path.
    Each item in the data list will be written as a separate line in the JSONL file.
    """
    with open(output_path, "a", encoding="utf-8") as f:
        for item in data:
            json_line = json.dumps(item, ensure_ascii=False)
            f.write(json_line + "\n")