import playwright_tool

# langchain imports
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
from langchain_core.runnables import RunnableLambda
from typing import Literal
from langchain.agents import create_agent
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage

# other dependencies
import re, json, textwrap, shutil
from typing import Any, Dict, List
import asyncio
import sqlite3

def create_database():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_name TEXT NOT NULL,
            documentation TEXT NOT NULL
        )
    """)
    conn.commit()

def update_documentation(row_id: int, device_name: str, documentation: str):
    cursor.execute("UPDATE knowledge SET documentation = ? WHERE id = ?", (documentation, row_id))
    conn.commit()
    print(f"📝  Docs updated for {device_name} (id={row_id}).")

# set up connector to llama.cpp server (OpenAI-compatible API)
llm = ChatOpenAI(
    base_url="http://localhost:8090/v1",
    api_key="not-needed",
    model="gemma-4-31B-it",
    temperature=1.0,
)

# set up system prompt
SYSTEM_PROMPT = """\
You are a documentation reasearcher. Utilize your search tool in order to find relevant information \
regarding how to update the consumer devices provided by the user. \
Your output should be a step by step instruction guide detailing exactly what to click in the menu of the \
device to properly perform the update. After providing the instuctions, provide some general tips on how \
to keep the consumer device secure. If the device is end of life (ie doesn't receive future updates anymore) include a small seciton informing the \
user of the security issue and reccomend they upgrade to a new device and remove the old one from the network. If you \
reccomend the user to upgrade to a new device do not name a specific device, simply direct them to the manufacturer's website to find a \
newer model. Your instructions should be tailored for an average user trying to perform the update in their
home environment. Keep your instructions simple, easy to follow, and pratical for the home domain. \
Keep your response friendly and personable, do not include specific references to your research in the final response. \
Output your final answer in markdown format, but only answer once you have verified with your search tool the guide \
is correct. Limit yourself to at most 3 passes of the search tool.\
"""

# define the search tool
@tool
async def search(query: str) -> str:
    """
    Search the web to gather information.
    """
    print(f"🔍  Searching the web with: '{query}'")
    try:
        return await asyncio.wait_for(playwright_tool.search_and_parse_web(query), timeout=30)
    except asyncio.TimeoutError:
        print("⏰  Search timed out.")
        return "Search timed out."
    except Exception as e:
        print(f"❗  Search failed with error: {e}")
        return f"Search failed with error: {e}"

# tool list
tools = [search]

# make the simple react agent
base_agent = create_agent(llm, tools=tools, system_prompt=SYSTEM_PROMPT)

def _fallback_response(_):
    return {"messages": [AIMessage(content="Temporary model/tool error. Please retry later.")]} 

async def _fallback_response_async(_):
    return _fallback_response(_)

safe_agent = base_agent.with_fallbacks(
    fallbacks=[RunnableLambda(func=_fallback_response, afunc=_fallback_response_async)],
    exceptions_to_handle=(Exception,),
).with_retry(stop_after_attempt=3)

# make prompts for each device
dynamic_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "When you write your documentation do not mention upgrading to a specific version, just the 'latest version.' Also, do not include any boilerplate or address to the 'average user' in your response. Create documentation for the following device: {device_name}"),
    ]
)

# extract intermediate output from agent
async def extract_output(response):
    msgs = response.get("messages", [])

    try:
        for m in reversed(msgs):
            if isinstance(m, AIMessage):
                return m.content
    except AttributeError as e:
        print("Error extracting output:", e)
        return "Error extracting output."
    

output_parser = RunnableLambda(func=lambda x: x, afunc=extract_output)

# execution chain
chain = dynamic_prompt | safe_agent | output_parser

if __name__ == "__main__":
    ERROR_SENTINEL = "Temporary model/tool error. Please retry later."
    SRC_DB = "knowledge/knowledge_base.db"
    DST_DB = "knowledge/knowledge_base_complete.db"

    # copy the original DB so we never touch it
    shutil.copy2(SRC_DB, DST_DB)
    print(f"Copied {SRC_DB} -> {DST_DB}")

    conn = sqlite3.connect(DST_DB)
    cursor = conn.cursor()

    # find every row that still has the error placeholder
    cursor.execute(
        "SELECT id, device_name FROM knowledge WHERE documentation = ?",
        (ERROR_SENTINEL,),
    )
    failed_rows = cursor.fetchall()
    print(f"Found {len(failed_rows)} rows to retry.")

    async def main():
        inputs = [{"device_name": name} for _, name in failed_rows]
        chain_responses = await chain.abatch(inputs, config={"max_concurrency": 1})

        for (row_id, device_name), documentation in zip(failed_rows, chain_responses):
            update_documentation(row_id, device_name, documentation)

    asyncio.run(main())
    conn.close()