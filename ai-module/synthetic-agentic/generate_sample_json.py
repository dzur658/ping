import json

def generate_json_output(obj):
    print(obj)
    with open('sample.jsonl', 'w') as f:
        for item in obj:
            f.write(json.dumps(item) + '\n')