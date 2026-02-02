# AGENTS.md

This file contains guidelines for AI coding agents working on this repository.

## Project Overview

This project generates synthetic support conversation data for LoRA fine-tuning. It simulates conversations between non-technical users and helpful AI support assistants, using local Ollama models and web search tools.

## Build/Test/Run Commands

### Installation
```bash
pip install -r requirements.txt
playwright install chromium
```

### Running the Conversation Generator
```bash
# Generate for all devices (default 5 conversations each)
python generate_conversations.py

# Generate for specific device
python generate_conversations.py --device "iPhone 14"

# Generate for device category with custom count
python generate_conversations.py --filter "Ring" --num-per-device 10

# Specify model and parallelism
python generate_conversations.py --model llama3.2 --workers 8

# Custom output path and system prompt
python generate_conversations.py --output ./custom/output.jsonl --system-prompt "You are a friendly support specialist."

# Override maximum turns per conversation
python generate_conversations.py --max-turns 5
```

### Testing playwright_tool.py
```bash
# Search mode
python tools/playwright_tool.py "Ring doorbell firmware update"

# Direct URL mode
python tools/playwright_tool.py "https://example.com/page"
```

## Code Style Guidelines

### Imports
- Standard library imports first, then third-party, then local imports
- Group imports with blank lines between groups
- Use absolute imports for local modules: `from src.config import DEFAULT_OLLAMA_MODEL`
- No wildcard imports (`from module import *`)

### Formatting
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use type hints for all function parameters and return values
- Add docstrings for all functions and classes
- Use f-strings for string formatting

### Types
- Use modern type hints: `str`, `int`, `List[Dict]`, `Optional[str]`, etc.
- Return `Optional[T]` when a function may return `None`
- Use `Dict[str, str]` for message objects in conversations
- Import `from typing import List, Dict, Optional` at module level

### Naming Conventions
- **Modules**: `lowercase_with_underscores` (e.g., `data_utils.py`)
- **Classes**: `PascalCase` (e.g., `OllamaClient`, `ConversationEngine`)
- **Functions/Methods**: `lowercase_with_underscores` (e.g., `generate_conversation`, `get_random_persona`)
- **Constants**: `UPPERCASE_WITH_UNDERSCORES` (e.g., `DEFAULT_OLLAMA_MODEL`, `MAX_TURNS`)
- **Private methods**: `_lowercase_with_leading_underscore` (e.g., `_is_conversation_complete`)

### Error Handling
- Always wrap database operations in try/except blocks
- Use async/await for all I/O operations (network, disk, database)
- Implement retry logic for external API calls (see `OllamaClient.chat_completion`)
- Return `None` or empty values for non-critical failures
- Print warnings for issues that don't halt execution

### Async/Await
- All functions that perform I/O should be async
- Use `asyncio.gather()` for concurrent independent operations
- Use `asyncio.Semaphore` to limit concurrent operations
- Never use blocking calls in async functions (use async versions like `aiosqlite`, `httpx.AsyncClient`)

### File Organization
- Keep modules focused on single responsibility
- Configuration goes in `config.py`
- Utility functions go in appropriate modules (`data_utils.py`, `personas.py`, etc.)
- Main orchestration logic in root-level `generate_conversations.py`
- Tools in `tools/` directory

### SQL/Database
- Use parameterized queries: `cursor.execute("SELECT * FROM table WHERE name = ?", (name,))`
- Always close connections in try/finally blocks or use context managers
- Store paths as `Path` objects from `pathlib`

### JSONL Output Format
MLX format required for fine-tuning:
```json
{"messages": [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "User message"},
  {"role": "assistant", "content": "Assistant response"}
]}
```
Each line is a complete conversation. No trailing commas in JSON.

### Testing Approach
- No automated tests currently defined
- Test by running single device generation first: `python generate_conversations.py --device "iPhone 14" --num-per-device 1`
- Verify output JSONL is valid: `cat output/conversations.jsonl | jq .`

## Project-Specific Notes

### Persona Guidelines
- Only use personas defined in `personas.py`
- Never include IT professionals, sysadmins, or Linux hobbyists
- All personas should be non-technical (tech level 1-3)
- Persona must be specified in output for tracking

### Knowledge Base
- Always validate device exists in `knowledge_base.db` before generating
- Skip devices without documentation entries (warn and continue)
- Initial assistant response must include the knowledge base documentation

### Tool Integration
- Web search results are internal only (not visible in training data)
- Use `should_search()` to determine when searching is helpful
- Gracefully handle search failures (continue without error)

### Parallel Execution
- Default to 4 concurrent workers
- Use semaphore to limit concurrent conversations
- Add small random delay between task starts to smooth load
- Display progress with tqdm for batch operations

## Configuration

All defaults are in `src/config.py`:
- `DEFAULT_OLLAMA_MODEL`: Default Ollama model
- `OLLAMA_BASE_URL`: Ollama API endpoint
- `DEFAULT_WORKERS`: Number of concurrent conversation generators
- `MIN_TURNS` / `MAX_TURNS`: Conversation length bounds
- `SEARXNG_URL`: Local search engine endpoint

These can be overridden via CLI arguments.
