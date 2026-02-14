"""Core conversation engine for generating synthetic support conversations."""

import asyncio
import logging
import random
from typing import List, Dict, Optional

from .config import (
    MAX_TURNS,
    MIN_TURNS,
    MAX_RETRIES,
    RETRY_DELAY,
    LOG_FILE,
)


logger = logging.getLogger(__name__)


def setup_logging():
    """Configure logging to file and console."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


from .data_utils import (
    get_knowledge_base_doc,
    get_random_turn_length,
    sanitize_user_bot_message,
    validate_conversation,
)
from .personas import get_random_persona, get_persona_prompt
from .llm_client import create_assistant_agent, generate_user_response

# from .tools.playwright_tool import search_web
from .prompts import ASSISTANT_SYSTEM_PROMPT
from .models import ReasoningResponse


class ConversationEngine:
    """Engine for generating synthetic support conversations."""

    def __init__(
        self,
        agent,
        user_model,
        assistant_system_prompt: str = ASSISTANT_SYSTEM_PROMPT,
        clean_system_prompt: Optional[str] = None,
    ):
        self.agent = agent
        self.user_model = user_model
        self.assistant_system_prompt = assistant_system_prompt
        self.clean_system_prompt = clean_system_prompt or assistant_system_prompt

    async def generate_conversation(
        self,
        device_name: str,
        max_turns_override: Optional[int] = None,
    ) -> Optional[Dict]:
        """Generate a complete conversation for a device."""
        knowledge_doc = get_knowledge_base_doc(device_name)
        if not knowledge_doc:
            logger.warning(f"No knowledge base entry for {device_name}")
            return None

        persona = get_random_persona()
        persona_prompt = get_persona_prompt(persona, device_name)
        target_turns = max_turns_override or get_random_turn_length()

        messages = []
        context_messages = []

        # intro user message to preserve chat format
        messages.append(
            {
                "role": "user",
                "content": f"[System Command]: Load reference for {device_name}.",
            }
        )
        context_messages.append(messages[-1])

        # Begin as if the assistant has provided an initial response
        messages.append(
            {
                "role": "assistant",
                "content": f"<think>\nLet me review what I know about this device to help the user.\n</think>\n\n{knowledge_doc}",
            }
        )
        context_messages.append(messages[-1])

        for turn in range(target_turns):
            user_response = await generate_user_response(
                user_model=self.user_model,
                persona_prompt=persona_prompt,
                conversation_history=context_messages,
                device_name=device_name,
            )

            if not user_response:
                logger.warning(
                    f"Failed to generate user response for {device_name}, turn {turn}"
                )
                break

            sanitized_user_response = sanitize_user_bot_message(user_response)
            if not sanitized_user_response:
                logger.warning(
                    f"Failed to sanitize user response for {device_name}, turn {turn}"
                )
                break

            messages.append({"role": "user", "content": sanitized_user_response})
            context_messages.append(
                {"role": "user", "content": sanitized_user_response}
            )

            structured_response = None
            last_error = None

            for attempt in range(MAX_RETRIES + 1):
                try:
                    result = await self.agent.ainvoke({"messages": context_messages})
                    messages_list = result.get("messages", [])
                    if not messages_list:
                        raise ValueError("No messages in agent result")

                    last_ai_message = messages_list[-1]
                    if (
                        not hasattr(last_ai_message, "content")
                        or not last_ai_message.content
                    ):
                        raise ValueError("No content in last AI message")

                    structured_response = ReasoningResponse.model_validate_json(
                        last_ai_message.content
                    )
                    break
                except Exception as e:
                    last_error = e
                    if attempt < MAX_RETRIES:
                        logger.warning(
                            f"Attempt {attempt + 1} failed for {device_name}, turn {turn}: {e}. "
                            f"Retrying in {RETRY_DELAY}s..."
                        )
                        await asyncio.sleep(RETRY_DELAY)
                    else:
                        logger.error(
                            f"All {MAX_RETRIES + 1} attempts failed for {device_name}, "
                            f"turn {turn}: {e}"
                        )

            if structured_response is None:
                break

            training_content = structured_response.to_training_format()
            messages.append({"role": "assistant", "content": training_content})
            context_messages.append(
                {"role": "assistant", "content": structured_response.response}
            )

            if turn >= MIN_TURNS and self._is_conversation_complete(
                sanitized_user_response
            ):
                break
            elif turn >= (MAX_TURNS // 2) - 1:
                # break we'll just assume the user doesn't have anything more to say which makes sense
                # considering how users use llms
                break

        if validate_conversation(messages):
            return {
                "device_name": device_name,
                "persona": persona,
                "messages": messages,
                "system_prompt": self.clean_system_prompt,
            }
        else:
            logger.warning(f"Conversation validation failed for {device_name}")
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
    import asyncio

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
