from transformers import AutoTokenizer
import json

# MODEL_TO_TEST = "openai/gpt-oss-120b" # 795 tokens for large CVE sample
# MODEL_TO_TEST = "zai-org/GLM-4.5-Air" # 819 tokens for large CVE sample
MODEL_TO_TEST = "Qwen/Qwen3-Next-80B-A3B-Thinking" # 910 tokens for large CVE sample

with open("./samples/large_sample.json", "r") as f:
    data = f.read()

tokenizer = AutoTokenizer.from_pretrained(MODEL_TO_TEST)
tokens = tokenizer.tokenize(data)
print(f"Number of tokens provided using {MODEL_TO_TEST}: {len(tokens)}")