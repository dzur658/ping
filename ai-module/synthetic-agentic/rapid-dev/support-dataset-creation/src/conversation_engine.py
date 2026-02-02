"""Core conversation engine for generating synthetic support conversations."""

import asyncio
import random
from typing import List, Dict, Optional, Callable, Mapping

from .config import (
    MAX_TURNS,
    MIN_TURNS,
    SamplingConfig,
    USER_SAMPLING,
    ASSISTANT_SAMPLING,
)
from .data_utils import (
    get_knowledge_base_doc,
    get_random_turn_length,
    validate_conversation,
)
from .personas import get_random_persona, get_persona_prompt
from .llm_client import OllamaClient
from .tools.playwright_tool import search_and_parse_web, SEARCH_TOOL_DEFINITION
from .prompts import ASSISTANT_SYSTEM_PROMPT
from .config import MAX_TOOL_CALLS_PER_TURN


class ConversationEngine:
    """Engine for generating synthetic support conversations."""

    def __init__(
        self,
        ollama_client: OllamaClient,
        assistant_system_prompt: str = ASSISTANT_SYSTEM_PROMPT,
        user_sampling: Optional[SamplingConfig] = None,
        assistant_sampling: Optional[SamplingConfig] = None,
        on_tool_call: Optional[Callable[[str, Mapping, str], None]] = None,
    ):
        self.client = ollama_client
        self.assistant_system_prompt = assistant_system_prompt
        self.user_sampling = user_sampling or USER_SAMPLING
        self.assistant_sampling = assistant_sampling or ASSISTANT_SAMPLING
        self.on_tool_call = on_tool_call

    async def generate_conversation(
        self,
        device_name: str,
        max_turns_override: Optional[int] = None,
    ) -> Optional[Dict]:
        """Generate a complete conversation for a device."""
        knowledge_doc = get_knowledge_base_doc(device_name)
        if not knowledge_doc:
            print(f"Warning: No knowledge base entry for {device_name}")
            return None

        persona = get_random_persona()
        persona_prompt = get_persona_prompt(persona, device_name)
        target_turns = max_turns_override or get_random_turn_length()

        messages = []

        # intro user message to preserve chat format
        messages.append(
            {
                "role": "user",
                "content": f"[System Command]: Load reference for {device_name}.",
            }
        )

        # Begin as if the assistant has provided an initial response
        messages.append({"role": "assistant", "content": knowledge_doc})

        for turn in range(target_turns):
            user_response = await self.client.generate_user_response(
                persona_prompt=persona_prompt,
                conversation_history=messages,
                device_name=device_name,
                sampling=self.user_sampling,
            )

            if not user_response:
                print(
                    f"Failed to generate user response for {device_name}, turn {turn}"
                )
                break

            messages.append({"role": "user", "content": user_response})

            assistant_response = await self.client.generate_assistant_response(
                system_prompt=self.assistant_system_prompt,
                conversation_history=messages,
                tools=[SEARCH_TOOL_DEFINITION],
                tool_executors={"search_web": search_and_parse_web},
                sampling=self.assistant_sampling,
                on_tool_call=self.on_tool_call,
            )

            if not assistant_response:
                print(
                    f"Failed to generate assistant response for {device_name}, turn {turn}"
                )
                break

            messages.append({"role": "assistant", "content": assistant_response})

            if turn >= MIN_TURNS and self._is_conversation_complete(user_response):
                break

        if validate_conversation(messages):
            return {
                "device_name": device_name,
                "persona": persona["name"],
                "messages": messages,
            }
        else:
            print(f"Conversation validation failed for {device_name}")
            return None

    def _is_conversation_complete(self, user_response: str) -> bool:
        """Determine if conversation seems complete based on user response."""
        complete_indicators = [
            "thank you",
            "thanks",
            "got it",
            "understood",
            "perfect",
            "that makes sense",
            "i'll try that",
            "ok thanks",
            "thanks for your help",
        ]

        user_lower = user_response.lower()
        return any(indicator in user_lower for indicator in complete_indicators)


async def generate_conversations_batch(
    engine: ConversationEngine,
    devices: List[str],
    num_per_device: int,
    max_turns: Optional[int] = None,
    max_concurrent: int = 4,
) -> List[Dict]:
    """Generate multiple conversations in parallel batches."""
    all_conversations = []
    semaphore = asyncio.Semaphore(max_concurrent)

    async def generate_single(device: str) -> Optional[Dict]:
        async with semaphore:
            await asyncio.sleep(random.uniform(0.1, 0.5))
            return await engine.generate_conversation(device, max_turns)

    tasks = []
    for device in devices:
        for _ in range(num_per_device):
            tasks.append(generate_single(device))

    from tqdm import tqdm

    results = []
    for future in tqdm(
        asyncio.as_completed(tasks),
        total=len(tasks),
        desc="Generating conversations",
    ):
        result = await future
        if result:
            results.append(result)

    return results
