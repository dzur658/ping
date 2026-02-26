from functools import partial
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import json
import time
import numpy as np
from tqdm import tqdm
import mlx.optimizers as optim
from mlx_lm import load
from mlx_lm.tuner.utils import linear_to_lora_layers
from transformers import AutoTokenizer
import mlx.core as mx
import mlx.nn as nn
from mlx.utils import tree_flatten

# --- CONFIGURATION ---
MODEL_PATH = "Qwen/Qwen3-1.7B"
DATA_DIR = "./output/mlx-datasets"
ADAPTER_FILE = "./adapters/adapter_model"
LORA_CONFIG_FILE = "./adapters/adapter_config.json"
LEARNING_RATE = 1e-5
ITERS = 800
BATCH_SIZE = 4
REPORT_EVERY = 50
VAL_RATE = 100
WEIGHT_DECAY = 0.02
# ---------------------

# LoRA Hyperparameters
LORA_CONFIG = {
    "rank": 8,
    "scale": 16,
    "dropout": 0.0,
    "keys": [
        "self_attn.q_proj", "self_attn.k_proj", "self_attn.v_proj", "self_attn.o_proj", 
        "mlp.gate_proj", "mlp.up_proj", "mlp.down_proj"
    ]
}

def save_lora_manually(model, adapter_file, config_file):
    print(f"Saving adapters to {adapter_file}...")
    
    # 1. Flatten the trainable parameters (the LoRA weights)
    # tree_flatten turns the nested model structure into a flat list of ("key", value) tuples
    trainable_params = dict(tree_flatten(model.trainable_parameters()))
    
    # 2. Save weights
    mx.save_safetensors(adapter_file, trainable_params)
    
    # 3. Save config with the CORRECT NESTED SCHEMA
    with open(config_file, "w") as f:
        final_config = {
            # Top level: Model info
            "model": MODEL_PATH,
            "num_layers": len(model.layers), # Must match num_lora_layers used in training
            
            # Nested level: The actual LoRA settings
            "lora_parameters": LORA_CONFIG 
        }
        json.dump(final_config, f, indent=4)
        
    print("Adapters and config saved successfully.")

def load_and_tokenize(filename, tokenizer):
    print(f"Loading and processing {filename}...")
    filepath = f"{DATA_DIR}/{filename}"
    
    data = []
    with open(filepath, 'r') as f:
        # Load all JSON lines
        raw_data = [json.loads(line) for line in f]
    
    # Process each line
    for entry in raw_data:
        if "messages" in entry:
            messages = entry["messages"]
            
            # Build input_ids and a loss mask that only covers assistant turns
            full_ids = []
            loss_mask = []
            
            for i, msg in enumerate(messages):
                # Tokenize up to and including this message
                single_turn = tokenizer.apply_chat_template(
                    messages[:i+1], 
                    tokenize=False
                )
                if i == 0:
                    turn_ids = tokenizer(single_turn).input_ids
                    new_tokens = turn_ids
                else:
                    prev_turn = tokenizer.apply_chat_template(
                        messages[:i], 
                        tokenize=False
                    )
                    prev_ids = tokenizer(prev_turn).input_ids
                    prev_len = len(prev_ids)
                    turn_ids = tokenizer(single_turn).input_ids
                    new_tokens = turn_ids[prev_len:]
                
                full_ids.extend(new_tokens)

                # get the first assistant idx
                first_assistant_idx = next((idx for idx, msg in enumerate(messages) if msg.get("role") == "assistant"), None)
                
                # Only compute loss on assistant responses
                if msg["role"] == "assistant":
                    if first_assistant_idx is not None and i == first_assistant_idx:
                        # do not include first assistant turn in loss
                        loss_mask.extend([0.0] * len(new_tokens))
                    else:
                        loss_mask.extend([1.0] * len(new_tokens))
                else:
                    loss_mask.extend([0.0] * len(new_tokens))
            
            # Debug: verify mask distribution (remove after testing)
            if len(data) == 0:  # Just log the first example
                assistant_tokens = sum(loss_mask)
                total_tokens = len(loss_mask)
                print(f"First example: {assistant_tokens}/{total_tokens} tokens are assistant ({100*assistant_tokens/total_tokens:.1f}%)")

                # Verify <think> tags are being handled correctly
                decoded = tokenizer.decode(full_ids)
                if "<think>" in decoded:
                    print("Note: <think> tags ARE included in loss computation")

            data.append({
                "input_ids": np.array(full_ids),
                "loss_mask": np.array(loss_mask, dtype=np.float32)
            })
            
        elif "text" in entry:
            token_ids = tokenizer(entry["text"]).input_ids
            data.append({
                "input_ids": np.array(token_ids),
                "loss_mask": np.ones(len(token_ids), dtype=np.float32)
            })
            
    return data

def create_batch(data, batch_size):
    # Guard against batch_size > dataset size
    actual_batch_size = min(batch_size, len(data))
    
    # Randomly sample indices
    indices = np.random.choice(len(data), actual_batch_size, replace=False)
    batch = [data[i] for i in indices]
    
    # Pad to the longest sequence in this mini-batch
    actual_max_len = max(len(x["input_ids"]) for x in batch)

    # Implement bucket padding for efficiency
    pad_to_len = ((actual_max_len + 255) // 256) * 256
    
    # Initialize arrays
    input_ids = np.zeros((actual_batch_size, pad_to_len), dtype=np.int32)
    # Loss mask: 1 only for assistant tokens, 0 for user/system/padding
    loss_mask = np.zeros((actual_batch_size, pad_to_len), dtype=np.float32)
    
    for i, item in enumerate(batch):
        seq = item["input_ids"]
        seq_loss_mask = item["loss_mask"]
        L = len(seq)
        input_ids[i, :L] = seq
        loss_mask[i, :L] = seq_loss_mask
        
    return mx.array(input_ids), mx.array(loss_mask)

def evaluate(model, dataset, eval_step_fn, batch_size=4):
    model.eval()
    total_loss = 0
    count = 0
    
    # We loop through the VALIDATION set
    # (Simplified loop: just grabbing random batches or iterating once)
    # For speed, let's just test on 50 random batches
    for _ in range(50): 
        input_ids, loss_mask = create_batch(dataset, batch_size)
        # We use a 'no_grad' equivalent context if available, 
        # but MLX handles inference efficiently by just not asking for grads.
        loss = eval_step_fn(input_ids, loss_mask)
        total_loss += loss.item()
        count += 1
    
    model.train() # Switch back to training mode
    return total_loss / count

def loss_fn(model, input_ids, loss_mask):
    # Forward pass: get logits
    logits = model(input_ids)
    
    # Shift targets: We predict the NEXT token
    # Logits: [Batch, Seq-1, Vocab]
    # Targets: [Batch, Seq-1] (shifted by 1)
    logits = logits[:, :-1, :]
    targets = input_ids[:, 1:]
    loss_mask = loss_mask[:, 1:] # Shift mask too
    
    # Calculate Cross Entropy
    # reduction='none' so we can apply our custom loss mask (only assistant tokens)
    losses = nn.losses.cross_entropy(logits, targets, reduction='none')
    
    # Apply mask and average (loss_mask is 1 only for assistant tokens, 0 elsewhere)
    losses = losses * loss_mask
    # Avoid division by zero if no assistant tokens in batch
    mask_sum = loss_mask.sum()
    loss = mx.where(mask_sum > 0, losses.sum() / mask_sum, mx.array(0.0))

    return loss

def main():
    # 1. Load the Model & Tokenizer
    print("Loading model...")
    model, _ = load(MODEL_PATH)

    # load tokenizer with AutoTokenizer for from HF
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    
    # 2. Freeze Base Model & Add LoRA
    print("Applying LoRA adapters...")
    model.freeze()
    linear_to_lora_layers(model, num_layers=len(model.layers), config=LORA_CONFIG)

    # safety check to ensure LoRA layers are trainable
    trainable_names = [k for k, _ in tree_flatten(model.trainable_parameters())]
    print(f"Trainable params after LoRA: {len(trainable_names)}")
    if len(trainable_names) == 0:
        # print all layers if this happens for key inspection
        print(model)
        raise RuntimeError(
            "LoRA produced 0 trainables. Verify LORA_CONFIG['keys'] match the model module names."
        )

    # 3. Load Data (Using our custom function that fixes the bug)
    train_data = load_and_tokenize("train.jsonl", tokenizer)
    valid_data = load_and_tokenize("valid.jsonl", tokenizer)

    # 4. Create the Optimizer
    print("Starting training...")
    optimizer = optim.AdamW(learning_rate=LEARNING_RATE, weight_decay=WEIGHT_DECAY)
    
    # 5. Create Training Step Function
    # mlx.value_and_grad returns a function that computes both loss and gradients
    training_step = nn.value_and_grad(model, loss_fn)
    
    # 6. Training Loop
    print(f"Starting training for {ITERS} iterations...")
    start_time = time.time()
    
    state = [model.state, optimizer.state]

    @partial(mx.compile, inputs=state, outputs=state)
    def step(inputs, mask):
        loss, grads = training_step(model, inputs, mask)
        optimizer.update(model, grads)
        return loss
    
    eval_state = [model.state]

    @partial(mx.compile, inputs=eval_state)
    def eval_step(inputs, mask):
        return loss_fn(model, inputs, mask)

    for i in tqdm(range(ITERS)):
        # A. Create Batch
        input_ids, loss_mask = create_batch(train_data, BATCH_SIZE)
        
        # # B. Compute Loss and Gradients (use loss_mask which covers assistant tokens only)
        # loss, grads = training_step(model, input_ids, loss_mask)
        
        # # C. Update Model Weights
        # optimizer.update(model, grads)
        loss = step(input_ids, loss_mask)
        
        # D. Evaluate (Force computation)
        # In MLX, computation is lazy. mx.eval forces it to happen now.
        mx.eval(state, loss)
        
        # E. Reporting (training)
        if (i + 1) % REPORT_EVERY == 0:
            elapsed = time.time() - start_time
            print(f"Iter {i+1}/{ITERS} | Loss: {loss.item():.4f} | Time: {elapsed:.2f}s")
            start_time = time.time() # Reset timer for accurate speed/iter

        # F. Validation
        if (i + 1) % VAL_RATE == 0:
            # Check against data the model hasn't seen
            val_loss = evaluate(model, valid_data, eval_step)

            trainable_params = dict(tree_flatten(model.trainable_parameters()))
    
            # 2. Save weights
            mx.save_safetensors(f"{ADAPTER_FILE}_val_{i+1}.safetensors", trainable_params)

            print(f"Iter {i+1} | Train Loss: {loss.item():.4f} | Val Loss: {val_loss:.4f}")
            
    # 7. Save Adapters
    print(f"Saving adapters to {ADAPTER_FILE}...")
    save_lora_manually(model, f"{ADAPTER_FILE}_final.safetensors", LORA_CONFIG_FILE)
    print("Done.")

if __name__ == "__main__":
    main()