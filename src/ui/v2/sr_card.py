import customtkinter as ctk

from src.theme_v2 import *


def create_sr_card(parent):

    card = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=RADIUS,
        border_width=1,
        border_color=BORDER
    )

    return card, {
        "rank": rank_label,
        "icon": rank_icon,
        "sr": sr_value,
        "progress": progress,
        "goal": goal_entry,
        "win": win_button,
        "loss": loss_button,
    }

    # ==========================
    # Rang
    # ==========================

    rank_label = ctk.CTkLabel(
        card,
        text="CRIMSON I",
        font=("Segoe UI", 18, "bold")
    )

    rank_label.pack(pady=(25, 10))

    # ==========================
    # Icône
    # ==========================

    rank_icon = ctk.CTkLabel(
        card,
        text="🏆",
        font=("Segoe UI Emoji", 72)
    )

    rank_icon.pack()

    # ==========================
    # SR
    # ==========================

    sr_value = ctk.CTkLabel(
        card,
        text="9300",
        font=("Segoe UI", 42, "bold")
    )

    sr_value.pack(pady=(15, 0))

    sr_text = ctk.CTkLabel(
        card,
        text="Skill Rating",
        font=LABEL_FONT,
        text_color=TEXT_SECONDARY
    )

    sr_text.pack()

    # ==========================
    # Barre de progression
    # ==========================

    progress = ctk.CTkProgressBar(
        card,
        width=300,
        progress_color=PRIMARY
    )

    progress.set(0.65)

    progress.pack(pady=(30, 10))

    progress_label = ctk.CTkLabel(
        card,
        text="65% vers Crimson II",
        font=LABEL_FONT,
        text_color=TEXT_SECONDARY
    )

    progress_label.pack()

    # ==========================
    # Objectif
    # ==========================

    goal_title = ctk.CTkLabel(
        card,
        text="Objectif",
        font=SUBTITLE_FONT
    )

    goal_title.pack(pady=(30, 10))

    goal_entry = ctk.CTkEntry(
        card,
        width=220,
        height=40,
        placeholder_text="10000"
    )

    goal_entry.pack()

    # ==========================
    # Boutons
    # ==========================

    buttons = ctk.CTkFrame(
        card,
        fg_color="transparent"
    )

    buttons.pack(pady=30)

    win_button = ctk.CTkButton(
        buttons,
        text="🟢 Victoire",
        width=150,
        height=45,
        fg_color=SUCCESS,
        hover_color="#2bbf85"
    )

    win_button.grid(row=0, column=0, padx=8)

    loss_button = ctk.CTkButton(
        buttons,
        text="🔴 Défaite",
        width=150,
        height=45,
        fg_color=DANGER,
        hover_color="#e05252"
    )

    loss_button.grid(row=0, column=1, padx=8)

    return {
        "frame": card,
        "rank": rank_label,
        "icon": rank_icon,
        "sr": sr_value,
        "progress": progress,
        "goal": goal_entry,
        "win": win_button,
        "loss": loss_button,
    }