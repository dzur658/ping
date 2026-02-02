import playwright_tool

# langchain imports
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
from langchain_core.runnables import RunnableLambda
from typing import Literal
from langchain.agents import create_agent
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage

# other dependencies
import re, json, textwrap
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

def store_documentation(current_device: str, documentation: str):
    cursor.execute("INSERT INTO knowledge (device_name, documentation) VALUES (?, ?)", (current_device, documentation))
    conn.commit()
    print(f"📝  Docs created for {current_device}.")

# set up connector to Ollama model
llm = ChatOllama(model="gpt-oss:120b", temperature=1.0, top_p=1.0, num_ctx=128000, reasoning="high")

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

# make runnable lambda to store results in database
store_runnable = RunnableLambda(func=lambda x: x, afunc=store_documentation)

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
    # set up database
    DB_FILE = "knowledge/knowledge_base.db"
    SEEDS = "seeds/consumer_devices.txt"

    # persistent connection
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    devices_to_investigate = []
    with open(SEEDS, "r") as f:
        for line in f:
            devices_to_investigate.append(line.strip())

    # testing
    # devices_to_investigate = devices_to_investigate[:1]
    
    # if it doesn't exist
    create_database()

    # iterate through each device and run the chain
    async def main():
        inputs = [ {"device_name": device} for device in devices_to_investigate ]
        chain_responses = await chain.abatch(inputs, config={"max_concurrency": 6})
        
        paired_results = list(zip(devices_to_investigate, chain_responses))

        # store in sqlite at the end to avoid race conditions
        for device, documentation in paired_results:
            store_documentation(device, documentation)
    
    # run asynchronously
    asyncio.run(main())

    conn.close()