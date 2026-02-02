#!/usr/bin/env python3
import json
from pathlib import Path

NEW_SYSTEM_PROMPT = """You are an expert network diagnostic assistant helping home users identify devices on their network.

Given Nmap scan data, your goal is to identify the SPECIFIC device model.

CORE PROTOCOL:
1. START with a <think> block to analyze the data.
2. DETERMINE if the device is specific (e.g. "OnePlus 10 Pro") or generic (e.g. "OnePlus Technology").
3. END with EXACTLY ONE of the following tags:

[OPTION 1: IDENTIFIED]
If you are 90% certain of the specific model:
<device>Exact Model Name</device>

[OPTION 2: AMBIGUOUS]
If you are NOT certain or need user confirmation:
<question>The clarifying question you want to ask the user</question>

CRITICAL RULES:
- NEVER use <device> and <question> in the same response.
- NEVER output plain text outside of tags."""

def wrap_question(content: str) -> str:
    if "<device>" in content:
        return content

    if "</think>" in content:
        parts = content.split("</think>", 1)
        return f"{parts[0]}</think><question>{parts[1]}</question>"

    return content


def main():
    input_path = Path("master.jsonl")
    output_path = Path("master_wrapped.jsonl")

    with open(input_path) as f_in, open(output_path, "w") as f_out:
        for line in f_in:
            data = json.loads(line)
            for msg in data["messages"]:
                if msg["role"] == "assistant":
                    msg["content"] = wrap_question(msg["content"])
                elif msg["role"] == "system":
                    msg["content"] = NEW_SYSTEM_PROMPT
            f_out.write(json.dumps(data) + "\n")


if __name__ == "__main__":
    main()
