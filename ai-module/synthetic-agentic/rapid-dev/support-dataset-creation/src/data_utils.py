"""Data utilities for loading devices, knowledge base, and writing output."""

import json
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .config import (
    CONSUMER_DEVICES_FILE,
    KNOWLEDGE_BASE_DB,
    MIN_TURNS,
    MAX_TURNS,
)


def load_consumer_devices(filter_pattern: Optional[str] = None) -> List[str]:
    """Load device names from consumer_devices.txt, optionally filtering."""
    with open(CONSUMER_DEVICES_FILE, "r", encoding="utf-8") as f:
        devices = [line.strip() for line in f if line.strip()]

    if filter_pattern:
        devices = [d for d in devices if filter_pattern.lower() in d.lower()]

    return devices


def get_knowledge_base_doc(device_name: str) -> Optional[str]:
    """Retrieve documentation for a specific device from knowledge_base.db."""
    try:
        conn = sqlite3.connect(KNOWLEDGE_BASE_DB)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT documentation FROM knowledge WHERE device_name = ?",
            (device_name,),
        )
        result = cursor.fetchone()
        conn.close()

        if result:
            return result[0]
        return None
    except Exception as e:
        print(f"Error retrieving documentation for {device_name}: {e}")
        return None


def write_conversation_jsonl(
    output_path: Path,
    conversations: List[Dict],
    system_prompt: str,
) -> None:
    """Write conversations to JSONL file in MLX format."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for conv in conversations:
            messages = [{"role": "system", "content": system_prompt}]
            messages.extend(conv["messages"])
            f.write(json.dumps({"messages": messages}, ensure_ascii=False) + "\n")


def get_random_turn_length() -> int:
    """Get a random number of turns between MIN_TURNS and MAX_TURNS."""
    import random

    return random.randint(MIN_TURNS, MAX_TURNS)


def validate_conversation(messages: List[Dict]) -> bool:
    """Validate that a conversation meets quality criteria."""
    user_turns = [m for m in messages if m["role"] == "user"]
    assistant_turns = [m for m in messages if m["role"] == "assistant"]

    if len(user_turns) < 2:
        return False

    if len(assistant_turns) < 2:
        return False

    for msg in messages:
        if not msg["content"].strip():
            return False

    return True
