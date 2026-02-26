import streamlit as st
import sqlite3
import json
from openai import OpenAI

# --- CONFIGURATION ---
DEFAULT_SERVER_URL = "http://localhost:8080/v1/responses"
KNOWLEDGE_BASE = "./context/knowledge_base.db"
VAL_PATH = "./output/mlx-datasets/valid.jsonl"
DEVICE_CTX = "TCL Roku TV (2019)"

st.set_page_config(page_title="GGUF LoRA Tester (Responses API)", layout="wide")

# --- UTILITIES ---
def construct_device_context(device_str, knowledge_base=KNOWLEDGE_BASE, val_path=VAL_PATH):
    """Builds the faked context to trick the model into its specific task."""
    system_prompt = ""
    fake_user = f"[System Command]: Load reference for {device_str}"
    
    try:
        with open(val_path, "r") as f:
            line = json.loads(f.readline())
            for msg in line.get("messages", []):
                if msg["role"] == "system":
                    system_prompt = msg["content"]
                    break
    except Exception as e:
        raise ValueError("Could not load system prompt from validation set.")

    try:
        conn = sqlite3.connect(knowledge_base)
        cursor = conn.cursor()
        cursor.execute("SELECT documentation FROM knowledge WHERE device_name = ?", (device_str,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            fake_assistant = f"<think>\nTrigger: System Command received (\"Load reference for {device_str}\").\nAction: Retrieve \"{device_str} Update Guide\" from database.\nPlan: Output the full update instructions so the user has the context available immediately.\n</think>\n" + result[0]
        else:
            raise ValueError(f"No documentation found for device: {device_str}")
    except Exception as e:
        raise ValueError(f"Database error: {e}")

    # We keep the system prompt in the history list here, and filter it out during generation
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": fake_user},
        {"role": "assistant", "content": fake_assistant},
    ]

# --- SIDEBAR: SETTINGS ---
st.sidebar.header("Server Config")
server_url = st.sidebar.text_input("llama.cpp API URL", DEFAULT_SERVER_URL)
api_key = st.sidebar.text_input("API Key (Dummy)", "sk-no-key-required", type="password") 

st.sidebar.divider()

st.sidebar.header("Generation Parameters")
temp = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tok = st.sidebar.slider("Max Output Tokens", 100, 2048, 512)
freq_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 2.0, 0.0, 0.1)

if st.sidebar.button("Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# --- MAIN APP ---
st.title("💬 Qwen3 GGUF Server Chat")

client = OpenAI(base_url=server_url, api_key=api_key)

if "messages" not in st.session_state or not st.session_state.messages:
    with st.spinner("Loading device context..."):
        st.session_state.messages = construct_device_context(DEVICE_CTX)

for msg in st.session_state.messages:
    if msg["role"] in ["user", "assistant"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

if prompt := st.chat_input("Type your message here..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Responses API strictly separates instructions from input items
        instructions = ""
        input_messages = []
        for msg in st.session_state.messages:
            if msg["role"] == "system":
                instructions = msg["content"]
            else:
                input_messages.append(msg)
        
        try:
            stream = client.responses.create(
                model="local-model", 
                instructions=instructions,
                input=input_messages,
                temperature=temp,
                max_output_tokens=max_tok,
                # frequency_penalty=freq_penalty,
                stream=True,
            )
            
            # Watch the stream for the semantic text delta event
            for event in stream:
                if getattr(event, "type", "") == "response.output_text.delta":
                    if event.delta: # Guard against empty tokens
                        full_response += event.delta
                        message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"Connection failed! Is your llama-server running at {server_url}? \nError: {e}")
            st.stop()
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})