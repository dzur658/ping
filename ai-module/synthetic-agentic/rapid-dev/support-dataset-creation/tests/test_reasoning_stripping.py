#!/usr/bin/env python3
"""Test reasoning tag handling without web search dependencies."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.models import validate_and_extract, strip_reasoning_tags, swap_reasoning_for_think
from src.prompts import ASSISTANT_SYSTEM_PROMPT, CLEAN_ASSISTANT_SYSTEM_PROMPT


def test_reasoning_validation():
    """Test that reasoning tags are properly validated and extracted."""
    print("=" * 60)
    print("TEST: Reasoning Tag Validation")
    print("=" * 60)

    test_input = """<reasoning>
The user is asking about their Ring doorbell. I need to check the documentation for firmware update instructions.
The knowledge base mentions the update process via the Ring app.
I should explain this step-by-step in simple terms.
</reasoning>

To update your Ring doorbell firmware, here's what you need to do:

1. Make sure your doorbell is connected to Wi-Fi and has at least 50% battery.
2. Open the Ring app on your phone.
3. Tap the menu icon (three lines) in the top left.
4. Select your Ring device.
5. Tap "Device Health" then check for updates.
6. If an update is available, follow the on-screen prompts.

The update usually takes 5-10 minutes and your doorbell may restart automatically."""

    parsed, cleaned = validate_and_extract(test_input)

    print(f"✓ Validation passed: {parsed is not None}")
    print(f"✓ Reasoning extracted: {len(parsed.reasoning) if parsed else 0} chars")
    print(f"✓ Response extracted: {len(parsed.response) if parsed else 0} chars")
    print(f"✓ Cleaned content: {len(cleaned)} chars")
    print()

    assert parsed is not None, "Validation should succeed with proper <reasoning> tags"
    assert "Ring doorbell" in parsed.response, "Response should contain user-facing content"
    assert "Ring doorbell" not in cleaned, "Cleaned content should not have reasoning"
    assert len(cleaned) < len(test_input), "Cleaned should be shorter than original"

    print("✓ All assertions passed!")
    print()


def test_swap_reasoning_for_think():
    """Test that <reasoning> tags are swapped for </think> tags."""
    print("=" * 60)
    print("TEST: Swap <reasoning> -> </think>
    print("=" * 60)

    test_input = """<reasoning>
This is my internal reasoning.
</reasoning>

Here is the actual response."""

    result = swap_reasoning_for_think(test_input)

    print(f"✓ Swap completed")
    print(f"✓ Result contains <think> tags: {'' in result}")
    print(f"✓ Result preserves reasoning: {'internal reasoning' in result}")
    print()

    assert "<think>" in result, "Result should contain opening <think> tag"
    assert "</think>" in result, "Result should contain closing </think> tag"
    assert "internal reasoning" in result, "Reasoning content should be preserved"
    assert "<reasoning>" not in result, "Original <reasoning> tag should be replaced"

    print("✓ All assertions passed!")
    print()


def test_system_prompts():
    """Test that system prompts are properly configured."""
    print("=" * 60)
    print("TEST: System Prompt Configuration")
    print("=" * 60)

    print(f"✓ ASSISTANT_SYSTEM_PROMPT contains <reasoning> instruction: {'<reasoning>' in ASSISTANT_SYSTEM_PROMPT}")
    print(f"✓ ASSISTANT_SYSTEM_PROMPT contains web search instruction: {'web search' in ASSISTANT_SYSTEM_PROMPT.lower()}")
    print()
    print(f"✓ CLEAN_ASSISTANT_SYSTEM_PROMPT excludes <reasoning>: {'<reasoning>' not in CLEAN_ASSISTANT_SYSTEM_PROMPT}")
    print(f"✓ CLEAN_ASSISTANT_SYSTEM_PROMPT excludes web search: {'web search' not in CLEAN_ASSISTANT_SYSTEM_PROMPT.lower()}")
    print()

    assert "<reasoning>" in ASSISTANT_SYSTEM_PROMPT, "Generation prompt should require <reasoning> tags"
    assert "web search" in ASSISTANT_SYSTEM_PROMPT.lower(), "Generation prompt should include web search instructions"
    assert "<reasoning>" not in CLEAN_ASSISTANT_SYSTEM_PROMPT, "Training prompt should not mention <reasoning>"
    assert "web search" not in CLEAN_ASSISTANT_SYSTEM_PROMPT.lower(), "Training prompt should not mention web search"

    print("✓ All assertions passed!")
    print()


def test_no_reasoning_fallback():
    """Test that content without reasoning tags is handled gracefully."""
    print("=" * 60)
    print("TEST: No Reasoning Tags (Fallback)")
    print("=" * 60)

    test_input = """Here is a response without any reasoning tags.
It should be returned unchanged from validate_and_extract."""

    parsed, cleaned = validate_and_extract(test_input)

    print(f"✓ Validation result: {parsed}")
    print(f"✓ Cleaned content length: {len(cleaned)}")
    print()

    assert parsed is None, "Validation should return None when no <reasoning> tags present"
    assert cleaned == test_input, "Cleaned content should match original when no tags present"

    print("✓ All assertions passed!")
    print()


def main():
    """Run all tests."""
    print()
    print("🧪 Testing Reasoning Tag Architecture")
    print()

    try:
        test_reasoning_validation()
        test_swap_reasoning_for_think()
        test_system_prompts()
        test_no_reasoning_fallback()

        print("=" * 60)
        print("✅ ALL TESTS PASSED")
        print("=" * 60)
        print()
        print("Architecture Summary:")
        print("- Model generates <reasoning> blocks per system prompt instructions")
        print("- Pydantic validates <reasoning> tags are present and non-empty")
        print("- Cleaned content (no <reasoning>) used for conversation context")
        print("- Full content (with <reasoning>) stored in training data")
        print("- At JSONL write time: <reasoning> → </think>
        print("- Clean system prompt (no tools/reasoning) used in training data")
        print()
        return 0
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
