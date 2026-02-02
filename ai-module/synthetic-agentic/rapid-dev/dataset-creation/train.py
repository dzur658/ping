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
DATA_DIR = "./synthetic-data/mlx-wrapped-datasets"
ADAPTER_FILE = "./adapters/adapter_model"
LORA_CONFIG_FILE = "./adapters/adapter_config.json"
LEARNING_RATE = 1e-5
ITERS = 2000
BATCH_SIZE = 8
REPORT_EVERY = 50
VAL_RATE = 100
WEIGHT_DECAY = 0.01
# ---------------------

# LoRA Hyperparameters
LORA_CONFIG = {
    "rank": 32,
    "scale": 64,
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
            "num_layers": 8, # Must match num_lora_layers used in training
            
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
            # Apply chat template
            text = tokenizer.apply_chat_template(entry["messages"], tokenize=False)
            
            # THE FIX: Explicitly extract input_ids to prevent the Encoding Object crash
            # We convert to a numpy array immediately so MLX is happy
            token_ids = tokenizer(text).input_ids
            data.append(np.array(token_ids))
            
        elif "text" in entry:
            token_ids = tokenizer(entry["text"]).input_ids
            data.append(np.array(token_ids))
            
    return data

def create_batch(data, batch_size, tokenizer):
    # Randomly sample indices
    indices = np.random.choice(len(data), batch_size, replace=False)
    batch = [data[i] for i in indices]
    
    # Pad to the longest sequence in this mini-batch
    max_len = max(len(x) for x in batch)
    
    # Initialize arrays
    input_ids = np.zeros((batch_size, max_len), dtype=np.int32)
    # Using a simple mask: 1 where data exists, 0 where padding
    mask = np.zeros((batch_size, max_len), dtype=np.float32)
    
    for i, seq in enumerate(batch):
        L = len(seq)
        input_ids[i, :L] = seq
        mask[i, :L] = 1.0
        
    return mx.array(input_ids), mx.array(mask)

def evaluate(model, dataset, tokenizer, batch_size=4):
    model.eval()
    total_loss = 0
    count = 0
    
    # We loop through the VALIDATION set
    # (Simplified loop: just grabbing random batches or iterating once)
    # For speed, let's just test on 50 random batches
    for _ in range(50): 
        input_ids, mask = create_batch(dataset, batch_size, tokenizer)
        # We use a 'no_grad' equivalent context if available, 
        # but MLX handles inference efficiently by just not asking for grads.
        loss = loss_fn(model, input_ids, mask)
        total_loss += loss.item()
        count += 1
    
    model.train() # Switch back to training mode
    return total_loss / count

def loss_fn(model, input_ids, mask):
    # Forward pass: get logits
    logits = model(input_ids)
    
    # Shift targets: We predict the NEXT token
    # Logits: [Batch, Seq-1, Vocab]
    # Targets: [Batch, Seq-1] (shifted by 1)
    logits = logits[:, :-1, :]
    targets = input_ids[:, 1:]
    mask = mask[:, 1:] # Shift mask too
    
    # Calculate Cross Entropy
    # reduction='none' so we can apply our custom padding mask
    losses = nn.losses.cross_entropy(logits, targets, reduction='none')
    
    # Apply mask and average
    losses = losses * mask
    loss = losses.sum() / mask.sum()

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
    linear_to_lora_layers(model, num_layers=8, config=LORA_CONFIG)

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

    for i in tqdm(range(ITERS)):
        # A. Create Batch
        input_ids, mask = create_batch(train_data, BATCH_SIZE, tokenizer)
        
        # B. Compute Loss and Gradients
        loss, grads = training_step(model, input_ids, mask)
        
        # C. Update Model Weights
        optimizer.update(model, grads)
        
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
            val_loss = evaluate(model, valid_data, tokenizer)

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