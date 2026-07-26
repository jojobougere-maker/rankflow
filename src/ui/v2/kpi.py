import customtkinter as ctk

from src.theme_v2 import *


def create_kpi_card(parent, icon, title, value):

    card = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=RADIUS,
        border_width=1,
        border_color=BORDER
    )

    icon_label = ctk.CTkLabel(
        card,
        text=icon,
        font=("Segoe UI Emoji", 26)
    )
    icon_label.pack(anchor="nw", padx=20, pady=(18, 0))

    value_label = ctk.CTkLabel(
        card,
        text=value,
        font=VALUE_FONT
    )
    value_label.pack(anchor="w", padx=20, pady=(8, 0))

    title_label = ctk.CTkLabel(
        card,
        text=title,
        font=LABEL_FONT,
        text_color=TEXT_SECONDARY
    )
    title_label.pack(anchor="w", padx=20, pady=(0, 18))

    return {
        "frame": card,
        "value": value_label,
        "title": title_label,
        "icon": icon_label
    }


def create_kpi_grid(parent):

    parent.grid_columnconfigure(0, weight=1)
    parent.grid_columnconfigure(1, weight=1)

    parent.grid_rowconfigure(0, weight=1)
    parent.grid_rowconfigure(1, weight=1)

    session = create_kpi_card(
        parent,
        "📈",
        "Session",
        "+0 SR"
    )

    session["frame"].grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    winrate = create_kpi_card(
        parent,
        "📊",
        "Winrate",
        "0%"
    )

    winrate["frame"].grid(
        row=0,
        column=1,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    streak = create_kpi_card(
        parent,
        "🔥",
        "Winstreak",
        "x0"
    )

    streak["frame"].grid(
        row=1,
        column=0,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    current = create_kpi_card(
        parent,
        "🎯",
        "SR actuel",
        "0"
    )

    current["frame"].grid(
        row=1,
        column=1,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    return parent, {
        "session": session,
        "winrate": winrate,
        "streak": streak,
        "current": current,
    }