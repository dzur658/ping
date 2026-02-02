import random
import os

# --- Configuration ---
INPUT_FILE = "./synthetic-data/master_wrapped.jsonl"
TRAIN_FILE = "./synthetic-data/mlx-wrapped-datasets/train.jsonl"
VALID_FILE = "./synthetic-data/mlx-wrapped-datasets/valid.jsonl"
TEST_FILE = "./synthetic-data/mlx-wrapped-datasets/test.jsonl"

TRAIN_RATIO = 0.85
VALID_RATIO = 0.10
# Test ratio is the remaining (0.05)

SEED = 42  # Set seed for reproducibility

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    print(f"Reading {INPUT_FILE}...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        # Read all lines into memory (efficient enough for <1M lines)
        lines = f.readlines()

    # Remove empty lines if any
    lines = [line for line in lines if line.strip()]
    
    total_lines = len(lines)
    print(f"Total examples found: {total_lines}")

    # Shuffle data randomly
    random.seed(SEED)
    random.shuffle(lines)

    # Calculate split indices
    train_end = int(total_lines * TRAIN_RATIO)
    valid_end = train_end + int(total_lines * VALID_RATIO)

    # Slice the data
    train_data = lines[:train_end]
    valid_data = lines[train_end:valid_end]
    test_data = lines[valid_end:]

    # Write to files
    print(f"Writing {len(train_data)} examples to {TRAIN_FILE}...")
    with open(TRAIN_FILE, 'w', encoding='utf-8') as f:
        f.writelines(train_data)

    print(f"Writing {len(valid_data)} examples to {VALID_FILE}...")
    with open(VALID_FILE, 'w', encoding='utf-8') as f:
        f.writelines(valid_data)

    print(f"Writing {len(test_data)} examples to {TEST_FILE}...")
    with open(TEST_FILE, 'w', encoding='utf-8') as f:
        f.writelines(test_data)

    print("\nDone! Split stats:")
    print(f"Train: {len(train_data) / total_lines:.1%}")
    print(f"Valid: {len(valid_data) / total_lines:.1%}")
    print(f"Test:  {len(test_data) / total_lines:.1%}")

if __name__ == "__main__":
    main()