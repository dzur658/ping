#!/usr/bin/env python3
"""Test script to generate and display a single training example.

Usage:
    python tests/test_single_conversation.py
    python tests/test_single_conversation.py --device "iPhone 14"
    python tests/test_single_conversation.py --turns 5
    python tests/test_single_conversation.py --seed 123
"""

import argparse
import asyncio
import json
import random
import sys
from pathlib import Path
from typing import Mapping

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import (
    DEFAULT_OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    USER_SAMPLING,
    ASSISTANT_SAMPLING,
)
from src.llm_client import OllamaClient
from src.conversation_engine import ConversationEngine
from src.data_utils import get_knowledge_base_doc, load_consumer_devices
from src.prompts import ASSISTANT_SYSTEM_PROMPT


DEFAULT_OUTPUT = Path(__file__).parent / "output" / "test_conversation.jsonl"
DEFAULT_SEED = 38
DEFAULT_TURNS = 3


def print_tool_call(func_name: str, args: Mapping, result: str):
    """Print tool call details to console."""
    print()
    print("-" * 60)
    print(f"[TOOL CALL] {func_name}")
    print(f"[ARGUMENTS] {json.dumps(args, indent=2)}")
    result_preview = result[:500] + "\n... (truncated)" if len(result) > 500 else result
    print(f"[RESULT] ({len(result)} chars)")
    print(result_preview)
    print("-" * 60)
    print()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a single training example for inspection."
    )
    parser.add_argument("--device", type=str, help="Specific device name")
    parser.add_argument(
        "--turns", type=int, default=DEFAULT_TURNS, help="Number of turns"
    )
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED, help="Random seed")
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT, help="Output file"
    )
    parser.add_argument("--model", type=str, default=DEFAULT_OLLAMA_MODEL)
    parser.add_argument("--ollama-url", type=str, default=OLLAMA_BASE_URL)
    return parser.parse_args()


def get_random_device_with_docs() -> str:
    """Get a random device that has knowledge base documentation."""
    devices = load_consumer_devices()
    random.shuffle(devices)
    for device in devices:
        if get_knowledge_base_doc(device):
            return device
    raise ValueError("No devices with documentation found")


def print_header(device: str, persona_name: str, turns: int, seed: int, output: Path):
    """Print header section."""
    print("=" * 60)
    print("TRAINING EXAMPLE PREVIEW")
    print("=" * 60)
    print(f"Device: {device}")
    print(f"Persona: {persona_name}")
    print(f"Turns: {turns}")
    print(f"Seed: {seed}")
    print(f"Output: {output}")
    print("=" * 60)
    print()


def print_conversation(messages: list, system_prompt: str):
    """Pretty print conversation messages."""
    print("[SYSTEM]")
    if len(system_prompt) > 200:
        print(system_prompt[:200] + "...")
    else:
        print(system_prompt)
    print()

    turn = 0
    i = 0
    while i < len(messages):
        print("-" * 60)
        if turn == 0:
            print(f"TURN {turn} (Initial)")
        else:
            print(f"TURN {turn}")
        print("-" * 60)
        print()

        if i < len(messages) and messages[i]["role"] == "user":
            print("[USER]")
            content = messages[i]["content"]
            if len(content) > 500:
                print(content[:500] + "\n... (truncated, see output file)")
            else:
                print(content)
            print()
            i += 1

        if i < len(messages) and messages[i]["role"] == "assistant":
            print("[ASSISTANT]")
            content = messages[i]["content"]
            if len(content) > 500:
                print(content[:500] + "\n... (truncated, see output file)")
            else:
                print(content)
            print()
            i += 1

        turn += 1


def write_output(output_path: Path, messages: list, system_prompt: str) -> int:
    """Write JSONL output and return file size."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    full_messages = [{"role": "system", "content": system_prompt}]
    full_messages.extend(messages)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(json.dumps({"messages": full_messages}, ensure_ascii=False) + "\n")

    return output_path.stat().st_size


def print_footer(output_path: Path, file_size: int, message_count: int):
    """Print footer section."""
    print("=" * 60)
    print("OUTPUT WRITTEN")
    print("=" * 60)
    print(f"File: {output_path}")
    print(f"Size: {file_size / 1024:.1f} KB")
    print(f"Messages: {message_count}")
    print()
    print("To view full output:")
    print(f"  cat {output_path} | jq .")
    print("=" * 60)


async def main():
    args = parse_args()

    random.seed(args.seed)

    if args.device:
        device = args.device
        if not get_knowledge_base_doc(device):
            print(f"Error: No knowledge base entry for '{device}'")
            sys.exit(1)
    else:
        device = get_random_device_with_docs()

    print("Generating conversation...")
    print()

    client = OllamaClient(base_url=args.ollama_url, model=args.model)
    engine = ConversationEngine(
        ollama_client=client,
        assistant_system_prompt=ASSISTANT_SYSTEM_PROMPT,
        user_sampling=USER_SAMPLING,
        assistant_sampling=ASSISTANT_SAMPLING,
        on_tool_call=print_tool_call,
    )

    result = await engine.generate_conversation(
        device_name=device,
        max_turns_override=args.turns,
    )

    if not result:
        print("Error: Failed to generate conversation")
        sys.exit(1)

    print_header(device, result["persona"], args.turns, args.seed, args.output)
    print_conversation(result["messages"], ASSISTANT_SYSTEM_PROMPT)

    file_size = write_output(args.output, result["messages"], ASSISTANT_SYSTEM_PROMPT)

    print_footer(args.output, file_size, len(result["messages"]) + 1)


if __name__ == "__main__":
    asyncio.run(main())
