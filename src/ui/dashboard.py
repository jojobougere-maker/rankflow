import customtkinter as ctk

from src.theme import *


def create_dashboard_card(parent):

    frame = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=18,
        border_width=2,
        border_color=BORDER
    )

    frame.pack(side="right", fill="both", padx=20, pady=20)

    title = ctk.CTkLabel(
        frame,
        text="📊 Dashboard",
        font=("Segoe UI", 24, "bold")
    )

    title.pack(pady=(20, 25))

    stats = {}

    labels = [
        ("session_sr", "📈 Session"),
        ("current_sr", "🎯 SR actuel"),
        ("wins", "🟢 Victoires"),
        ("losses", "🔴 Défaites"),
        ("winrate", "📊 Winrate"),
        ("streak", "🔥 Winstreak"),
        ("games", "⚔️ Parties"),
        ("avg_win", "📈 Moy. victoire"),
        ("avg_loss", "📉 Moy. défaite"),
    ]

    for key, text in labels:

        row = ctk.CTkFrame(frame, fg_color="transparent")
        row.pack(fill="x", padx=20, pady=5)

        ctk.CTkLabel(
            row,
            text=text,
            font=("Segoe UI", 16)
        ).pack(side="left")

        value = ctk.CTkLabel(
            row,
            text="--",
            font=("Segoe UI", 16, "bold")
        )

        value.pack(side="right")

        stats[key] = value

    return {
        "frame": frame,
        **stats
    }