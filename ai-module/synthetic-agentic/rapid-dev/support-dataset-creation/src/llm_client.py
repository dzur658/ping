"""LLM client factory for creating agents and chat models using LangChain."""

from typing import Optional

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.tools import BaseTool

from .config import (
    OLLAMA_BASE_URL,
    USER_MODEL_KWARGS,
    ASSISTANT_MODEL_KWARGS,
)
from .models import ReasoningResponse
from .data_utils import strip_think_tags


def create_assistant_agent(
    model_name: str,
    system_prompt: str,
    tools: list[BaseTool],
    **model_kwargs,
):
    """Create a ReAct agent with structured output for assistant responses.

    Args:
        model_name: Name of the Ollama model to use
        system_prompt: System prompt for the agent
        tools: List of tools the agent can use
        **model_kwargs: Additional model parameters (temperature, num_ctx, etc.)

    Returns:
        Compiled LangChain agent
    """
    kwargs = {**ASSISTANT_MODEL_KWARGS, **model_kwargs}
    model = ChatOllama(
        model=model_name,
        base_url=OLLAMA_BASE_URL,
        **kwargs,
    )

    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
        response_format=ReasoningResponse,
    )
    return agent


def create_user_model(model_name: str, **model_kwargs):
    """Create a simple chat model for user responses.

    Args:
        model_name: Name of the Ollama model to use
        **model_kwargs: Additional model parameters (temperature, num_ctx, etc.)

    Returns:
        ChatOllama model instance
    """
    kwargs = {**USER_MODEL_KWARGS, **model_kwargs}
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
    messages = [{"role": "system", "content": persona_prompt}]
    messages.extend(conversation_history)
    messages.append(
        {
            "role": "user",
            "content": f"You are asking about your {device_name}. Based on the assistant's response above, ask a natural follow-up question that shows you're trying to understand or implement their advice. Keep your response concise and in character as {persona_prompt.split('You are roleplaying as ')[1].split(',')[0]}.",
        }
    )

    response = await user_model.ainvoke(messages)
    return strip_think_tags(response.content.strip()) if response.content else ""
