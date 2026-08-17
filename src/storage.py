import json
import os
import sys

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SAVE_FILE = os.path.join(BASE_DIR, "data", "session.json")


def save_session(session):
    os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)

    data = {
        "current_sr": session.current_sr,
        "goal": session.goal,
        "session_sr": session.session_sr,
        "wins": session.wins,
        "losses": session.losses,
        "winstreak": session.winstreak,
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_session(session):
    if not os.path.exists(SAVE_FILE):
        return

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    session.current_sr = data["current_sr"]
    session.goal = data["goal"]
    session.session_sr = data["session_sr"]
    session.wins = data["wins"]
    session.losses = data["losses"]
    session.winstreak = data["winstreak"]


def save_overlay(session):
    import json
    import os
    import sys

    if getattr(sys, "frozen", False):
        BASE_DIR = os.path.dirname(sys.executable)
    else:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    OVERLAY_FILE = os.path.join(BASE_DIR, "overlay", "overlay_data.json")

    os.makedirs(os.path.dirname(OVERLAY_FILE), exist_ok=True)

    data = {
        "player": "AXIIIOMTV",
        "rank": "CRIMSON II",
        "current_sr": session.current_sr,
        "goal": session.goal,
        "session_sr": session.session_sr,
        "wins": session.wins,
        "losses": session.losses,
        "winstreak": session.winstreak,
    }

    with open(OVERLAY_FILE, "w") as f:
        json.dump(data, f, indent=4)