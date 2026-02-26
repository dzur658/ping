"""ChatOpenAI subclass that fixes tool_call parsing for llama.cpp servers.

This module provides ChatLlamaCppFixed, a ChatOpenAI subclass that correctly
parses tool_calls from llama.cpp OpenAI-compatible API responses. The standard
ChatOpenAI implementation sometimes drops tool_calls from non-standard
OpenAI-compatible servers like llama.cpp.
"""

import json
import logging
from typing import Any, Dict, List, Optional

from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_openai import ChatOpenAI

logger = logging.getLogger(__name__)


class ChatLlamaCppFixed(ChatOpenAI):
    """ChatOpenAI subclass that correctly parses tool_calls from llama.cpp.

    This class overrides the response parsing in ChatOpenAI to ensure that
    tool_calls from llama.cpp servers are properly extracted and attached to
    the AIMessage.

    The class logs raw API responses at DEBUG level for troubleshooting.
    """

    def _generate(
        self,
        messages: List[Any],
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Generate chat completions with corrected tool_call parsing.

        Args:
            messages: List of messages to send
            stop: Stop sequences
            run_manager: Callback manager
            **kwargs: Additional parameters

        Returns:
            ChatResult with properly populated tool_calls
        """
        result = super()._generate(messages, stop, run_manager, **kwargs)

        if not result.generations:
            return result

        generation = result.generations[0]
        message = generation.message

        if not isinstance(message, AIMessage):
            return result

        llm_output = result.llm_output or {}
        choices = llm_output.get("choices", [])

        if not choices:
            return result

        choice = choices[0]
        message_data = choice.get("message", {})

        if not message_data.get("content"):
            logger.warning(f"Empty content in API response. Full choice: {choice!r}")

        raw_tool_calls = message_data.get("tool_calls", [])

        if not raw_tool_calls:
            return result

        logger.debug(f"Raw tool_calls found in response: {raw_tool_calls}")

        tool_calls = self._parse_tool_calls(raw_tool_calls)

        if tool_calls:
            message_with_tools = AIMessage(
                content=message.content, tool_calls=tool_calls
            )
            fixed_generation = ChatGeneration(
                message=message_with_tools,
                generation_info=generation.generation_info,
            )
            result.generations = [fixed_generation]

            finish_reason = choice.get("finish_reason", "stop")
            if finish_reason == "tool_calls" and generation.generation_info:
                generation.generation_info["finish_reason"] = "tool_calls"

            logger.debug(f"Fixed tool_calls: {len(tool_calls)} calls")
        else:
            logger.debug("No valid tool_calls could be parsed")

        return result

    async def _agenerate(
        self,
        messages: List[Any],
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
        **kwargs: Any,
    ) -> ChatResult:
        """Async generate chat completions with corrected tool_call parsing.

        Args:
            messages: List of messages to send
            stop: Stop sequences
            run_manager: Callback manager
            **kwargs: Additional parameters

        Returns:
            ChatResult with properly populated tool_calls
        """
        result = await super()._agenerate(messages, stop, run_manager, **kwargs)

        if not result.generations:
            return result

        generation = result.generations[0]
        message = generation.message

        if not isinstance(message, AIMessage):
            return result

        llm_output = result.llm_output or {}
        choices = llm_output.get("choices", [])

        if not choices:
            return result

        choice = choices[0]
        message_data = choice.get("message", {})

        if not message_data.get("content"):
            logger.warning(f"Empty content in API response. Full choice: {choice!r}")
            logger.warning(f"Full llm_output: {llm_output!r}")

        raw_tool_calls = message_data.get("tool_calls", [])
        """Async generate chat completions with corrected tool_call parsing.

        Args:
            messages: List of messages to send
            stop: Stop sequences
            run_manager: Callback manager
            **kwargs: Additional parameters

        Returns:
            ChatResult with properly populated tool_calls
        """
        result = await super()._agenerate(messages, stop, run_manager, **kwargs)

        if not result.generations:
            return result

        generation = result.generations[0]
        message = generation.message

        if not isinstance(message, AIMessage):
            return result

        llm_output = result.llm_output or {}
        choices = llm_output.get("choices", [])

        if not choices:
            return result

        choice = choices[0]
        message_data = choice.get("message", {})

        if not message_data.get("content"):
            logger.warning(f"Empty content in API response. Full choice: {choice!r}")

        raw_tool_calls = message_data.get("tool_calls", [])

        if not raw_tool_calls:
            return result

        logger.debug(f"Raw tool_calls found in async response: {raw_tool_calls}")

        tool_calls = self._parse_tool_calls(raw_tool_calls)

        if tool_calls:
            message_with_tools = AIMessage(
                content=message.content, tool_calls=tool_calls
            )
            fixed_generation = ChatGeneration(
                message=message_with_tools,
                generation_info=generation.generation_info,
            )
            result.generations = [fixed_generation]

            finish_reason = choice.get("finish_reason", "stop")
            if finish_reason == "tool_calls" and generation.generation_info:
                generation.generation_info["finish_reason"] = "tool_calls"

            logger.debug(f"Fixed tool_calls: {len(tool_calls)} calls")
        else:
            logger.debug("No valid tool_calls could be parsed")

        return result

    def _parse_tool_calls(
        self, raw_tool_calls: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Parse raw tool_calls from llama.cpp response.

        Args:
            raw_tool_calls: Raw tool_calls from API response

        Returns:
            List of properly formatted tool_call dicts
        """
        tool_calls = []

        for i, raw_call in enumerate(raw_tool_calls):
            if not isinstance(raw_call, dict):
                continue

            call_type = raw_call.get("type", "function")
            if call_type != "function":
                continue

            function_data = raw_call.get("function", {})
            if not isinstance(function_data, dict):
                continue

            name = function_data.get("name", "")
            arguments_str = function_data.get("arguments", "{}")
            call_id = raw_call.get("id", f"call_{i}")

            if not name:
                logger.warning(f"Tool call missing 'name' field: {raw_call}")
                continue

            try:
                args = (
                    json.loads(arguments_str) if isinstance(arguments_str, str) else {}
                )
            except json.JSONDecodeError:
                logger.warning(f"Failed to parse tool args as JSON: {arguments_str}")
                args = {}

            tool_call = {
                "name": name,
                "args": args,
                "id": call_id,
                "type": "tool_call",
            }
            tool_calls.append(tool_call)
            logger.debug(f"Parsed tool call: {name}({call_id})")

        return tool_calls
