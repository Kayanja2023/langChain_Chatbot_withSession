import json
from pathlib import Path

DATA_PATH = Path("data/history_logs.json")

def load_long_chat_history():
    if DATA_PATH.exists():
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    return []

def save_long_chat_history(history):
    with open(DATA_PATH, "w") as f:
        json.dump(history, f, indent=2)
