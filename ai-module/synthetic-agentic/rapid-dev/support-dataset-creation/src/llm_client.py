"""LLM client for interacting with Ollama API."""

import asyncio
from typing import List, Dict, Callable, Optional, Mapping

from ollama import AsyncClient, ResponseError

from .config import (
    DEFAULT_OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    MAX_RETRIES,
    RETRY_DELAY,
    MAX_TOOL_CALLS_PER_TURN,
    SamplingConfig,
    USER_SAMPLING,
    ASSISTANT_SAMPLING,
    DEFAULT_SAMPLING,
)


class OllamaClient:
    """Async client for Ollama API using official library."""

    def __init__(
        self, base_url: str = OLLAMA_BASE_URL, model: str = DEFAULT_OLLAMA_MODEL
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.client = AsyncClient(host=self.base_url)

    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        sampling: Optional[SamplingConfig] = None,
    ) -> str:
        """Send chat completion request to Ollama with retry logic."""
        sampling = sampling or DEFAULT_SAMPLING
        for attempt in range(MAX_RETRIES):
            try:
                response = await self.client.chat(
                    model=self.model,
                    messages=messages,
                    options=sampling.to_ollama_options(),
                )
                return response.message.content or ""

            except ResponseError as e:
                if attempt < MAX_RETRIES - 1:
                    print(
                        f"Ollama error: {e.error}, retrying... ({attempt + 1}/{MAX_RETRIES})"
                    )
                    await asyncio.sleep(RETRY_DELAY * (attempt + 1))
                else:
                    raise Exception(
                        f"Ollama API error after {MAX_RETRIES} attempts: {e.error}"
                    )

            except Exception as e:
                if attempt < MAX_RETRIES - 1:
                    print(f"Error: {e}, retrying... ({attempt + 1}/{MAX_RETRIES})")
                    await asyncio.sleep(RETRY_DELAY * (attempt + 1))
                else:
                    raise Exception(f"Ollama connection error: {e}")

        return ""

    async def chat_with_tools(
        self,
        messages: List[Dict[str, str]],
        tools: List[Dict],
        tool_executors: Dict[str, Callable],
        sampling: Optional[SamplingConfig] = None,
        on_tool_call: Optional[Callable[[str, Mapping, str], None]] = None,
    ) -> str:
        """Chat with tool calling support."""
        from .tools.playwright_tool import SEARCH_TOOL_DEFINITION

        sampling = sampling or ASSISTANT_SAMPLING

        if tools and SEARCH_TOOL_DEFINITION not in tools:
            tools = [SEARCH_TOOL_DEFINITION]

        call_count = 0

        working_messages = list(messages)

        try:
            response = await self.client.chat(
                model=self.model,
                messages=working_messages,
                tools=tools if tools else None,
                options=sampling.to_ollama_options(),
            )

            if response.message.tool_calls:
                working_messages.append(
                    {"role": "assistant", "content": response.message.content or ""}
                )

                for tool_call in response.message.tool_calls:
                    if call_count >= MAX_TOOL_CALLS_PER_TURN:
                        print("Max tool calls reached, stopping tool execution")
                        break

                    func_name = tool_call.function.name
                    func_args = tool_call.function.arguments

                    if func_name in tool_executors:
                        try:
                            result = await tool_executors[func_name](**func_args)

                            if on_tool_call:
                                on_tool_call(func_name, func_args, result)

                            working_messages.append(
                                {
                                    "role": "tool",
                                    "content": str(result),
                                    "name": func_name,
                                }
                            )
                            call_count += 1
                        except Exception as e:
                            print(f"Error executing tool {func_name}: {e}")

                            if on_tool_call:
                                on_tool_call(func_name, func_args, f"Error: {e}")

                            working_messages.append(
                                {
                                    "role": "tool",
                                    "content": f"Error: {e}",
                                    "name": func_name,
                                }
                            )
                            call_count += 1

                if call_count > 0:
                    second_response = await self.client.chat(
                        model=self.model,
                        messages=working_messages,
                        options=sampling.to_ollama_options(),
                    )
                    return second_response.message.content or ""
                else:
                    return response.message.content or ""
            else:
                return response.message.content or ""

        except ResponseError as e:
            print(f"Ollama error: {e.error}")
            return ""
        except Exception as e:
            print(f"Unexpected error: {e}")
            return ""

    async def generate_user_response(
        self,
        persona_prompt: str,
        conversation_history: List[Dict[str, str]],
        device_name: str,
        sampling: Optional[SamplingConfig] = None,
    ) -> str:
        """Generate a user response based on persona and conversation history."""
        sampling = sampling or USER_SAMPLING

        messages = [{"role": "system", "content": persona_prompt}]

        messages.extend(conversation_history)

        messages.append(
            {
                "role": "user",
                "content": f"You are asking about your {device_name}. Based on the assistant's response above, ask a natural follow-up question that shows you're trying to understand or implement their advice. Keep your response concise and in character as {persona_prompt.split('You are roleplaying as ')[1].split(',')[0]}.",
            }
        )

        response = await self.chat_completion(messages, sampling=sampling)
        return response.strip()

    async def generate_assistant_response(
        self,
        system_prompt: str,
        conversation_history: List[Dict[str, str]],
        tools: Optional[List[Dict]] = None,
        tool_executors: Optional[Dict[str, Callable]] = None,
        sampling: Optional[SamplingConfig] = None,
        on_tool_call: Optional[Callable[[str, Mapping, str], None]] = None,
    ) -> str:
        """Generate an assistant response with tool calling support."""
        sampling = sampling or ASSISTANT_SAMPLING

        if tools and tool_executors:
            return await self.chat_with_tools(
                messages=conversation_history,
                tools=tools,
                tool_executors=tool_executors,
                sampling=sampling,
                on_tool_call=on_tool_call,
            )
        else:
            messages = [{"role": "system", "content": system_prompt}]
            messages.extend(conversation_history)
            messages.append(
                {
                    "role": "user",
                    "content": "Provide a helpful, patient response to the user's question. If they seem confused, explain in simpler terms. Be encouraging and supportive.",
                }
            )
            response = await self.chat_completion(messages, sampling=sampling)
            return response.strip()
