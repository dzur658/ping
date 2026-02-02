#!/usr/bin/env python3
"""Main entry point for synthetic conversation generation."""

import argparse
import asyncio
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))

from src.config import (
    DEFAULT_CONVERSATIONS_PER_DEVICE,
    DEFAULT_OUTPUT_FILE,
    DEFAULT_WORKERS,
    DEFAULT_OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    SamplingConfig,
    USER_SAMPLING,
    ASSISTANT_SAMPLING,
)
from src.data_utils import (
    load_consumer_devices,
    write_conversation_jsonl,
)
from src.llm_client import OllamaClient
from src.conversation_engine import ConversationEngine, generate_conversations_batch
from src.prompts import ASSISTANT_SYSTEM_PROMPT


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate synthetic support conversations for LoRA fine-tuning."
    )

    parser.add_argument(
        "--device",
        type=str,
        help="Specific device to generate conversations for (e.g., 'iPhone 14')",
    )

    parser.add_argument(
        "--filter",
        type=str,
        help="Filter devices by pattern (e.g., 'iPhone', 'Ring', 'Nest')",
    )

    parser.add_argument(
        "--num-per-device",
        type=int,
        default=DEFAULT_CONVERSATIONS_PER_DEVICE,
        help="Number of conversations to generate per device",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_FILE,
        help="Output file path (JSONL format)",
    )

    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_OLLAMA_MODEL,
        help="Ollama model to use",
    )

    parser.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help="Number of concurrent conversation generators",
    )

    parser.add_argument(
        "--system-prompt",
        type=str,
        default=ASSISTANT_SYSTEM_PROMPT,
        help="Custom system prompt for the assistant model",
    )

    parser.add_argument(
        "--max-turns",
        type=int,
        help="Override maximum number of turns per conversation",
    )

    parser.add_argument(
        "--ollama-url",
        type=str,
        default=OLLAMA_BASE_URL,
        help="Ollama API base URL",
    )

    # Sampling parameter overrides
    parser.add_argument(
        "--temperature",
        type=float,
        help="Override temperature for both user and assistant models",
    )
    parser.add_argument(
        "--user-temperature",
        type=float,
        help="Override user model temperature",
    )
    parser.add_argument(
        "--assistant-temperature",
        type=float,
        help="Override assistant model temperature",
    )
    parser.add_argument(
        "--user-max-tokens",
        type=int,
        help="Override user model max tokens",
    )
    parser.add_argument(
        "--assistant-max-tokens",
        type=int,
        help="Override assistant model max tokens",
    )
    parser.add_argument(
        "--num-ctx",
        type=int,
        help="Override context window size for both models",
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducibility",
    )

    return parser.parse_args()


async def main():
    """Main execution function."""
    args = parse_args()

    print(f"🤖 Starting synthetic conversation generation")
    print(f"   Model: {args.model}")
    print(f"   Workers: {args.workers}")
    print(f"   Output: {args.output}")

    from dataclasses import replace

    # Build sampling configs with CLI overrides
    user_sampling = USER_SAMPLING
    assistant_sampling = ASSISTANT_SAMPLING

    # Apply shared overrides
    if args.temperature is not None:
        user_sampling = replace(user_sampling, temperature=args.temperature)
        assistant_sampling = replace(assistant_sampling, temperature=args.temperature)
    if args.num_ctx is not None:
        user_sampling = replace(user_sampling, num_ctx=args.num_ctx)
        assistant_sampling = replace(assistant_sampling, num_ctx=args.num_ctx)
    if args.seed is not None:
        user_sampling = replace(user_sampling, seed=args.seed)
        assistant_sampling = replace(assistant_sampling, seed=args.seed)

    # Apply model-specific overrides (these take precedence)
    if args.user_temperature is not None:
        user_sampling = replace(user_sampling, temperature=args.user_temperature)
    if args.assistant_temperature is not None:
        assistant_sampling = replace(
            assistant_sampling, temperature=args.assistant_temperature
        )
    if args.user_max_tokens is not None:
        user_sampling = replace(user_sampling, max_tokens=args.user_max_tokens)
    if args.assistant_max_tokens is not None:
        assistant_sampling = replace(
            assistant_sampling, max_tokens=args.assistant_max_tokens
        )

    print(
        f"   User temp: {user_sampling.temperature}, max_tokens: {user_sampling.max_tokens}"
    )
    print(
        f"   Assistant temp: {assistant_sampling.temperature}, max_tokens: {assistant_sampling.max_tokens}"
    )
    print(f"   Context window: {user_sampling.num_ctx}")
    if user_sampling.seed is not None:
        print(f"   Seed: {user_sampling.seed}")
    print()

    if args.device:
        devices = [args.device]
        print(f"📱 Generating for single device: {args.device}")
    else:
        devices = load_consumer_devices(args.filter)
        print(f"📱 Found {len(devices)} devices to process")

    if not devices:
        print("❌ No devices found matching the criteria")
        sys.exit(1)

    print(f"🔄 Generating {args.num_per_device} conversation(s) per device")
    print(f"⏳ This may take a while...\n")

    client = OllamaClient(base_url=args.ollama_url, model=args.model)
    engine = ConversationEngine(
        ollama_client=client,
        assistant_system_prompt=args.system_prompt,
        user_sampling=user_sampling,
        assistant_sampling=assistant_sampling,
    )

    conversations = await generate_conversations_batch(
        engine=engine,
        devices=devices,
        num_per_device=args.num_per_device,
        max_turns=args.max_turns,
        max_concurrent=args.workers,
    )

    print(f"\n✅ Successfully generated {len(conversations)} conversations")

    write_conversation_jsonl(args.output, conversations, args.system_prompt)

    print(f"💾 Saved to: {args.output}")
    print(f"📊 Statistics:")
    print(f"   - Total conversations: {len(conversations)}")
    print(f"   - Devices covered: {len(set(c['device_name'] for c in conversations))}")
    print(f"   - Personas used: {len(set(c['persona'] for c in conversations))}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
