"""Configuration for synthetic conversation generation."""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# Backend: "ollama" or "llamacpp"
BACKEND = "llamacpp"

# Ollama settings
DEFAULT_OLLAMA_MODEL = "qwen3-next:80b-a3b-thinking-fp16"
DEFAULT_USER_OLLAMA_MODEL = "hf.co/LiquidAI/LFM2.5-1.2B-Instruct-GGUF:BF16"
USER_MODEL_SUPPORTS_THINKING = False
OLLAMA_BASE_URL = "http://127.0.0.1:11434"

# llama.cpp server settings (only used when BACKEND = "llamacpp")
LLAMACPP_ASSISTANT_URL = "http://127.0.0.1:8090/v1"
# using the same server since lfm2.5 will not stay in character
LLAMACPP_USER_URL = "http://127.0.0.1:8090/v1"
LLAMACPP_API_KEY = "not-needed"

# Model names for llama.cpp (llama.cpp serves one model per server,
# but ChatOpenAI requires a model name — any string works)
LLAMACPP_ASSISTANT_MODEL = "assistant"
LLAMACPP_USER_MODEL = "user"

# SearXNG settings
SEARXNG_URL = "http://127.0.0.1:8081/search"
MAX_SEARCH_RESULTS = 3

# Conversation settings
# NOTE: Max and Min turns do not count the preamble of the generation ([system prompt], user [system command], or the assistant response pulled from the database).
# They only count the turns generated in the main loop of `generate_conversation`.
MIN_TURNS = 2
MAX_TURNS = 5
DEFAULT_CONVERSATIONS_PER_DEVICE = 3
DEFAULT_WORKERS = 1

# Output settings
OUTPUT_DIR = BASE_DIR / "output"
DEFAULT_OUTPUT_FILE = OUTPUT_DIR / "master.jsonl"

# Database paths
CONSUMER_DEVICES_FILE = BASE_DIR / "context" / "consumer_devices.txt"
KNOWLEDGE_BASE_DB = BASE_DIR / "context" / "knowledge_base.db"

# Retry settings
MAX_RETRIES = 2
RETRY_DELAY = 2.0
LOG_FILE = OUTPUT_DIR / "generation_failures.log"

# Tool settings
SEARCH_TOOL_ENABLED = True
MAX_TOOL_CALLS_PER_TURN = 1

USER_MODEL_KWARGS = {
    # "temperature": 1.0,
    # "num_predict": 32768,
    # "top_p": 1.0,
    # "top_k": 40,
    # "num_ctx": 32768,
}

ASSISTANT_MODEL_KWARGS = {
    # "temperature": 1.0,
    # "num_predict": 80000,
    # "top_p": 1.0,
    # "top_k": 40,
    # "num_ctx": 80000,
}

JUDGE_MODEL_KWARGS = {
    "temperature": 0.5,
    "num_predict": 4096,
    "top_p": 0.9,
    "top_k": 40,
    "num_ctx": 8192,
}
