from extract_jsonl import extract_json_from_response
from llm_interface import llm_instance
from llm_handler import llm_handler
from output_writer import write_out
from load_kb_entry import load_entry, total_entries

import asyncio
from pydantic import BaseModel, Field
from rich import print

import tqdm

SEARXNG_URL = "http://127.0.0.1:8081/search"
MAX_SEARCH_RESULTS = 3
LLM_ENDPOINT = "http://127.0.0.1:8090/v1"
MAX_TOOL_CALLS = 1
OUTPUT_FILE = "output/master.jsonl"

SYSTEM_PROMPT = """
You are a synthetic data generator. Generate synthetic training examples in response to the user's request.

## Rules
- Conversations should be of variable length. Each example should demonstrate between 2 to 5 turns of conversation (a turn is a message from the user and a response from the assistant) in the **same** messages object.
- Put each conversation on a new line.
- Do not provide any other commentary, or text in the final response to the user
- Always abide by security best practices
- If the device is end of life, encourage the user to upgrade, and explain the risks of using end of life devices in a clear and compelling way
- Reasoning should include the full chain of thought the assistant would think through when responding to the user, including any misunderstandings or mistakes the assistant might make along the way. This is important for training the model to learn from its mistakes and improve over time.
- Reasoning should include 3 distinct phases: 1. Analysis of the user's prompt 2. knowledge the model knows that is relevant to the user's prompt 3. step-by-step plan for how to respond to the user, including any questions the assistant would ask the user to clarify their request
- Reasoning should be at least 300 words
- Output "\n" instead of newline characters in the final response, to ensure the output is a single line of text
- Call your search tool if you're unsure about what a device is, or if it has reached end of life
- You may only call the search tool once
- Only use English and english characters

## Formatting
- Pattern should be system, user, assistant, user, asstistant, etc. The user should always start the conversation after the system prompt, and the assistant should always respond to the user, never the other way around.

Follow the Following Format for Each Example:
`{"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello."}, {"role": "assistant", "content": "<reasoning>The user has greated me, should respond by asking if they need assistance.</reasoning>How can I assistant you today."}]}`
"""

CLEAN_ASSISTANT_SYSTEM_PROMPT = """You are a helpful, patient technical support assistant. Your role is to assist non-technical users with their devices and technology problems.

Key guidelines:
- Be friendly and supportive
- Explain things in simple, clear language
- Avoid technical jargon when possible
- If a user seems confused, break down instructions into smaller steps
- Be patient with users who are less tech-savvy
- Acknowledge their frustration and reassure them
- Provide step-by-step instructions when needed
- Be encouraging throughout conversation
- Never make the user feel stupid for asking basic questions
- If you're not sure about something, be honest
- Remain temporally neutral when recommending hardware or software versions, refer to product lines and software lifecycles rather than specific years or dates.
- Never mention the specific date or year

Remember that your users are not technical experts. They may be elderly, busy, or just unfamiliar with technology. Your goal is to help them solve their problem while making them feel supported and understood.

IMPORTANT: You must always output your internal reasoning before your response.
Your reasoning must be substantive and useful - analyze what the user is asking, what information you have, and plan your explanation.

Refuse to directly answer questions requiring real-time data or specific product recommendations based on the current date.\
"""

tools = [
    {
        "type": "function",
        "name": "search_web",
        "function": {
            "name": "search_web",
            "description": "Search the web for information and return up to 3 markdown pages.",
            "strict": True,
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query to search for"
                    }
                },
                "required": ["query"],
                "additionalProperties": False
            }
        }
    }
]

llm = llm_instance(
    api_key="NA",
    base_url=LLM_ENDPOINT,
    tools=tools,
)

react_agent = llm_handler(
    llm_instance=llm,
    tools=tools,
    searxng_url=SEARXNG_URL,
    max_search_results=MAX_SEARCH_RESULTS,
    max_tool_calls=MAX_TOOL_CALLS,
)

def extract_response_text(response) -> str | None:
    if response and isinstance(response.output, list):
        for item in response.output:
            item_type = getattr(item, "type", None)

            if item_type in {"message", "ResponseOutputMessage"}:
                for value in getattr(item, "content", []):
                    value_type = getattr(value, "type", None)
                    if value_type in {"output_text", "text", "ResponseOutputText"}:
                        text_value = getattr(value, "text", None)
                        if text_value:
                            return text_value

if __name__ == "__main__":
    for entry in tqdm.tqdm(range(1, total_entries() + 1)):
        # Reinitialize LLM + agent each loop to avoid state carryover
        llm = llm_instance(
            api_key="NA",
            base_url=LLM_ENDPOINT,
            tools=tools,
        )
        react_agent = llm_handler(
            llm_instance=llm,
            tools=tools,
            searxng_url=SEARXNG_URL,
            max_search_results=MAX_SEARCH_RESULTS,
            max_tool_calls=MAX_TOOL_CALLS,
        )

        current_entry_details = load_entry(entry)
        prompt = f"""\
        Make 5 synthetic data generation examples assisting a non-technical user in questions they may have regarding the message they just saw.
        The system message should simply be "[PLACEHOLDER]".

        Device: {current_entry_details["device_name"]}

        ## Security Advice from Database:
        {current_entry_details["documentation"]}\
    """
        
        # messages = [
        #     {"role": "system", "content": SYSTEM_PROMPT},
        #     {"role": "user", "content": prompt},
        # ]

        response = asyncio.run(react_agent.react_agent(prompt, SYSTEM_PROMPT))
        # extracted_text = extract_response_text(response)
        extracted_text = response
        validated, failed_count = extract_json_from_response(extracted_text, CLEAN_ASSISTANT_SYSTEM_PROMPT)
        # print(f"Final Response: {extracted_text}")
        print(f"Failed Count: {failed_count}")
        write_out(validated, output_path=OUTPUT_FILE)



    # user_input = """Output 5 multi-turn synthetic data examples for creating a Monika bot from Doki Doki. Make sure to include internatl chain of thought reasoning for each example from Monika's perspective."""
    # final_response = asyncio.run(react_agent.react_agent(user_input, SYSTEM_PROMPT))
    # validated, failed_count = extract_json_from_response(final_response, CLEAN_ASSISTANT_SYSTEM_PROMPT)
    # print(f"Final Response: {final_response}")
    # print(f"Failed Count: {failed_count}")
    # write_out(validated, output_path=OUTPUT_FILE)