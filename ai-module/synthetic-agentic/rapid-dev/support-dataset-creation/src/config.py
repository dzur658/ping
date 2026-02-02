"""Configuration for synthetic conversation generation."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class SamplingConfig:
    """Configuration for LLM sampling parameters."""

    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None
    repeat_penalty: Optional[float] = None
    num_ctx: Optional[int] = None
    seed: Optional[int] = None

    def to_ollama_options(self) -> dict:
        base = {
            "temperature": self.temperature,
            "num_predict": self.max_tokens,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "repeat_penalty": self.repeat_penalty,
            "num_ctx": self.num_ctx,
            "seed": self.seed,
        }
        return {k: v for k, v in base.items() if v is not None}


BASE_DIR = Path(__file__).parent.parent

# Ollama settings
DEFAULT_OLLAMA_MODEL = "qwen3-next:80b-a3b-thinking-fp16"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"

# SearXNG settings
SEARXNG_URL = "http://127.0.0.1:8081/search"
MAX_SEARCH_RESULTS = 3

# Conversation settings
MIN_TURNS = 2
MAX_TURNS = 10
DEFAULT_CONVERSATIONS_PER_DEVICE = 5
DEFAULT_WORKERS = 16

# Output settings
OUTPUT_DIR = BASE_DIR / "output"
DEFAULT_OUTPUT_FILE = OUTPUT_DIR / "master.jsonl"

# Database paths
CONSUMER_DEVICES_FILE = BASE_DIR / "context" / "consumer_devices.txt"
KNOWLEDGE_BASE_DB = BASE_DIR / "context" / "knowledge_base.db"

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 1.0

# Tool settings
SEARCH_TOOL_ENABLED = True
MAX_TOOL_CALLS_PER_TURN = 2

# =============================================================================
# Sampling Parameters
# =============================================================================

# User model: higher temperature for creative/varied responses
USER_SAMPLING = SamplingConfig(
    temperature=0.7,
    max_tokens=32768,
    top_p=0.8,
    top_k=20,
    num_ctx=32768,
)

# Assistant model: lower temperature for focused/accurate responses
ASSISTANT_SAMPLING = SamplingConfig(
    temperature=0.7,
    max_tokens=64000,
    top_p=0.8,
    top_k=20,
    num_ctx=64000,
)

# Default fallback
DEFAULT_SAMPLING = SamplingConfig()
