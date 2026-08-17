import customtkinter as ctk
from PIL import Image
from src.ranks import get_rank
from src.theme import (
    CARD,
    PRIMARY,
    FONT_TITLE,
    FONT_HUGE,
    FONT_TEXT,
    FONT_BODY,
    FONT_SMALL,
    TEXT,
)
from src.utils.resource_path import resource_path

def create_session_card(parent, border, new_session, session):

    stats = ctk.CTkFrame(
        parent,
        fg_color="#25282E",
        corner_radius=18,
        border_width=1,
        border_color=border
    )

    stats.pack(
        side="right",
        fill="both",
        expand=True,
        padx=10
    )

    ctk.CTkLabel(
        stats,
        text="📊 Session",
        font=("Arial", 24, "bold")
    ).pack(pady=20)

    session_label = ctk.CTkLabel(
    stats,
    text=f"📈 {session.session_sr:+} SR",
    font=("Arial", 18)
    )

    session_label.pack(pady=8)

    wins_label = ctk.CTkLabel(
        stats,
        text=f"✅ {session.wins} Victoire(s)",
        font=("Arial", 18)
    )

    wins_label.pack(pady=8)

    losses_label = ctk.CTkLabel(
        stats,
        text=f"❌ {session.losses} Défaite(s)",
        font=("Arial", 18)
    )

    losses_label.pack(pady=8)

    streak_label = ctk.CTkLabel(
        stats,
        text=f"🔥 Winstreak : {session.winstreak}",
        font=("Arial", 18)
    )

    streak_label.pack(pady=8)

    winrate_label = ctk.CTkLabel(
        stats,
        text="📊 Winrate : 0.0%",
        font=("Arial", 18)
    )

    winrate_label.pack(pady=8)

    ctk.CTkButton(
        stats,
        text="🗘 Nouvelle session",
        command=new_session
    ).pack(pady=25) 

    return {
        "frame": stats,
        "session_label": session_label,
        "wins_label": wins_label,
        "losses_label": losses_label,
        "streak_label": streak_label,
        "winrate_label": winrate_label,
    }

def create_history_card(parent, border):

    history_frame = ctk.CTkFrame(
        parent,
        fg_color="#25282E",
        corner_radius=18,
        border_width=1,
        border_color=border
    )

    history_frame.pack(
        side="right",
        fill="both",
        expand=True,
        padx=10
    )

    ctk.CTkLabel(
        history_frame,
        text="📋 Historique",
        font=("Arial", 24, "bold")
    ).pack(pady=20)

    return history_frame

def create_sr_card(parent, session):

    sr_frame = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=18,
        border_width=1,
        border_color="#31343B"
    )

    sr_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10
    )

    ctk.CTkFrame(
        sr_frame,
        height=2,
        fg_color=PRIMARY,
        corner_radius=1
    ).pack(fill="x", padx=40, pady=(0,20))

    rank_label = ctk.CTkLabel(
    sr_frame,
    text="",
    font=FONT_TITLE,
    text_color=TEXT
    )

    rank_label.pack(pady=5)

    rank = get_rank(session.current_sr)

    rank_image = ctk.CTkImage(
        light_image=Image.open(resource_path(rank["image"])),
        dark_image=Image.open(resource_path(rank["image"])),
        size=(90, 90)
    )

    rank_icon = ctk.CTkLabel(
        sr_frame,
        image=rank_image,
        text=""
    )

    rank_icon.image = rank_image
    rank_icon.pack(pady=10)

    sr_value = ctk.CTkLabel(
        sr_frame,
        text=f"{session.current_sr} SR",
        font=FONT_HUGE
    )

    sr_value.pack(pady=10)

    next_rank_label = ctk.CTkLabel(
        sr_frame,
        text="",
        font=FONT_TEXT
    )

    next_rank_label.pack(pady=(10, 2))

    remaining_label = ctk.CTkLabel(
        sr_frame,
        text="",
        font=FONT_BODY
    )

    remaining_label.pack(pady=(0, 15))

    rank_progress = ctk.CTkProgressBar(
        sr_frame,
        width=250
    )

    rank_progress.pack(pady=(5, 15))

    rank_progress_label = ctk.CTkLabel(
        sr_frame,
        text="",
        font=FONT_SMALL
    )

    rank_progress_label.pack()

    goal_remaining_label = ctk.CTkLabel(
        sr_frame,
        text="",
        font=("Arial", 14)
    )

    goal_remaining_label.pack(pady=(5, 15))

    ctk.CTkLabel(
        sr_frame,
        text="🎯 Objectif",
        font=("Arial", 22)
    ).pack(pady=20)

    goal_entry = ctk.CTkEntry(
        sr_frame,
        width=200,
        justify="center"
    )

    goal_entry.insert(0, str(session.goal))
    goal_entry.pack()

    progress = ctk.CTkProgressBar(
        sr_frame,
        width=250
    )

    progress.pack(pady=20)

    progress_label = ctk.CTkLabel(
        sr_frame,
        text="0%",
        font=("Arial", 16)
    )

    progress_label.pack()

    buttons = ctk.CTkFrame(
    sr_frame,
    fg_color="transparent"
    )

    buttons.pack(pady=30)

    win_button = ctk.CTkButton(
        buttons,
        text="🟢 VICTOIRE",
        width=220,
        height=55,
        corner_radius=12,
        command=None
    )

    win_button.grid(row=0, column=0, padx=10)

    loss_button = ctk.CTkButton(
        buttons,
        text="🔴 DÉFAITE",
        width=220,
        height=55,
        corner_radius=12,
        command=None
    )

    loss_button.grid(row=0, column=1, padx=10)

    return {
        "frame": sr_frame,
        "rank_icon": rank_icon,
        "rank_label": rank_label,
        "sr_value": sr_value,
        "next_rank_label": next_rank_label,
        "remaining_label": remaining_label,
        "rank_progress": rank_progress,
        "rank_progress_label": rank_progress_label,
        "goal_entry": goal_entry,
        "progress": progress,
        "progress_label": progress_label,
        "goal_remaining_label": goal_remaining_label,
        "win_button": win_button,
        "loss_button": loss_button,
    }

def update_sr_rank_icon(rank_icon, current_sr):

    rank = get_rank(current_sr)

    rank_image = ctk.CTkImage(
        light_image=Image.open(resource_path(rank["image"])),
        dark_image=Image.open(resource_path(rank["image"])),
        size=(90, 90)
    )

    rank_icon.configure(image=rank_image)
    rank_icon.image = rank_image
