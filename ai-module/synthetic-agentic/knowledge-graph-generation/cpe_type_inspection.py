import json
import sys
from collections import Counter
from typing import Any

def classify_config(config: Any) -> str:
    if config is None:
        return "none"
    if isinstance(config, list):
        return "list"
    if isinstance(config, dict):
        if "configurations" in config:
            return "dict(configurations)"
        if "nodes" in config or "operator" in config:
            return "dict(nodes-tree)"
        return "dict(other)"
    return type(config).__name__

def main(path: str) -> None:
    counts = Counter()
    total = 0

    with open(path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"[line {line_no}] JSON parse error: {e}")
                continue

            for vendor, cve_list in obj.items():
                if not isinstance(cve_list, list):
                    continue
                for cve in cve_list:
                    total += 1
                    cve_id = cve.get("cve_id", "UNKNOWN")
                    config = cve.get("config_data")
                    cfg_type = classify_config(config)

                    counts[cfg_type] += 1
                    print(f"{vendor} | {cve_id} -> {cfg_type}")
                    if "dict" in cfg_type:
                        if config != { "configurations": [] }:
                            print(json.dumps(cve, indent=2))

    print("\nSummary:")
    for t, n in counts.items():
        print(f"  {t}: {n}")
    print(f"  total: {total}")

if __name__ == "__main__":
    default_path = "/Users/dzurec/ping/ai-module/synthetic-agentic/samples/discovered_cves.jsonl"
    main(sys.argv[1] if len(sys.argv) > 1 else default_path)