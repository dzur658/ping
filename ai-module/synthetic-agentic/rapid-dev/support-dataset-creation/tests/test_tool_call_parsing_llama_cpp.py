"""Test script to verify tool_call parsing works with llama.cpp.

This script tests that ChatLlamaCppFixed correctly parses tool_calls from
the llama.cpp OpenAI-compatible API response.

Usage:
    python tests/test_tool_call_parsing.py

To see DEBUG logs (raw responses):
    python -m logging --level=DEBUG tests/test_tool_call_parsing.py
"""

import asyncio
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import (
    LLAMACPP_ASSISTANT_URL,
    LLAMACPP_API_KEY,
    LLAMACPP_ASSISTANT_MODEL,
    BACKEND,
)
from src.llm_llamacpp import ChatLlamaCppFixed


def setup_logging():
    """Configure logging to show DEBUG level messages."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )


async def test_tool_call_parsing_async():
    """Test async tool_call parsing with ChatLlamaCppFixed."""
    print("\n" + "=" * 60)
    print("ASYNC TEST: ChatLlamaCppFixed Tool Call Parsing")
    print("=" * 60)

    if BACKEND != "llamacpp":
        print(f"\nSkipping test: BACKEND is '{BACKEND}', expected 'llamacpp'")
        return False

    print(f"\nConnecting to: {LLAMACPP_ASSISTANT_URL}")
    print(f"Model: {LLAMACPP_ASSISTANT_MODEL}")

    from src.tools.playwright_tool import search_web

    llm = ChatLlamaCppFixed(
        base_url=LLAMACPP_ASSISTANT_URL,
        api_key=LLAMACPP_API_KEY,
        model=LLAMACPP_ASSISTANT_MODEL,
        temperature=1.0,
    )

    llm_with_tool = llm.bind_tools([search_web])

    test_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Search the web for the current weather in San Francisco.",
        },
    ]

    print(f"\nTest messages:")
    for msg in test_messages:
        content_preview = msg.get("content", "")
        if len(content_preview) > 60:
            content_preview = content_preview[:60] + "..."
        print(f"  {msg['role']}: {content_preview}")

    try:
        print("\n--- Calling model (async) ---")
        response = await llm_with_tool.ainvoke(test_messages)

        print("\n--- Response Analysis ---")
        print(f"Content type: {type(response.content)}")
        print(f"Content length: {len(response.content) if response.content else 0}")
        print(f"Content: {response.content if response.content else '<empty>'}")

        print(f"\nTool calls count: {len(response.tool_calls)}")
        print(f"Invalid tool calls count: {len(response.invalid_tool_calls)}")
        print(
            f"Finish reason: {response.response_metadata.get('finish_reason', 'unknown')}"
        )

        print(f"\n--- Tool Calls ---")
        if response.tool_calls:
            for i, tc in enumerate(response.tool_calls):
                print(f"  [{i}] Name: {tc.get('name', 'N/A')}")
                print(f"      ID: {tc.get('id', 'N/A')}")
                print(f"      Type: {tc.get('type', 'N/A')}")
                args = tc.get("args", {})
                args_str = str(args)
                if len(args_str) > 100:
                    print(f"      Args: {args_str[:100]}...")
                else:
                    print(f"      Args: {args_str}")
        else:
            print("  No tool_calls found!")

        if response.invalid_tool_calls:
            print(f"\n--- Invalid Tool Calls ---")
            for i, itc in enumerate(response.invalid_tool_calls):
                print(
                    f"  [{i}] Name: {itc.get('name', 'N/A')}, Error: {itc.get('error', 'N/A')}"
                )

        if response.tool_calls:
            print("\n✓ SUCCESS: Tool calls were correctly parsed!")
            return True
        else:
            print("\n✗ FAILURE: No tool_calls in response")
            return False

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_tool_call_parsing_sync():
    """Test sync tool_call parsing with ChatLlamaCppFixed."""
    print("\n" + "=" * 60)
    print("SYNC TEST: ChatLlamaCppFixed Tool Call Parsing")
    print("=" * 60)

    if BACKEND != "llamacpp":
        print(f"\nSkipping test: BACKEND is '{BACKEND}', expected 'llamacpp'")
        return False

    print(f"\nConnecting to: {LLAMACPP_ASSISTANT_URL}")
    print(f"Model: {LLAMACPP_ASSISTANT_MODEL}")

    from src.tools.playwright_tool import search_web

    llm = ChatLlamaCppFixed(
        base_url=LLAMACPP_ASSISTANT_URL,
        api_key=LLAMACPP_API_KEY,
        model=LLAMACPP_ASSISTANT_MODEL,
        temperature=1.0,
    )

    llm_with_tool = llm.bind_tools([search_web])

    test_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Search the web for the current weather in San Francisco.",
        },
    ]

    print(f"\nTest messages:")
    for msg in test_messages:
        content_preview = msg.get("content", "")
        if len(content_preview) > 60:
            content_preview = content_preview[:60] + "..."
        print(f"  {msg['role']}: {content_preview}")

    try:
        print("\n--- Calling model (sync) ---")
        response = llm_with_tool.invoke(test_messages)

        print("\n--- Response Analysis ---")
        print(f"Content type: {type(response.content)}")
        print(f"Content length: {len(response.content) if response.content else 0}")
        print(f"Content: {response.content if response.content else '<empty>'}")

        print(f"\nTool calls count: {len(response.tool_calls)}")
        print(f"Invalid tool calls count: {len(response.invalid_tool_calls)}")
        print(
            f"Finish reason: {response.response_metadata.get('finish_reason', 'unknown')}"
        )

        print(f"\n--- Tool Calls ---")
        if response.tool_calls:
            for i, tc in enumerate(response.tool_calls):
                print(f"  [{i}] Name: {tc.get('name', 'N/A')}")
                print(f"      ID: {tc.get('id', 'N/A')}")
                print(f"      Type: {tc.get('type', 'N/A')}")
                args = tc.get("args", {})
                args_str = str(args)
                if len(args_str) > 100:
                    print(f"      Args: {args_str[:100]}...")
                else:
                    print(f"      Args: {args_str}")
        else:
            print("  No tool_calls found!")

        if response.invalid_tool_calls:
            print(f"\n--- Invalid Tool Calls ---")
            for i, itc in enumerate(response.invalid_tool_calls):
                print(
                    f"  [{i}] Name: {itc.get('name', 'N/A')}, Error: {itc.get('error', 'N/A')}"
                )

        if response.tool_calls:
            print("\n✓ SUCCESS: Tool calls were correctly parsed!")
            return True
        else:
            print("\n✗ FAILURE: No tool_calls in response")
            return False

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_regular_response():
    """Test that non-tool-call responses still work correctly."""
    print("\n" + "=" * 60)
    print("REGULAR RESPONSE TEST: Non-tool-call responses")
    print("=" * 60)

    if BACKEND != "llamacpp":
        print(f"\nSkipping test: BACKEND is '{BACKEND}', expected 'llamacpp'")
        return False

    from src.tools.playwright_tool import search_web

    llm = ChatLlamaCppFixed(
        base_url=LLAMACPP_ASSISTANT_URL,
        api_key=LLAMACPP_API_KEY,
        model=LLAMACPP_ASSISTANT_MODEL,
        temperature=1.0,
    )

    llm_with_tool = llm.bind_tools([search_web])

    test_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! How are you doing today?"},
    ]

    print(f"\nTest messages:")
    for msg in test_messages:
        content_preview = msg.get("content", "")
        if len(content_preview) > 60:
            content_preview = content_preview[:60] + "..."
        print(f"  {msg['role']}: {content_preview}")

    try:
        print("\n--- Calling model ---")
        response = llm_with_tool.invoke(test_messages)

        print("\n--- Response Analysis ---")
        print(f"Content length: {len(response.content) if response.content else 0}")
        print(f"Tool calls count: {len(response.tool_calls)}")
        print(
            f"Finish reason: {response.response_metadata.get('finish_reason', 'unknown')}"
        )

        if response.content:
            content_str = str(response.content)
            content_preview = content_str
            if len(content_preview) > 200:
                content_preview = content_preview[:200] + "..."
            print(f"\nContent preview: {content_preview}")
            print("\n✓ SUCCESS: Regular response works correctly!")
            return True
        else:
            print("\n✗ FAILURE: Empty content in response")
            return False

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback

        traceback.print_exc()
        return False


async def main():
    """Run all tests."""
    setup_logging()

    print("\n" + "=" * 60)
    print("ChatLlamaCppFixed Tool Call Parsing Tests")
    print("=" * 60)
    print(f"BACKEND: {BACKEND}")
    print(f"API URL: {LLAMACPP_ASSISTANT_URL}")
    print(f"Model: {LLAMACPP_ASSISTANT_MODEL}")
    print("=" * 60)

    results = {}

    results["sync_tool_call"] = test_tool_call_parsing_sync()
    results["async_tool_call"] = await test_tool_call_parsing_async()
    results["regular_response"] = test_regular_response()

    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    for test_name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status}: {test_name}")

    all_passed = all(results.values())
    print("=" * 60)
    if all_passed:
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
