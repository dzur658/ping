"""LLM client factory for creating agents and chat models using LangChain."""

from typing import Dict, Optional
from pydantic import SecretStr

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.tools import BaseTool

from .config import (
    BACKEND,
    OLLAMA_BASE_URL,
    DEFAULT_OLLAMA_MODEL,
    LLAMACPP_ASSISTANT_URL,
    LLAMACPP_USER_URL,
    LLAMACPP_API_KEY,
    LLAMACPP_ASSISTANT_MODEL,
    LLAMACPP_USER_MODEL,
    USER_MODEL_KWARGS,
    ASSISTANT_MODEL_KWARGS,
    JUDGE_MODEL_KWARGS,
)

if BACKEND == "llamacpp":
    from .llm_llamacpp import ChatLlamaCppFixed

from .models import ReasoningResponse
from .data_utils import strip_think_tags


def _translate_kwargs_for_openai(kwargs: Dict) -> Dict:
    """Translate Ollama-style kwargs to OpenAI/llama.cpp compatible kwargs.

    Maps:
        num_predict -> max_tokens
    Drops:
        num_ctx (set on llama.cpp server startup)
        top_k (not in OpenAI API)

    Args:
        kwargs: Original Ollama-style kwargs

    Returns:
        Translated kwargs for OpenAI API
    """
    translated = {}
    for key, value in kwargs.items():
        if key == "num_predict":
            translated["max_tokens"] = value
        elif key in ("num_ctx", "top_k"):
            continue
        else:
            translated[key] = value
    return translated


def create_assistant_agent(
    model_name: str,
    system_prompt: str,
    tools: list[BaseTool],
    **model_kwargs,
):
    """Create a ReAct agent with structured output for assistant responses.

    Args:
        model_name: Name of the model to use (ignored for llama.cpp, where model is server-side)
        system_prompt: System prompt for the agent
        tools: List of tools the agent can use
        **model_kwargs: Additional model parameters (temperature, num_ctx, etc.)

    Returns:
        Compiled LangChain agent
    """
    kwargs = {**ASSISTANT_MODEL_KWARGS, **model_kwargs}

    if BACKEND == "llamacpp":
        translated_kwargs = _translate_kwargs_for_openai(kwargs)
        model = ChatLlamaCppFixed(  # type: ignore
            base_url=LLAMACPP_ASSISTANT_URL,
            api_key=SecretStr(LLAMACPP_API_KEY),
            model=LLAMACPP_ASSISTANT_MODEL,
            **translated_kwargs,
        )
    else:
        model = ChatOllama(
            model=model_name,
            base_url=OLLAMA_BASE_URL,
            **kwargs,
        )

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
    )
    return agent


def create_user_model(model_name: str, **model_kwargs):
    """Create a simple chat model for user responses.

    Args:
        model_name: Name of the model to use (ignored for llama.cpp, where model is server-side)
        **model_kwargs: Additional model parameters (temperature, num_ctx, etc.)

    Returns:
        Chat model instance (ChatOllama or ChatOpenAI)
    """
    kwargs = {**USER_MODEL_KWARGS, **model_kwargs}

    if BACKEND == "llamacpp":
        translated_kwargs = _translate_kwargs_for_openai(kwargs)
        return ChatOpenAI(
            base_url=LLAMACPP_USER_URL,
            api_key=SecretStr(LLAMACPP_API_KEY),
            model=LLAMACPP_USER_MODEL,
            **translated_kwargs,
        )
    else:
        return ChatOllama(
            model=model_name,
            base_url=OLLAMA_BASE_URL,
            **kwargs,
        )


async def generate_user_response(
    user_model,
    persona_prompt: str,
    conversation_history: list,
    device_name: str,
) -> str:
    """Generate a user response based on persona and conversation history.

    Args:
        user_model: Chat model instance for user responses
        persona_prompt: Persona prompt for the user
        conversation_history: List of previous messages
        device_name: Name of the device being discussed

    Returns:
        Generated user response as string
    """
    from .prompts import (
        USER_PROMPT_CONTINUE,
        USER_PROMPT_CLARIFY,
        USER_PROMPT_DONE,
        USER_PROMPT_TROUBLE,
    )

    import random

    user_prompts = [
        USER_PROMPT_CONTINUE,
        USER_PROMPT_CLARIFY,
        USER_PROMPT_DONE,
        USER_PROMPT_TROUBLE,
    ]
    selected_prompt = random.choice(user_prompts)

    messages = [{"role": "system", "content": persona_prompt}]
    messages.extend(conversation_history)

    last_assistant_msg = None
    for msg in reversed(conversation_history):
        if msg.get("role") == "assistant":
            last_assistant_msg = msg.get("content", "")
            break

    guidance = ""
    if last_assistant_msg:
        guidance = f" The assistant just said: {last_assistant_msg[:500]}"

    messages.append(
        {
            "role": "user",
            "content": f"You are asking about your {device_name}.{guidance}\n\n{selected_prompt}\n\nRespond ONLY with your question or comment — no narration, no emojis, no stage directions like *smiles* or *leans back*. You are the person seeking help, not providing it.",
        }
    )

    response = await user_model.ainvoke(messages)
    return strip_think_tags(response.content.strip()) if response.content else ""


def create_judge_model(**model_kwargs):
    """Create a chat model for judging assistant responses.

    Args:
        **model_kwargs: Additional model parameters (temperature, num_ctx, etc.)

    Returns:
        Chat model instance (ChatOllama or ChatOpenAI)
    """
    kwargs = {**JUDGE_MODEL_KWARGS, **model_kwargs}

    if BACKEND == "llamacpp":
        translated_kwargs = _translate_kwargs_for_openai(kwargs)
        return ChatOpenAI(
            base_url=LLAMACPP_USER_URL,
            api_key=SecretStr(LLAMACPP_API_KEY),
            model=LLAMACPP_USER_MODEL,
            **translated_kwargs,
        )
    else:
        return ChatOllama(
            model=DEFAULT_OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            **kwargs,
        )


async def generate_judge_feedback(
    judge_model,
    user_message: str,
    assistant_response: str,
    conversation_context: list,
    failure_reason: str,
) -> str:
    """Generate feedback for a failed assistant response using the judge model.

    Args:
        judge_model: Chat model instance for judging
        user_message: The original user message
        assistant_response: The failed assistant response
        conversation_context: List of previous messages for context
        failure_reason: Description of why the response failed

    Returns:
        Feedback message string
    """
    from .prompts import JUDGE_SYSTEM_PROMPT

    messages = [{"role": "system", "content": JUDGE_SYSTEM_PROMPT}]

    messages.extend(conversation_context)

    prompt = f"""Analyze this failed assistant response and provide actionable feedback.

User Message:
{user_message}

Assistant Response:
{assistant_response}

Failure Reason:
{failure_reason}

Provide specific, actionable feedback to help the assistant improve its response on the next attempt."""
    messages.append({"role": "user", "content": prompt})

    response = await judge_model.ainvoke(messages)
    return response.content.strip() if response.content else ""
