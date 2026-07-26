import customtkinter as ctk

from src.theme import *
from src.ui.dialogs import open_settings


def create_header(
    app,
    logo_image,
    settings,
):

    # -----------------------
    # Barre du haut
    # -----------------------

    top_bar = ctk.CTkFrame(
        app,
        height=3,
        fg_color=PRIMARY,
        corner_radius=0
    )
    top_bar.pack(fill="x")

    header = ctk.CTkFrame(
        app,
        height=90,
        fg_color=HEADER,
        corner_radius=0
    )

    header.pack(fill="x")

    header.grid_columnconfigure(0, weight=1)
    header.grid_columnconfigure(1, weight=2)
    header.grid_columnconfigure(2, weight=1)

    left_header = ctk.CTkFrame(header, fg_color="transparent")
    center_header = ctk.CTkFrame(header, fg_color="transparent")
    right_header = ctk.CTkFrame(header, fg_color="transparent")

    left_header.grid(row=0, column=0, sticky="w", padx=25, pady=12)
    center_header.grid(row=0, column=1)
    right_header.grid(row=0, column=2, sticky="e", padx=25, pady=12)

    logo_container = ctk.CTkFrame(
    left_header,
    fg_color="transparent"
    )
    logo_container.pack(anchor="w")

    ctk.CTkLabel(
        logo_container,
        image=logo_image,
        text=""
    ).pack(side="left", padx=(0, 15))

    text_container = ctk.CTkFrame(
        logo_container,
        fg_color="transparent"
    )
    text_container.pack(side="left")

    ctk.CTkLabel(
        text_container,
        text="RankFlow",
        font=("Segoe UI", 30, "bold")
    ).pack(anchor="w")

    ctk.CTkLabel(
        text_container,
        text="Track • Improve • Rise",
        font=("Segoe UI", 14),
        text_color=TEXT_SECONDARY
    ).pack(anchor="w")

    header_session_title = ctk.CTkLabel(
    center_header,
    text="+2130 SR",
    font=("Segoe UI", 30, "bold"),
    text_color="#22C55E"
    )

    header_session_title.pack(pady=(6, 2))

    stats_row = ctk.CTkFrame(
        center_header,
        fg_color="transparent"
    )

    stats_row.pack()

    header_wins_label = ctk.CTkLabel(
        stats_row,
        text="🟢 15 W",
        font=("Segoe UI", 15, "bold")
    )

    header_wins_label.pack(side="left", padx=10)

    header_loss_label = ctk.CTkLabel(
        stats_row,
        text="🔴 1 L",
        font=("Segoe UI", 15, "bold")
    )

    header_loss_label.pack(side="left", padx=10)

    header_winrate_label = ctk.CTkLabel(
        stats_row,
        text="📊 93.8 %",
        font=("Segoe UI", 15, "bold")
    )

    header_winrate_label.pack(side="left", padx=10)

    header_streak_label = ctk.CTkLabel(
        stats_row,
        text="🔥 x5",
        font=("Segoe UI", 15, "bold")
    )   

    header_streak_label.pack(side="left", padx=10)

    profile_frame = ctk.CTkFrame(
    right_header,
    fg_color="transparent"
    )

    profile_frame.pack(anchor="e")

    player_label = ctk.CTkLabel(
        profile_frame,
        text=settings["player"],
        font=("Segoe UI", 18, "bold")
    )

    player_label.pack(anchor="e")

    version_label = ctk.CTkLabel(
        profile_frame,
        text="Version 1.0.0",
        font=("Segoe UI", 12),
        text_color=TEXT_SECONDARY
    )

    version_label.pack(anchor="e", pady=(0, 8))

    settings_button = ctk.CTkButton(
        right_header,
        text="⚙",
        width=42,
        height=42,
        corner_radius=21,
        fg_color=PRIMARY,
        hover_color="#1E6FD9",
        command=None
    )

    settings_button.pack(anchor="e")

    return {
        "header": header,
        "left_header": left_header,
        "center_header": center_header,
        "right_header": right_header,
        "logo_container": logo_container,
        "text_container": text_container,

        "session_title": header_session_title,
        "wins_label": header_wins_label,
        "loss_label": header_loss_label,
        "winrate_label": header_winrate_label,
        "streak_label": header_streak_label,

        "profile_frame": profile_frame,
        "player_label": player_label,
        "version_label": version_label,
        "settings_button": settings_button,
    }