from openai import AsyncOpenAI
from pydantic import BaseModel

class llm_instance:
    def __init__(self, api_key: str, base_url: str, tools: list):
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        self.tools = tools
    
    async def generate_response(self, input):
        response = await self.client.responses.create(
            input=input,
            tools=self.tools,
            tool_choice="auto",
            # temperature=1.0,
            # top_p=0.95,
            # frequency_penalty=0,
            # presence_penalty=0,
            max_output_tokens=64000,
        )
        return response