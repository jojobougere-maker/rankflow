import json
import os
from datetime import datetime

HISTORY_FILE = "data/history.json"


def save_match(result, sr_change, current_sr):

    os.makedirs("data", exist_ok=True)

    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)

    history.append({
        "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "result": result,
        "sr_change": sr_change,
        "current_sr": current_sr
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def clear_history():

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)