import json
import re
from pydantic import BaseModel, ValidationError, model_validator
from typing import List, Literal

class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str

class ChatFormat(BaseModel):
    messages: List[Message]

def validate_turn_structure(messages: List[Message]) -> bool:
    """
    Validates that the conversation follows a logical turn structure:
    - Starts with a system message
    - User and assistant messages alternate
    - Contains at least 2 turns (user + assistant)
    """
    if not messages or messages[0].role != "system":
        return False

    last_role = "system"
    user_turns = 0
    assistant_turns = 0

    for msg in messages[1:]:
        if msg.role == last_role:
            return False  # Two consecutive messages from the same role
        if msg.role == "user":
            user_turns += 1
        elif msg.role == "assistant":
            assistant_turns += 1
        last_role = msg.role

    return user_turns > 0 and assistant_turns > 0

def extract_json_from_response(response: str, assistant_system_prompt: str) -> tuple[List, int]:
    responses = response.splitlines()
    failed_count = 0

    json_list = []

    for line in responses:
        try:
            json_data = json.loads(line)
            if isinstance(json_data, dict) and "messages" in json_data:
                # check for validation of messages format
                try:
                    validate_data = ChatFormat.model_validate_json(json.dumps(json_data))
                    if not validate_turn_structure(validate_data.messages):
                        print("Failed validation for turn structure, skipping example.")
                        failed_count += 1
                        continue
                    # swap system prompt for the clean one
                    # swap reasoning for thinking tags
                    for message in json_data["messages"]:
                        # print(message.keys())
                        if message["role"] == "system":
                            message["content"] = assistant_system_prompt
                        if message["role"] == "assistant":
                            if re.search(r"<reasoning>.*?</reasoning>\s*\S", message["content"], re.DOTALL):
                                message["content"] = re.sub(r"<reasoning>", "<think>", message["content"])
                                message["content"] = re.sub(r"</reasoning>", "</think>", message["content"])
                            else:
                                raise ValueError("Assistant message missing <reasoning>...</reasoning> block")

                    json_list.append(json_data)
                except ValidationError as e:
                    failed_count += 1
                    print(f"Validation error: {e}, skipping example.")
                    continue
                except ValueError as e:
                    print(f"Value error: {e}, skipping example.")
                    failed_count += 1
                    continue
        except json.JSONDecodeError:
            if line != "\n" and line != "```json" and line != "```":
                print(f"Failed to parse line as JSON: {line}, skipping example.")
                failed_count += 1
            continue
    return (json_list, failed_count)