import json
import os
import torch
from safetensors.torch import load_file, save_file

# --- CONFIGURATION ---
INPUT_DIR = "./dataset-creation/adapters"           # Folder containing your mlx-saved adapters
OUTPUT_DIR = "./dataset-creation/adapters-hf"       # Where to save the fixed HF-compatible adapters
MLX_WEIGHTS = "adapter_model.safetensors" 
MLX_CONFIG = "adapter_config.json"

def main():
    print(f"🔄 Converting MLX adapters from '{INPUT_DIR}' to Hugging Face format...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ---------------------------------------------------------
    # STEP 1: Fix the Config
    # ---------------------------------------------------------
    config_path = os.path.join(INPUT_DIR, MLX_CONFIG)
    if not os.path.exists(config_path):
        print(f"❌ Error: {MLX_CONFIG} not found in {INPUT_DIR}")
        return

    with open(config_path, "r") as f:
        mlx_data = json.load(f)

    # Flatten params if nested
    params = mlx_data.get("lora_parameters", mlx_data)

    hf_config = {
        "base_model_name_or_path": mlx_data.get("model", "Qwen/Qwen3-1.7B"),
        "peft_type": "LORA",
        "task_type": "CAUSAL_LM",
        "r": params.get("rank", 32),
        "lora_alpha": params.get("alpha", 64),
        "lora_dropout": params.get("dropout", 0.0),
        "target_modules": params.get("keys", []),
        "bias": "none"
    }

    with open(os.path.join(OUTPUT_DIR, "adapter_config.json"), "w") as f:
        json.dump(hf_config, f, indent=2)
    print("✅ Config converted.")

    # ---------------------------------------------------------
    # STEP 2: Fix the Weights (Rename AND Transpose)
    # ---------------------------------------------------------
    weights_path = os.path.join(INPUT_DIR, MLX_WEIGHTS)
    if not os.path.exists(weights_path):
        weights_path = os.path.join(INPUT_DIR, "adapters.safetensors")
    
    if not os.path.exists(weights_path):
        print(f"❌ Error: Could not find weights file in {INPUT_DIR}")
        return

    print("⏳ Loading, renaming, and TRANSPOSTING tensors...")
    tensors = load_file(weights_path)
    new_tensors = {}

    for k, v in tensors.items():
        # 1. Add the HF Prefix
        new_k = "base_model.model." + k if not k.startswith("base_model.model") else k
        
        # 2. Rename Suffixes & Transpose
        # MLX lora_a is (In, Rank) -> HF lora_A needs (Rank, In)
        if ".lora_a" in new_k:
            new_k = new_k.replace(".lora_a", ".lora_A.weight")
            v = v.t().contiguous() # <--- CRITICAL FIX: TRANSPOSE
            
        # MLX lora_b is (Rank, Out) -> HF lora_B needs (Out, Rank)
        elif ".lora_b" in new_k:
            new_k = new_k.replace(".lora_b", ".lora_B.weight")
            v = v.t().contiguous() # <--- CRITICAL FIX: TRANSPOSE

        new_tensors[new_k] = v

    save_file(new_tensors, os.path.join(OUTPUT_DIR, "adapter_model.safetensors"))
    print(f"✅ Weights transposed and saved to '{OUTPUT_DIR}'")
    print("\n🚀 READY: Run llama.cpp conversion on the 'adapters_hf' folder now.")

if __name__ == "__main__":
    main()