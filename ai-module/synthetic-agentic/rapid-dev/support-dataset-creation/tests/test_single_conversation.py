"""Test script to generate and display a single training example."""

import argparse
import json
import sqlite3
import sys
from pathlib import Path
from typing import Dict, Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import (
    OLLAMA_BASE_URL,
    DEFAULT_OLLAMA_MODEL,
    CONSUMER_DEVICES_FILE,
    KNOWLEDGE_BASE_DB,
    USER_MODEL_KWARGS,
    ASSISTANT_MODEL_KWARGS,
    MAX_TURNS,
)
from src.llm_client import create_assistant_agent, create_user_model
from src.conversation_engine import ConversationEngine
from src.personas import get_random_persona, get_persona_prompt
from src.prompts import ASSISTANT_SYSTEM_PROMPT, CLEAN_ASSISTANT_SYSTEM_PROMPT
from src.data_utils import get_knowledge_base_doc, sanitize_user_bot_message
from src.tools.playwright_tool import search_web


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate a single conversation for testing"
    )
    parser.add_argument(
        "--device",
        type=str,
        default=None,
        help="Specific device to generate conversation for (random if not specified)",
    )
    parser.add_argument(
        "--turns",
        type=int,
        default=MAX_TURNS,
        help=f"Number of turns to generate (`MAX_TURNS` if not specified, max {MAX_TURNS})",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output/test_conversation.jsonl",
        help="Output JSONL file path",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_OLLAMA_MODEL,
        help="Ollama model to use",
    )
    parser.add_argument(
        "--user-model",
        type=str,
        default=None,
        help="Separate model for user responses (uses --model if not specified)",
    )
    parser.add_argument(
        "--ollama-url",
        type=str,
        default=OLLAMA_BASE_URL,
        help="Ollama API base URL",
    )
    return parser.parse_args()


def get_random_device_with_docs() -> str:
    """Pick a random device that has knowledge base documentation."""
    devices = []
    with open(CONSUMER_DEVICES_FILE, "r", encoding="utf-8") as f:
        devices = [line.strip() for line in f if line.strip()]

    conn = sqlite3.connect(KNOWLEDGE_BASE_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT device_name FROM knowledge")
    devices_with_docs = set(row[0] for row in cursor.fetchall())
    conn.close()

    devices_with_kb = [d for d in devices if d in devices_with_docs]
    return devices_with_kb[0] if devices_with_kb else ""


def print_header(device_name: str, persona: Dict) -> None:
    """Print conversation header information."""
    print("=" * 60)
    print(f"Device: {device_name}")
    print(f"Persona: {persona['name']} (Tech Level: {persona['tech_level']}/5)")
    print(f"Personality: {persona['style']}")
    print("=" * 60)
    print()


def print_conversation(messages: list, persona_name: str) -> None:
    """Print the full conversation with formatting."""
    think_open = "<think>"
    think_close = "</think>"

    for i, msg in enumerate(messages):
        role = msg["role"]
        content = msg.get("content", "")

        if role == "user":
            print(f"👤 {persona_name}:")
            print(f"  {content}")
        elif role == "assistant":
            # Assistant content now contains think tags
            print("🤖 Assistant:")
            lines = content.split("\n")
            in_think_block = False
            for line in lines:
                stripped = line.strip()
                if stripped.startswith(think_open):
                    in_think_block = True
                    continue
                if stripped.endswith(think_close):
                    in_think_block = False
                    continue
                if in_think_block:
                    print(f"  [THINK] {line}")
                else:
                    print(f"  {line}")
        else:
            print(f"[{role.upper()}]:")

        print()
        print("-" * 60)
        print()


def print_footer(total_messages: int, user_turns: int, assistant_turns: int) -> None:
    """Print conversation summary footer."""
    print("=" * 60)
    print(f"Total messages: {total_messages}")
    print(f"User turns: {user_turns}")
    print(f"Assistant turns: {assistant_turns}")
    print("=" * 60)


def write_output(output_path: str, conversation: Dict, system_prompt: str) -> None:
    """Write conversation to JSONL file in MLX format."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        messages = [{"role": "system", "content": system_prompt}]
        for msg in conversation["messages"]:
            if msg["role"] == "user":
                messages.append(
                    {
                        "role": "user",
                        "content": sanitize_user_bot_message(msg["content"]),
                    }
                )
            elif msg["role"] == "assistant":
                messages.append({"role": "assistant", "content": msg["content"]})
        f.write(json.dumps({"messages": messages}, ensure_ascii=False) + "\n")

    print(f"\n✓ Written to: {output_path}")


async def main() -> None:
    """Generate a single conversation and display it."""
    args = parse_args()

    if args.seed is not None:
        import random

        random.seed(args.seed)

    # Get device name
    device_name = args.device or get_random_device_with_docs()
    if not device_name:
        print("Error: No valid device found with knowledge base documentation")
        return

    # Load knowledge base doc
    kb_doc = get_knowledge_base_doc(device_name)
    if not kb_doc:
        print(f"Error: No knowledge base entry for {device_name}")
        return

    # Build model kwargs
    user_kwargs = dict(USER_MODEL_KWARGS)
    assistant_kwargs = dict(ASSISTANT_MODEL_KWARGS)

    if args.seed is not None:
        user_kwargs["seed"] = args.seed
        assistant_kwargs["seed"] = args.seed

    # Create agent and user model
    agent = create_assistant_agent(
        model_name=args.model,
        system_prompt=ASSISTANT_SYSTEM_PROMPT,
        tools=[search_web],
        **assistant_kwargs,
    )
    user_model_name = args.user_model or args.model
    user_model = create_user_model(user_model_name, **user_kwargs)

    # Create conversation engine
    engine = ConversationEngine(
        agent=agent,
        user_model=user_model,
        assistant_system_prompt=ASSISTANT_SYSTEM_PROMPT,
        clean_system_prompt=CLEAN_ASSISTANT_SYSTEM_PROMPT,
    )

    # Generate conversation
    print(f"\nGenerating conversation for: {device_name}\n")
    result = await engine.generate_conversation(
        device_name=device_name, max_turns_override=args.turns
    )

    if not result:
        print("Failed to generate conversation")
        return

    # Print results
    print_header(
        result["device_name"],
        result["persona"],
    )

    persona_prompt = get_persona_prompt(result["persona"], result["device_name"])
    print("Persona Prompt:")
    print(f"  {persona_prompt[:200]}...")
    print()

    print_conversation(result["messages"], result["persona"]["name"])

    # Count turns
    user_turns = sum(1 for m in result["messages"] if m["role"] == "user")
    assistant_turns = sum(1 for m in result["messages"] if m["role"] == "assistant")
    print_footer(len(result["messages"]), user_turns, assistant_turns)

    # Validate no duplicate consecutive roles
    for i in range(1, len(result["messages"])):
        if result["messages"][i]["role"] == result["messages"][i - 1]["role"]:
            print(
                f"WARNING: Consecutive {result['messages'][i]['role']} messages at index {i}"
            )

    # Write output
    write_output(args.output, result, result["system_prompt"])


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
