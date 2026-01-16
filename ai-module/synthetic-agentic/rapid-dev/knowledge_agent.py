import playwright_tool

# langchain imports
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
from langchain_core.runnables import RunnableLambda
from typing import Literal
from langchain.agents import create_agent
from langchain_core.output_parsers import StrOutputParser

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

# hacky way to get around implementing weird langchain logic for device name passing
counter = 0
async def store_documentation(documentation: str):
    global counter
    current_device = devices_to_investigate[counter]

    cursor.execute("INSERT INTO knowledge (device_name, documentation) VALUES (?, ?)", (current_device, documentation))
    conn.commit()
    counter += 1
    print(f"📝  Docs created for {current_device}.")

# set up connector to Ollama model
llm = ChatOllama(model="gpt-oss:120b", temperature=1.0, top_p=1.0, format="json", num_ctx=128000, reasoning="high")

# set up system prompt
SYSTEM_PROMPT = """\
You are a documentation reasearcher. Utilize your search tool in order to find relevant information \
regarding how to update the consumer devices provided by the user. \
Your output should be a step by step instruction guide detailing exactly what to click in the menu of the \
device to properly perform the update. After providing the instuctions, provide some general tips on how \
to keep the consumer device secure. Remember you are writing for non-technical consumers operating in a \
home environment. Keep your instructions simple, easy to follow, and pratical for the home domain. \
Output your final answer in markdown format, but only answer once you have verified with your search tool the guide \
is correct.\
"""

# define the search tool
@tool
async def search(query: str) -> str:
    """
    Search the web to gather information.
    """
    print(f"🔍  Searching the web with: '{query}'")
    return await playwright_tool.search_and_parse_web(query)

# tool list
tools = [search]

# make the simple react agent
agent = create_agent(llm, tools=tools, system_prompt=SYSTEM_PROMPT)

# make prompts for each device
dynamic_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "Create documentation for the following device: {device_name}"),
    ]
)

# make runnable lambda to store results in database
store_runnable = RunnableLambda(func=lambda x: x, afunc=store_documentation)

# extract intermediate output from agent
async def extract_output(response):
    print(f"🕵 Agent response type: {type(response)}")
    print(f"🕵 Agent response: {response}")
    return response.get("output", str(response))

output_parser = RunnableLambda(func=lambda x: x, afunc=extract_output)

# execution chain
chain = dynamic_prompt | agent | output_parser | store_runnable

if __name__ == "__main__":
    # set up database
    DB_FILE = "knowledge_base.db"

    # persistent connection
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    devices_to_investigate = []
    with open("consumer_devices.txt", "r") as f:
        for line in f:
            devices_to_investigate.append(line.strip())

    # testing
    devices_to_investigate = devices_to_investigate[:5]
    
    # if it doesn't exist
    create_database()

    # iterate through each device and run the chain
    async def main():
        # map to dictionary
        inputs = [ {"device_name": device} for device in devices_to_investigate ]
        await chain.abatch(inputs)
    
    # run asynchronously
    asyncio.run(main())

    conn.close()