# Synthetic Support Conversation Generator

Generate synthetic support conversations for LoRA fine-tuning using local Ollama models and web search tools.

## Overview

This tool creates realistic multi-turn support conversations between:
- **User Model**: Simulates non-technical users with diverse personas
- **Assistant Model**: Provides grounded support responses using web search

Conversations build upon pre-generated responses from `knowledge_base.db` and cover troubleshooting, menu navigation clarification, and general questions.

## Installation

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browser
playwright install chromium

# (Optional) Ensure Ollama is running and has your model pulled
ollama pull llama3.2
```

## Quick Start

```bash
# Generate 5 conversations for all devices
python generate_conversations.py

# Generate for a specific device
python generate_conversations.py --device "iPhone 14" --num-per-device 3

# Generate for a category (e.g., all Ring devices)
python generate_conversations.py --filter "Ring" --num-per-device 10

# Use a different model and increase parallelism
python generate_conversations.py --model llama3.2 --workers 8
```

## Output Format

Generates MLX-compatible JSONL files:

```json
{"messages": [
  {"role": "system", "content": "You are a helpful technical support assistant..."},
  {"role": "user", "content": "I have a Ring Video Doorbell 3..."},
  {"role": "assistant", "content": "I'd be happy to help..."},
  ...
]}
```

## Features

- **12 diverse user personas**: From elderly retirees to busy professionals
- **Variable conversation length**: 2-10 turns per conversation
- **Web search integration**: Assistant uses `playwright_tool.py` for grounding
- **Parallel generation**: Generate multiple conversations simultaneously
- **Configurable**: Customize models, prompts, and output format

## Project Structure

```
support-dataset-creation/
├── context/                    # Data sources
│   ├── consumer_devices.txt    # 1,070 device names
│   └── knowledge_base.db       # Pre-generated device docs
├── tools/
│   └── playwright_tool.py      # Web search & parsing
├── src/
│   ├── config.py              # Configuration
│   ├── llm_client.py          # Ollama API wrapper
│   ├── personas.py            # User persona definitions
│   ├── prompts.py             # Prompt templates
│   ├── conversation_engine.py  # Core generation logic
│   ├── data_utils.py          # Data I/O utilities
│   └── tools/
│       └── playwright_tool.py # Web search via SearXNG + Playwright
├── output/                    # Generated conversations
└── generate_conversations.py  # Main CLI entry point
```

## CLI Options

| Option | Description | Default |
|--------|-------------|---------|
| `--device` | Specific device name | All devices |
| `--filter` | Filter devices by pattern | No filter |
| `--num-per-device` | Conversations per device | 5 |
| `--model` | Ollama model | `llama3.2` |
| `--workers` | Concurrent generators | 4 |
| `--output` | Output JSONL path | `output/conversations.jsonl` |
| `--system-prompt` | Custom assistant prompt | See `prompts.py` |
| `--max-turns` | Override max turns | 10 |
| `--ollama-url` | Ollama API URL | `http://127.0.0.1:11434` |

## Requirements

- Python 3.10+
- Ollama running locally
- SearXNG instance (optional, for web search)
- ~2GB RAM for base operation, more with high worker counts

## Examples

### Generate small test dataset
```bash
python generate_conversations.py \
  --filter "iPhone" \
  --num-per-device 1 \
  --workers 2 \
  --output ./output/test.jsonl
```

### Large-scale generation
```bash
python generate_conversations.py \
  --num-per-device 10 \
  --workers 12 \
  --output ./output/full_dataset.jsonl
```

### Custom assistant personality
```bash
python generate_conversations.py \
  --system-prompt "You are a friendly, patient tech support specialist who loves helping people solve problems."
```

## Notes

- Web search results are used internally and not included in training data
- All personas are non-technical (tech level 1-3)
- Conversations are validated before saving
- Failed generations are logged but don't halt execution

## Troubleshooting

**Ollama connection errors**: Ensure Ollama is running with `ollama serve`

**Playwright not found**: Run `playwright install chromium`

**Slow generation**: Reduce `--workers` or use a smaller model

**Search errors**: SearXNG is optional - generation continues without it

## See Also

- `AGENTS.md` - Guidelines for AI coding agents
- `tools/playwright_tool.py` - Web search implementation
