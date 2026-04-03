1. Run the following MLX LM command
```bash
mlx_lm.fuse --model Qwen/Qwen3-1.7B --save-path fused/ping_technical_support --adapter-path ./adapters
```

2. Due to llama.cpp version mismatches, tokenizer config files must be copied from the original model's huggingface format directory
- `tokenizer_config.json`
- `tokenizer.json`
- `vocab.json`
- `merges.txt`

3. Run the HF to GGUF conversion script from llama.cpp
```bash
python convert_hf_to_gguf.py [SAFETENSORS DIRECTORY] --outfile [OUTPUT PATH] --outtype f16
```