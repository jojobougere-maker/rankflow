import json
import os

SETTINGS_FILE = "data/settings.json"

DEFAULT_SETTINGS = {
    "player": "AXIIIOMTV",
    "goal": 10000,
    "sounds": True,
    "animations": True
}


def load_settings():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(SETTINGS_FILE):

        save_settings(DEFAULT_SETTINGS)

    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:

        return json.load(f)


def save_settings(settings):

    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:

        json.dump(settings, f, indent=4)