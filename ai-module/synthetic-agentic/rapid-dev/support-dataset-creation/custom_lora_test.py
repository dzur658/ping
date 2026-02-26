import streamlit as st
import sqlite3
import json
import mlx.core as mx
from mlx_lm import load, generate

# --- CONFIGURATION ---
DEFAULT_MODEL = "Qwen/Qwen3-1.7B"
DEFAULT_ADAPTER_DIR = "./adapters"  # Current directory

KNOWLEDGE_BASE = "./context/knowledge_base.db"
VAL_PATH = "./output/mlx-datasets/valid.jsonl"
DEVICE_CTX = "TCL Roku TV (2019)"

st.set_page_config(page_title="LoRA Chat Tester", layout="wide")

# --- CACHED MODEL LOADER ---
@st.cache_resource
def load_model_and_adapters(model_path, adapter_path):
    """
    Loads the model and adapter only once.
    """
    try:
        # Load model with LoRA adapters overlaid
        model, tokenizer = load(model_path, adapter_path=adapter_path)
        return model, tokenizer, None
    except Exception as e:
        return None, None, str(e)

# --- UTILITIES ---
def ensure_think_tag(messages):
    """Ensure every assistant message begins with '<think>' when used in context/display."""
    tagged = []
    for m in messages:
        content = m["content"]
        if m["role"] == "assistant" and not content.lstrip().startswith("<think>"):
            content = "<think>" + content
        tagged.append({**m, "content": content})
    return tagged

def contrust_device_context(device_str, knowledge_base=KNOWLEDGE_BASE, val_path=VAL_PATH):
    system_prompt = ""
    fake_user = f"[System Command]: Load reference for {device_str}"
    fake_assistant = ""

    # system prompt remains the same so just grab the first instance from the validation set
    with open(val_path, "r") as f:
        line = f.readline()
        line = json.loads(line)
        for msg in line["messages"]:
            if msg["role"] == "system":
                system_prompt = msg["content"]
                break
    
    # 
    conn = sqlite3.connect(knowledge_base)
    cursor = conn.cursor()
    cursor.execute("SELECT documentation FROM knowledge WHERE device_name = ?", (device_str,))
    result = cursor.fetchone()
    if result:
        fake_assistant = f"<think>\nTrigger: System Command received (\"Load reference for {device_str}\").\nAction: Retrieve \"{device_str} Update Guide\" from database.\nPlan: Output the full update instructions so the user has the context available immediately.\n</think>" + result[0]
    else:
        raise ValueError(f"No documentation found for device: {device_str}")

    context = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": fake_user},
        {"role": "assistant", "content": fake_assistant},
    ]

    return context

def build_temperature_sampler(t: float):
    """Return a sampler callable that applies temperature to log-probs.

    When t <= 0, falls back to greedy argmax sampling. Otherwise samples
    from the categorical distribution with logits scaled by 1/t.
    """
    try:
        temp = float(t)
    except Exception:
        temp = 0.0

    if temp <= 0.0:
        return lambda logprobs: mx.argmax(logprobs, axis=-1)

    def _sampler(logprobs):
        # logprobs is log-softmaxed; scaling by 1/temp adjusts entropy
        return mx.random.categorical(logprobs / temp, axis=-1)

    return _sampler

def build_repetition_penalty_processor(penalty: float, window: int):
    """Return a logits processor that penalizes tokens seen recently.

    Applies a simple presence-based penalty to logits for any token id
    that appeared within the last `window` tokens.
    """
    try:
        p = float(penalty)
    except Exception:
        p = 0.0
    try:
        w = int(window)
    except Exception:
        w = 0

    def _processor(tokens, logits):
        if p <= 0.0 or w <= 0:
            return logits
        try:
            n = len(tokens)
            start = max(0, n - w)
            recent = tokens[start:]
            ids = [int(x) for x in recent.tolist()] if hasattr(recent, "tolist") else []
        except Exception:
            return logits
        if not ids:
            return logits
        uniq = set(ids)
        # logits shape expected: (1, vocab_size)
        try:
            row = logits[0].tolist()
        except Exception:
            return logits
        vocab_size = len(row)
        for idx in uniq:
            if 0 <= idx < vocab_size:
                row[idx] = row[idx] - p
        return mx.array([row], dtype=logits.dtype)

    return _processor

# --- SIDEBAR: SETTINGS ---
st.sidebar.header("Model Config")
model_name = st.sidebar.text_input("Base Model", DEFAULT_MODEL)
adapter_dir = st.sidebar.text_input("Adapter Path", DEFAULT_ADAPTER_DIR)
reload_btn = st.sidebar.button("Reload Model")

if reload_btn:
    st.cache_resource.clear()
    st.session_state.messages = [] # Clear chat on reload

st.sidebar.divider()

st.sidebar.header("Generation Parameters")
system_prompt = st.sidebar.text_area("System Prompt", value="You are a helpful AI assistant.")
temp = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tok = st.sidebar.slider("Max Tokens", 100, 2048, 512)
rep_penalty = st.sidebar.slider("Repetition Penalty", 0.0, 3.0, 1.1, 0.1)
rep_window = st.sidebar.slider("Penalty Window (tokens)", 0, 1024, 128, 16)

if st.sidebar.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# --- MAIN APP ---
st.title("💬 Qwen3 LoRA Chat")

# 1. Load Model
with st.spinner("Accessing Neural Engine..."):
    model, tokenizer, error = load_model_and_adapters(model_name, adapter_dir)

if error:
    st.error(f"Failed to load model: {error}")
    st.stop()

# 2. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = contrust_device_context(DEVICE_CTX)  # Load initial context from validation set

# 3. Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Chat Input & Processing
if prompt := st.chat_input("Type your message here..."):
    # A. Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # B. Add to History
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # C. Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        # Prepare the full conversation for the model
        # We construct the list including the system prompt, tagging assistant turns
        conversation_history = st.session_state.messages  # Already includes system prompt and initial context
        print(conversation_history)
        
        # Apply Qwen's chat template
        full_prompt = tokenizer.apply_chat_template(
            conversation_history, 
            tokenize=False, 
            add_generation_prompt=True
        )
        # Ensure the model sees '<think>' at the start of the assistant turn
        full_prompt = full_prompt
        
        # Generate
        response = generate(
            model, 
            tokenizer, 
            prompt=full_prompt, 
            verbose=False,
            max_tokens=max_tok,
            sampler=build_temperature_sampler(temp),
            logits_processors=[build_repetition_penalty_processor(rep_penalty, rep_window)],
        )
        
        # Display Final Response (model already saw '<think>' in prompt)
        message_placeholder.markdown(response)
    
    # D. Save Assistant Response to History
    st.session_state.messages.append({"role": "assistant", "content": response})

# --- DEBUG EXPANDER ---
with st.expander("Debug: View Raw Prompt"):
    if 'full_prompt' in locals():
        st.text(full_prompt)