"""Core conversation engine for generating synthetic support conversations."""

import asyncio
import logging
import random
from typing import List, Dict, Optional

from langchain_core.messages import AIMessage, BaseMessage

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
from .llm_client import (
    create_assistant_agent,
    generate_user_response,
    generate_judge_feedback,
)

# from .tools.playwright_tool import search_web
from .prompts import ASSISTANT_SYSTEM_PROMPT
from .models import ReasoningResponse


def _parse_fallback_response(content: str) -> Optional[ReasoningResponse]:
    """Parse reasoning and response from content when structured_output fails.

    Args:
        content: The AIMessage content string

    Returns:
        ReasoningResponse if content has valid structure
    """
    if not content or not content.strip():
        return None

    content_stripped = content.strip()

    # Try to find <reasoning>...</reasoning> tags first
    reasoning_open = "<reasoning>"
    reasoning_close = "</reasoning>"
    think_open = "</think>"
    think_close = "</think>"

    # Check for <reasoning> tags
    if reasoning_open.lower() in content_stripped.lower():
        try:
            # Use case-insensitive regex to find the tags
            import re

            pattern = r"<\s*reasoning\s*>(.*?)<\s*/\s*reasoning\s*>"
            match = re.search(pattern, content_stripped, re.DOTALL | re.IGNORECASE)
            if match:
                reasoning = match.group(1).strip()
                # Get response after the closing tag
                response = content_stripped[match.end() :].strip()

                if reasoning and response:
                    return ReasoningResponse(reasoning=reasoning, response=response)
        except Exception:
            pass

    # Fallback to think tags
    if think_open in content_stripped:
        try:
            parts = content_stripped.split(think_open, 1)
            before_think = parts[0]
            after_think = parts[1] if len(parts) > 1 else ""

            if think_close in after_think:
                think_parts = after_think.split(think_close, 1)
                reasoning = think_parts[0].strip()
                response = think_parts[1].strip() if len(think_parts) > 1 else ""
            else:
                reasoning = after_think.strip()
                response = before_think.strip()

            if reasoning and response:
                return ReasoningResponse(reasoning=reasoning, response=response)
        except Exception:
            pass

    return None


class ConversationEngine:
    """Engine for generating synthetic support conversations."""

    def __init__(
        self,
        agent,
        user_model,
        assistant_system_prompt: str = ASSISTANT_SYSTEM_PROMPT,
        clean_system_prompt: Optional[str] = None,
        judge_model=None,
    ):
        self.agent = agent
        self.user_model = user_model
        self.judge_model = judge_model
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
                "content": f"<reasoning>\nTrigger: System Command received (\"Load reference for {device_name}\").\nAction: Retrieve \"{device_name} Update Guide\" from database.\nPlan: Output the full update instructions so the user has the context available immediately.\n</reasoning>\n\n{knowledge_doc}",
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
                {"role": "user", "content": f"{sanitized_user_response} [SYSTEM INSTRUCTION: You are generating a training dataset. The <reasoning> tags MUST be visible in the final string. Do not use your internal hidden thought process. Print the tags explicitly.]"}
            )

            structured_response = None
            last_error = None

            for attempt in range(MAX_RETRIES + 1):
                result = None
                failure_reason = ""
                has_feedback = False
                try:
                    result = await self.agent.ainvoke({"messages": context_messages})

                    if not result:
                        raise ValueError("Agent returned None result")

                    messages_list = result.get("messages", [])
                    if not messages_list:
                        raise ValueError("No messages in agent result")

                    last_ai_message = messages_list[-1]
                    content = last_ai_message.content

                    if not content:
                        raise ValueError("No content in last AI message")

                    content_str = (
                        str(content) if not isinstance(content, str) else content
                    )
                    # print(f"Content for {device_name}, turn {turn}: {content_str}")

                    structured_response = result.get("structured_response")
                    if structured_response is None:
                        structured_response = _parse_fallback_response(content_str)

                    if structured_response is None:
                        raise ValueError(
                            "Failed to extract structured response from agent output, are <reasoning></reasoning> tags included and properly formatted in the response?"
                        )

                    logger.debug(
                        f"Agent result keys for {device_name}, turn {turn}: {list(result.keys())}"
                    )
                    logger.debug(
                        f"Agent result for {device_name}, turn {turn}: {result}"
                    )

                    messages_list = result.get("messages", [])
                    if not messages_list:
                        raise ValueError("No messages in agent result")

                    last_ai_message = messages_list[-1]

                    logger.debug(
                        f"Raw AI message for {device_name}, turn {turn}: "
                        f"content={last_ai_message.content!r}, "
                        f"tool_calls={last_ai_message.tool_calls}, "
                        f"additional_kwargs={last_ai_message.additional_kwargs}, "
                        f"response_metadata={last_ai_message.response_metadata}"
                    )

                    if isinstance(last_ai_message, AIMessage):
                        structured_response = result.get("structured_response")

                        if structured_response is None:
                            content = last_ai_message.content
                            if isinstance(content, (list, dict)):
                                content_str = str(content)
                            else:
                                content_str = content or ""

                            fallback = _parse_fallback_response(content_str)
                            if fallback:
                                logger.debug(
                                    f"Using fallback parsing for {device_name}, turn {turn}"
                                )
                                structured_response = fallback
                            else:
                                raise ValueError(
                                    "No structured_response in agent result"
                                )

                    if not isinstance(structured_response, ReasoningResponse):
                        raise ValueError(
                            f"Unexpected response type: {type(structured_response)}"
                        )

                    reasoning_length = len(structured_response.reasoning)
                    response_length = len(structured_response.response)

                    # check that reasoning is at least half the length of the response to ensure substantive reasoning
                    if reasoning_length <= (response_length / 2):
                        failure_reason = (
                            f"Reasoning length ({reasoning_length}) must be greater "
                            f"than response length ({response_length}). "
                            "The reasoning should be more detailed than the final response."
                        )
                        raise ValueError(failure_reason)

                    break
                except Exception as e:
                    last_error = e
                    failure_reason = str(e)

                    if attempt < MAX_RETRIES:
                        messages_list = result.get("messages", []) if result else []
                        diagnostic_info = ""
                        if messages_list and isinstance(messages_list[-1], AIMessage):
                            msg = messages_list[-1]
                            token_usage = msg.response_metadata.get("token_usage", {})
                            finish_reason = msg.response_metadata.get(
                                "finish_reason", "unknown"
                            )
                            diagnostic_info = (
                                f" | Content len: {len(msg.content or '')} "
                                f"| Tool calls: {len(msg.tool_calls)} "
                                f"| Tokens: {token_usage.get('total_tokens', '?')} "
                                f"| Finish: {finish_reason}"
                            )

                        logger.warning(
                            f"Attempt {attempt + 1} failed for {device_name}, turn {turn}: {e}."
                            f"{diagnostic_info}"
                        )

                        if (
                            context_messages
                            and context_messages[-1].get("role") == "assistant"
                        ):
                            context_messages.pop()

                        if self.judge_model and not has_feedback:
                            last_user_msg = None
                            for msg in reversed(context_messages):
                                if msg.get("role") == "user":
                                    last_user_msg = msg
                                    break

                            if last_user_msg:
                                last_user_content = last_user_msg.get("content", "")
                                assistant_content = ""
                                if result and "messages" in result:
                                    last_assistant = None
                                    for msg in reversed(result["messages"]):
                                        if isinstance(msg, AIMessage):
                                            last_assistant = msg
                                            break
                                    if last_assistant:
                                        content = last_assistant.content or ""
                                        if isinstance(content, list):
                                            assistant_content = str(content)
                                        else:
                                            assistant_content = content
                                feedback = await generate_judge_feedback(
                                    judge_model=self.judge_model,
                                    user_message=last_user_content,
                                    assistant_response=assistant_content,
                                    conversation_context=context_messages[:-2],
                                    failure_reason=failure_reason,
                                )

                                if feedback:
                                    updated_content = (
                                        f"[Feedback]: {feedback}\n\n{last_user_content}"
                                    )
                                    # print(f"Adding feedback for {device_name}, turn {turn}: {feedback}...")
                                    last_user_msg["content"] = updated_content
                                    has_feedback = True
                                    logger.info(
                                        f"Feedback added for {device_name}, turn {turn}: {feedback[:200]}..."
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
    user_model,
    devices: List[str],
    num_per_device: int,
    max_turns: Optional[int] = None,
    max_concurrent: int = 4,
    model_name: str = "llama3.2",
    system_prompt: str = "",
    clean_system_prompt: Optional[str] = None,
    assistant_kwargs: Optional[Dict] = None,
    judge_model=None,
) -> List[Dict]:
    """Generate multiple conversations in parallel batches."""
    import asyncio
    from .llm_client import create_assistant_agent
    from .tools.playwright_tool import SearchWebLimited

    if assistant_kwargs is None:
        assistant_kwargs = {}

    all_conversations = []
    semaphore = asyncio.Semaphore(max_concurrent)

    async def generate_single(device: str) -> Optional[Dict]:
        async with semaphore:
            await asyncio.sleep(random.uniform(0.1, 0.5))

            search_tool = SearchWebLimited(max_calls=1)

            agent = create_assistant_agent(
                model_name=model_name,
                system_prompt=system_prompt,
                tools=[search_tool],
                **assistant_kwargs,
            )

            engine = ConversationEngine(
                agent=agent,
                user_model=user_model,
                assistant_system_prompt=system_prompt,
                clean_system_prompt=clean_system_prompt or system_prompt,
                judge_model=judge_model,
            )

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
