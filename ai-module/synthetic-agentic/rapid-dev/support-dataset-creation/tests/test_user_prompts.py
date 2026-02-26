"""Test script to verify user prompt templates are working correctly."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.prompts import (
    USER_PROMPT_CONTINUE,
    USER_PROMPT_CLARIFY,
    USER_PROMPT_DONE,
    USER_PROMPT_TROUBLE,
)


def test_user_prompts():
    """Verify all user prompts have examples and proper formatting."""
    prompts = {
        "USER_PROMPT_CONTINUE": USER_PROMPT_CONTINUE,
        "USER_PROMPT_CLARIFY": USER_PROMPT_CLARIFY,
        "USER_PROMPT_DONE": USER_PROMPT_DONE,
        "USER_PROMPT_TROUBLE": USER_PROMPT_TROUBLE,
    }

    all_passed = True

    for name, prompt in prompts.items():
        print(f"\nTesting {name}...")

        if not prompt or not prompt.strip():
            print(f"  ❌ FAIL: Prompt is empty")
            all_passed = False
            continue

        if "Examples:" not in prompt:
            print(f"  ❌ FAIL: Missing Examples section")
            all_passed = False
        else:
            print(f"  ✓ Has Examples section")

        examples_section = prompt.split("Examples:")[1] if "Examples:" in prompt else ""
        example_count = examples_section.count("\n-") if examples_section else 0

        if example_count < 2:
            print(f"  ⚠ WARNING: Only {example_count} example(s)")
        else:
            print(f"  ✓ Has {example_count} example(s)")

        if "Examples:" in examples_section:
            print(f"  ⚠ WARNING: Nested 'Examples:' keyword")

        if len(prompt) < 100:
            print(f"  ⚠ WARNING: Prompt seems short ({len(prompt)} chars)")

        print(f"  Length: {len(prompt)} chars")

    return all_passed


if __name__ == "__main__":
    print("=" * 60)
    print("Testing User Prompt Templates")
    print("=" * 60)

    if test_user_prompts():
        print("\n" + "=" * 60)
        print("✓ All tests passed")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("❌ Some tests failed")
        print("=" * 60)
        sys.exit(1)
