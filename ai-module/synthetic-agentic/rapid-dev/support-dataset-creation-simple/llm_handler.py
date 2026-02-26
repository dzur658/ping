# handles looping for LLM tool calls and response generation
import json
from llm_interface import llm_instance
from tools.playwright_tool import search_web
from rich import print

class llm_handler:
    def __init__(self, llm_instance: llm_instance, tools: list, searxng_url: str, max_search_results: int, max_tool_calls: int = 1):
        self.llm_instance = llm_instance
        self.tools = tools
        self.searxng_url = searxng_url
        self.max_search_results = max_search_results
        self.max_tool_calls = max_tool_calls
        self.messages = []
        self.system_prompt = None

    def _extract_response_text(self, response) -> str | None:
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

        direct_text = getattr(response, "text", None) if response else None
        if direct_text:
            return direct_text

        return None

    async def react_agent(self, input: str, system_prompt: str) -> str:
        current_tool_call_count = 0

        if not self.messages or self.system_prompt != system_prompt:
            self.messages = [{"role": "system", "content": system_prompt}]
            self.system_prompt = system_prompt

        self.messages.append({"role": "user", "content": input})

        response = None

        while True:
            response = await self.llm_instance.generate_response(self.messages)
            print(f"LLM Response: {response}")
            output_items = response.output if isinstance(response.output, list) else []
            function_calls = [
                item
                for item in output_items
                if getattr(item, "type", None) in {"function_call", "ResponseFunctionCall"}
            ]

            if not function_calls:
                assistant_text = self._extract_response_text(response)
                if assistant_text:
                    self.messages.append({"role": "assistant", "content": assistant_text})
                break

            assistant_tool_calls = []
            tool_outputs = []
            final_prompt = None

            for item in function_calls:
                tool_name = getattr(item, "name", None)
                tool_args = getattr(item, "arguments", {}) or {}
                tool_call_id = getattr(item, "call_id", None)
                print(f"Tool Call: {tool_name} with args {tool_args}")

                serialized_arguments = tool_args
                if isinstance(serialized_arguments, dict):
                    serialized_arguments = json.dumps(serialized_arguments)
                if not isinstance(serialized_arguments, str):
                    serialized_arguments = "{}"

                if tool_call_id and tool_name:
                    assistant_tool_calls.append({
                        "type": "function_call",
                        "call_id": tool_call_id,
                        "name": tool_name,
                        "arguments": serialized_arguments,
                    })

                if tool_name != "search_web":
                    unknown_tool_message = f"Unknown tool: {tool_name}, tools available are: {[tool['function']['name'] for tool in self.tools]}"
                    if tool_call_id:
                        tool_outputs.append({
                            "type": "function_call_output",
                            "call_id": tool_call_id,
                            "output": unknown_tool_message,
                        })
                    else:
                        final_prompt = unknown_tool_message
                    continue

                if current_tool_call_count >= self.max_tool_calls:
                    final_prompt = "Maximum number of search_web tool calls reached. Please provide a final answer based on the information you have."
                    break

                if isinstance(tool_args, str):
                    try:
                        tool_args = json.loads(tool_args)
                    except json.JSONDecodeError:
                        tool_args = {}

                query = tool_args.get("query") if isinstance(tool_args, dict) else None
                if not query:
                    query_example = {"query": "My query here"}
                    final_prompt = f"search_web was called without a valid 'query'. You sent {tool_args}. But you should send {query_example}"
                
                tool_output = await search_web(query, self.searxng_url, self.max_search_results)
                print(tool_output)
                if tool_call_id:
                    tool_outputs.append({
                        "type": "function_call_output",
                        "call_id": tool_call_id,
                        "output": f"<tool_output>{tool_output}</tool_output>",
                    })
                else:
                    final_prompt = f"Tool output: {tool_output}"
                current_tool_call_count += 1

            if final_prompt:
                next_input = [{"role": "user", "content": final_prompt}]
            elif tool_outputs:
                next_input = assistant_tool_calls + tool_outputs
            else:
                next_input = [{"role": "user", "content": "Please provide your final answer."}]

            self.messages.extend(next_input)

        final_text = self._extract_response_text(response)
        if final_text:
            return final_text

        return "No final response generated."