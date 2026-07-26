import customtkinter as ctk

from src.theme_v2 import *


def create_header(parent, logo_image, player_name):

    frame = ctk.CTkFrame(
        parent,
        fg_color=SURFACE,
        corner_radius=RADIUS
    )

    return frame, {
        "player_label": player,
        "settings_button": settings,
    }

    frame.grid_columnconfigure(1, weight=1)

    # ==========================
    # Logo
    # ==========================

    logo = ctk.CTkLabel(
        frame,
        image=logo_image,
        text=""
    )

    logo.grid(
        row=0,
        column=0,
        rowspan=2,
        padx=(20, 15),
        pady=20
    )

    # ==========================
    # Titre
    # ==========================

    title = ctk.CTkLabel(
        frame,
        text="RankFlow",
        font=TITLE_FONT
    )

    title.grid(
        row=0,
        column=1,
        sticky="w",
        pady=(18, 0)
    )

    subtitle = ctk.CTkLabel(
        frame,
        text="Track • Improve • Rise",
        font=LABEL_FONT,
        text_color=TEXT_SECONDARY
    )

    subtitle.grid(
        row=1,
        column=1,
        sticky="nw",
        pady=(0, 18)
    )

    # ==========================
    # Profil
    # ==========================

    player = ctk.CTkLabel(
        frame,
        text=player_name,
        font=SUBTITLE_FONT
    )

    player.grid(
        row=0,
        column=2,
        padx=(0, 20),
        sticky="e"
    )

    settings = ctk.CTkButton(
        frame,
        text="⚙",
        width=42,
        height=42,
        corner_radius=21,
        fg_color=PRIMARY,
        hover_color="#6D4AFF"
    )

    settings.grid(
        row=1,
        column=2,
        padx=(0, 20),
        pady=(0, 15),
        sticky="e"
    )

    return {
        "frame": frame,
        "player_label": player,
        "settings_button": settings,
    }