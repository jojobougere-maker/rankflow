import os
import sys
from pathlib import Path

import customtkinter as ctk
from customtkinter import CTkProgressBar
from PIL import Image

from src.history import save_match, load_history, clear_history
from src.logic import ask_sr_change
from src.ranks import get_rank, get_division
from src.session import Session
from src.settings import load_settings, save_settings
from src.storage import save_session, load_session, save_overlay
from src.theme import *
from src.ui.dialogs import open_settings
from src.ui.cards import (
    create_session_card,
    create_history_card,
    create_sr_card,
    update_sr_rank_icon,
)
from src.ui.header import create_header
from src.ui.dashboard import create_dashboard_card
    
# ==================================================
# UTILITAIRES
# ==================================================

def resource_path(relative_path):
    """Retourne le bon chemin, même après compilation."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

BASE_DIR = Path(__file__).resolve().parent

# ==================================================
# CHARGEMENT DES DONNÉES
# ==================================================

session = Session()
load_session(session)
settings = load_settings()
session.rank = get_rank(session.current_sr)["name"]

# -----------------------
# Configuration
# -----------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# -----------------------
# Fenêtre
# -----------------------
app = ctk.CTk()

app.iconbitmap(resource_path("assets/ranks/logo.ico"))

app.title("RankFlow")
app.minsize(1200, 700)
app.geometry("1400x800")

logo_image = ctk.CTkImage(
    light_image=Image.open(resource_path("assets/ranks/logo.png")),
    dark_image=Image.open(resource_path("assets/ranks/logo.png")),
    size=(56, 56)
)

popup_frame = ctk.CTkFrame(
    app,
    width=180,
    height=55,
    fg_color=CARD,
    border_width=2,
    border_color=PRIMARY,
    corner_radius=14
)

popup_text = ctk.CTkLabel(
    popup_frame,
    text="",
    font=("Segoe UI", 22, "bold")
)

popup_text.pack(expand=True)

popup_frame.place(relx=0.5, rely=0.18, anchor="center")
popup_frame.place_forget()

header_widgets = create_header(
    app,
    logo_image,
    settings,
)

header_session_title = header_widgets["session_title"]
header_wins_label = header_widgets["wins_label"]
header_loss_label = header_widgets["loss_label"]
header_winrate_label = header_widgets["winrate_label"]
header_streak_label = header_widgets["streak_label"]
player_label = header_widgets["player_label"]

# -----------------------
# Contenu principal
# -----------------------
content = ctk.CTkFrame(app)
content.pack(fill="both", expand=True, padx=24, pady=24)

# Carte SR
sr_widgets = create_sr_card(
    content,
    session
)

sr_frame = sr_widgets["frame"]

rank_icon = sr_widgets["rank_icon"]
rank_label = sr_widgets["rank_label"]
sr_value = sr_widgets["sr_value"]

next_rank_label = sr_widgets["next_rank_label"]
remaining_label = sr_widgets["remaining_label"]

rank_progress = sr_widgets["rank_progress"]
rank_progress_label = sr_widgets["rank_progress_label"]

goal_entry = sr_widgets["goal_entry"]
progress = sr_widgets["progress"]
progress_label = sr_widgets["progress_label"]
goal_remaining_label = sr_widgets["goal_remaining_label"]
win_button = sr_widgets["win_button"]
loss_button = sr_widgets["loss_button"]

def refresh_header():

    player_label.configure(
        text=settings["player"]
    )

    header_session_title.configure(
        text=f"{session.session_sr:+} SR",
        text_color="#22C55E" if session.session_sr >= 0 else "#EF4444"
    )

    header_wins_label.configure(
        text=f"🟢 {session.wins} W"
    )

    header_loss_label.configure(
        text=f"🔴 {session.losses} L"
    )

    games = session.wins + session.losses

    winrate = (session.wins / games * 100) if games else 0

    header_winrate_label.configure(
        text=f"📊 {winrate:.1f} %"
    )

    header_streak_label.configure(
        text=f"🔥 x{session.winstreak}"
    )

def refresh_sr_card():

    rank = get_rank(session.current_sr)

    rank_min = rank["min"]
    rank_max = rank["max"]

    rank_progress_value = (session.current_sr - rank_min) / (rank_max - rank_min)
    rank_progress_value = max(0, min(rank_progress_value, 1))

    rank_progress.set(rank_progress_value)

    rank_progress_label.configure(
        text=f"{rank_progress_value * 100:.1f}% du rang"
    )

    if rank["next"] is None:

        next_rank_label.configure(
            text="👑 Rang maximum"
        )

        remaining_label.configure(
            text=""
        )

    else:

        remaining = rank["max"] - session.current_sr

        next_rank_label.configure(
            text=f"🎯 {rank['next']}"
        )

        remaining_label.configure(
            text=f"📈 Encore {remaining} SR"
        )

    update_sr_rank_icon(
        rank_icon,
        session.current_sr
    )

    division = get_division(session.current_sr)

    if division:
        rank_label.configure(
            text=f"{rank['name']} {division}"
        )
    else:
        rank_label.configure(
            text=rank["name"]
        )

    sr_value.configure(
        text=f"{session.current_sr} SR"
    )

def refresh_session_card():

    session_label.configure(
        text=f"📈 {session.session_sr:+} SR"
    )

    wins_label.configure(
        text=f"✅ {session.wins} Victoire(s)"
    )

    losses_label.configure(
        text=f"❌ {session.losses} Défaite(s)"
    )

    streak_label.configure(
        text=f"🔥 Winstreak : {session.winstreak}"
    )

    games = session.wins + session.losses

    if games > 0:
        winrate = (session.wins / games) * 100
    else:
        winrate = 0

    winrate_label.configure(
        text=f"📊 Winrate : {winrate:.1f}%"
    )

def refresh_goal():

    goal_entry.delete(0, "end")
    goal_entry.insert(0, str(session.goal))

    goal = session.goal

    if goal > 0:
        goal_progress = session.current_sr / goal
        goal_progress = max(0, min(goal_progress, 1))
        progress.set(goal_progress)

    remaining = max(0, session.goal - session.current_sr)

    if remaining == 0:
        progress_label.configure(
            text="🏆 Objectif atteint !"
        )
    else:
        progress_label.configure(
            text=f"📍 Plus que {remaining} SR"
        )

    goal_remaining_label.configure(
        text=f"Objectif : {session.goal} SR"
    )

def refresh_dashboard():

    dashboard_session_sr.configure(
        text=f"{session.session_sr:+} SR"
    )

    dashboard_current_sr.configure(
        text=f"{session.current_sr} SR"
    )

    dashboard_wins.configure(
        text=str(session.wins)
    )

    dashboard_losses.configure(
        text=str(session.losses)
    )

    games = session.wins + session.losses

    if games:
        winrate = session.wins / games * 100
    else:
        winrate = 0

    dashboard_winrate.configure(
        text=f"{winrate:.1f}%"
    )

    dashboard_streak.configure(
        text=str(session.winstreak)
    )

    dashboard_games.configure(
        text=str(games)
    )

    dashboard_avg_win.configure(
        text="À venir"
    )

    dashboard_avg_loss.configure(
        text="À venir"
    )

def refresh_ui():

    refresh_header()
    refresh_sr_card()
    refresh_session_card()
    refresh_goal()
    refresh_dashboard()
    refresh_history()

def refresh_history():

    history_box.delete("1.0", "end")

    history = load_history()

    for match in history[-10:]:

        icon = "🟢" if match["result"] == "WIN" else "🔴"

        history_box.insert(
            "end",
            f"{icon} {match['result']}   "
            f"{match['sr_change']:+} SR   "
            f"{match['current_sr']} SR\n"
        )

def show_popup(text, color):

    popup_text.configure(
        text=text,
        text_color=color
    )

    popup_frame.place(
        relx=0.5,
        rely=0.18,
        anchor="center"
    )

    popup_frame.lift()

    app.after(
        1000,
        popup_frame.place_forget
    )

def win():

    sr = ask_sr_change("Victoire")

    if sr is None:
        return

    old_rank = get_rank(session.current_sr)["name"] 
    session.current_sr += sr
    new_rank = get_rank(session.current_sr)["name"]
    session.session_sr += sr
    show_popup(f"+{sr} SR", "#32CD32")

    if old_rank != new_rank:
        app.after(
        1300,
        lambda: show_popup(f"🏆 PROMOTION\n{new_rank}", "#FFD700")
    )

    session.wins += 1
    session.winstreak += 1

    save_session(session)

    save_overlay(session)

    save_match(
    "WIN",
    sr,
    session.current_sr
)
    refresh_ui()

def loss():
    sr = ask_sr_change("Défaite")

    if sr is None:
        return

    session.current_sr -= sr
    session.session_sr -= sr
    show_popup(f"-{sr} SR", "#FF4C4C")
    session.losses += 1
    session.winstreak = 0

    save_session(session)
    save_overlay(session)

    save_match(
    "LOSS",
    -sr,
    session.current_sr
)

    refresh_ui()

def reset_session():

    session.session_sr = 0
    session.wins = 0
    session.losses = 0
    session.winstreak = 0

    clear_history()

    save_session(session)
    save_overlay(session)

    refresh_ui()

win_button.configure(command=win)
loss_button.configure(command=loss)

header_widgets["settings_button"].configure(
    command=lambda: open_settings(
        app,
        session,
        settings,
        refresh_ui
    )
)

# Carte statistiques
session_widgets = create_session_card(
    content,
    BORDER,
    reset_session,
    session
)

stats = session_widgets["frame"]
session_label = session_widgets["session_label"]
wins_label = session_widgets["wins_label"]
losses_label = session_widgets["losses_label"]
streak_label = session_widgets["streak_label"]
winrate_label = session_widgets["winrate_label"]

history_frame = create_history_card(
    content,
    BORDER
)

history_box = ctk.CTkTextbox(
    history_frame,
    width=350,
    height=450
)

history_box.pack(padx=20, pady=20)

dashboard_widgets = create_dashboard_card(content)

dashboard_session_sr = dashboard_widgets["session_sr"]
dashboard_current_sr = dashboard_widgets["current_sr"]
dashboard_wins = dashboard_widgets["wins"]
dashboard_losses = dashboard_widgets["losses"]
dashboard_winrate = dashboard_widgets["winrate"]
dashboard_streak = dashboard_widgets["streak"]
dashboard_games = dashboard_widgets["games"]
dashboard_avg_win = dashboard_widgets["avg_win"]
dashboard_avg_loss = dashboard_widgets["avg_loss"]

widgets = {
    # Header
    "player_label": player_label,
    "header_session_title": header_session_title,
    "header_wins_label": header_wins_label,
    "header_loss_label": header_loss_label,
    "header_winrate_label": header_winrate_label,
    "header_streak_label": header_streak_label,

    # SR Card
    "rank_icon": rank_icon,
    "rank_label": rank_label,
    "sr_value": sr_value,
    "next_rank_label": next_rank_label,
    "remaining_label": remaining_label,
    "rank_progress": rank_progress,
    "rank_progress_label": rank_progress_label,

    # Goal
    "goal_entry": goal_entry,
    "progress": progress,
    "progress_label": progress_label,
    "goal_remaining_label": goal_remaining_label,

    # Session
    "session_label": session_label,
    "wins_label": wins_label,
    "losses_label": losses_label,
    "streak_label": streak_label,
    "winrate_label": winrate_label,

    # History
    "history_box": history_box,
}

refresh_ui()
refresh_history()

# ==================================================
# LANCEMENT
# ==================================================

app.mainloop()