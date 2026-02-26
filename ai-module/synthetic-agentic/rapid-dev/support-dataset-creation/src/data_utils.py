"""Data utilities for loading devices, knowledge base, and writing output."""

import json
import re
import sqlite3
from pathlib import Path
from typing import Dict, List, Optional

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


def swap_reasoning_for_think(content: str) -> str:
    """Replace <reasoning> tags with think tags in the text.

    Args:
        content: Text containing <reasoning>...</reasoning> tags

    Returns:
        Text with <reasoning> replaced by think tags
    """
    if not content:
        return ""

    content = re.sub(r"<\s*reasoning\s*>", "<think>", content, flags=re.IGNORECASE)
    content = re.sub(r"<\s*/\s*reasoning\s*>", "</think>", content, flags=re.IGNORECASE)
    return content


def write_conversation_jsonl(
    output_path: Path,
    conversations: List[Dict],
    system_prompt: str,
) -> None:
    """Write conversations to JSONL file in MLX format.

    Assistant messages contain <reasoning> tags which are swapped to <think> tags.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for conv in conversations:
            messages = [{"role": "system", "content": system_prompt}]
            for msg in conv["messages"]:
                if msg["role"] == "user":
                    messages.append(
                        {
                            "role": "user",
                            "content": sanitize_user_bot_message(msg["content"]),
                        }
                    )
                elif msg["role"] == "assistant":
                    messages.append(
                        {
                            "role": "assistant",
                            "content": swap_reasoning_for_think(msg["content"]),
                        }
                    )
                else:
                    messages.append(msg)
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

    for i in range(1, len(messages)):
        if messages[i]["role"] == messages[i - 1]["role"]:
            return False

    if messages and messages[-1]["role"] != "assistant":
        return False

    return True


def strip_think_tags(content: str) -> str:
    """Remove think blocks and their content from text."""
    if not content:
        return ""
    pattern = r"<\s*think\b[^>]*>.*?<\s*/\s*think\s*>"
    cleaned = re.sub(pattern, "", content, flags=re.DOTALL | re.IGNORECASE)
    return cleaned.strip()


def sanitize_user_bot_message(content: str) -> str:
    """Strip think tags, system-reminder tags, and wrapping quotes from user bot output."""
    if not content:
        return ""

    content = strip_think_tags(content)

    if _contains_block_tag(content, "system-reminder"):
        return "FAILURE"

    if not content:
        return ""

    # Remove wrapping quotation marks model may add around dialogue
    content = content.strip()
    if len(content) >= 2 and content[0] == content[-1] and content[0] in ('"', "'"):
        content = content[1:-1].strip()

    return content


def _contains_block_tag(content: str, tag: str) -> bool:
    """Check if content includes a specific tag name."""
    return re.search(rf"(?is)<\s*{re.escape(tag)}\b", content) is not None
