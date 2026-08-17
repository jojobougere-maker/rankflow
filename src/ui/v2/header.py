import customtkinter as ctk

from src.theme_v2 import *
from src.ui.v2.avatar import create_avatar
from src.ui.v2.icon_button import create_icon_button
from src.core.version import APP_VERSION


HEADER_HEIGHT = 90


def create_header(parent, logo_image, player_name):

    # --------------------------------------------------
    # LOGO
    # --------------------------------------------------

    try:
        w, h = logo_image.cget("size")
        logo_image.configure(size=(82, 82))
    except Exception:
        pass

    header = ctk.CTkFrame(
        parent,
        fg_color="#0B0F17",
        corner_radius=0,
        height=HEADER_HEIGHT,
        border_width=0,
    )

    header.pack_propagate(False)

    # 3 zones
    header.grid_columnconfigure(0, weight=0)
    header.grid_columnconfigure(1, weight=1)
    header.grid_columnconfigure(2, weight=0)

    header.grid_rowconfigure(0, weight=1)
    header.grid_rowconfigure(1, minsize=1)

    # ============================================================
    # LEFT
    # ============================================================

    left = ctk.CTkFrame(
        header,
        fg_color="transparent",
        height=HEADER_HEIGHT,
    )

    left.grid(
        row=0,
        column=0,
        sticky="nsw",
        padx=(20, 0),
    )

    # --------------------------------------------------
    # Logo container
    # --------------------------------------------------

    logo_box = ctk.CTkFrame(
        left,
        width=84,
        height=84,
        fg_color="#101722",
        border_width=1,
        border_color="#252F3F",
        corner_radius=20
    )

    logo_box.pack(
        side="left",
        pady=(12,2)
    )

    logo_box.pack_propagate(False)

    logo = ctk.CTkLabel(
        logo_box,
        image=logo_image,
        text="",
    )

    logo.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
    )

    # petite séparation verticale
    divider = ctk.CTkFrame(
        left,
        width=1,
        height=52,
        fg_color="#232936",
    )

    divider.pack(
        side="left",
        padx=(14, 14),
        pady=18,
    )

    # --------------------------------------------------
    # Branding
    # --------------------------------------------------

    branding = ctk.CTkFrame(
        left,
        fg_color="transparent",
    )

    branding.pack(
        side="left",
        pady=(2, 0),
    )

    title = ctk.CTkFrame(
        branding,
        fg_color="transparent",
    )

    title.pack(anchor="w")

    lbl_rank = ctk.CTkLabel(
        title,
        text="Rank",
        font=("Segoe UI", 36, "bold"),
        text_color="#B45CFF",
    )

    lbl_rank.pack(
        side="left",
        pady=0,
    )

    lbl_flow = ctk.CTkLabel(
        title,
        text="Flow",
        font=("Segoe UI", 36, "bold"),
        text_color="#FFFFFF",
    )

    lbl_flow.pack(
        side="left",
        pady=0,
    )

    subtitle = ctk.CTkLabel(
        branding,
        text="Track • Improve • Rise",
        font=("Segoe UI", 13),
        text_color=TEXT_SECONDARY,
    )

    subtitle.pack(
        anchor="w",
        pady=(1, 0),
    )

    # ============================================================
    # CENTER
    # ============================================================

    center = ctk.CTkFrame(
        header,
        fg_color="transparent",
    )

    center.grid(
        row=0,
        column=1,
        sticky="nsew",
    )

    # la capsule sera ajoutée ici (PARTIE 2)

    # ============================================================
    # RIGHT
    # ============================================================

    right = ctk.CTkFrame(
        header,
        fg_color="transparent",
        width=290,
    )

    right.grid(
        row=0,
        column=2,
        sticky="e",
        padx=(20, 20),
    )

    right.pack_propagate(False)

    # ============================================================
    # SESSION CAPSULE
    # ============================================================

    session_box = ctk.CTkFrame(
        center,
        width=620,
        height=54,
        fg_color="#101620",
        corner_radius=16,
        border_width=1,
        border_color="#1A2330",
    )

    session_box.place(
        relx=0.5,
        rely=0.46,
        anchor="center",
    )

    session_box.pack_propagate(False)
    session_box.grid_propagate(False)

    stats_container = ctk.CTkFrame(
        session_box,
        fg_color="transparent",
    )

    stats_container.place(
        relx=0.5,
        rely=0.5,
        anchor="center",
    )

    stats = [
        ("+253 SR", "SESSION", "#22C55E"),
        ("18", "VICTOIRES", "#22C55E"),
        ("9", "DÉFAITES", "#EF4444"),
        ("66.7%", "WINRATE", "#3B82F6"),
        ("🔥 x7", "WINSTREAK", "#F59E0B"),
    ]

    header_kpis = {}
    kpi_keys = ("session", "wins", "losses", "winrate", "winstreak")

    for i, (value, label, color) in enumerate(stats):

        item = ctk.CTkFrame(
            stats_container,
            width=104,
            height=44,
            fg_color="transparent",
        )

        item.pack(
            side="left",
            padx=0,
        )

        item.pack_propagate(False)

        value_lbl = ctk.CTkLabel(
            item,
            text=value,
            font=("Segoe UI", 20, "bold"),
            text_color=color,
        )

        value_lbl.pack(
            pady=(2, 0),
        )
        header_kpis[kpi_keys[i]] = value_lbl

        label_lbl = ctk.CTkLabel(
            item,
            text=label,
            font=("Segoe UI", 10),
            text_color=TEXT_SECONDARY,
        )

        label_lbl.pack(
            pady=(1, 0),
        )

        if i != len(stats) - 1:

            separator = ctk.CTkFrame(
                stats_container,
                width=1,
                height=28,
                fg_color="#2D3644",
            )

            separator.pack(
                side="left",
                padx=8,
                pady=8,
            )

    # ============================================================
    # PROFILE
    # ============================================================

    profile = ctk.CTkFrame(
        right,
        fg_color="transparent",
    )

    profile.place(
        relx=1.0,
        rely=0.55,
        anchor="e",
    )

    profile.grid_columnconfigure(1, weight=1)

    # -------------------------------------------------------
    # Rank emblem
    # -------------------------------------------------------

    avatar = create_avatar(
        profile,
        size=46,
    )

    avatar.grid(
        row=0,
        column=0,
        rowspan=3,
        padx=(0, 12),
        sticky="n",
    )

    # -------------------------------------------------------
    # Player name
    # -------------------------------------------------------

    player = ctk.CTkLabel(
        profile,
        text=player_name,
        font=("Segoe UI", 17, "bold"),
        text_color=TEXT,
    )

    player.grid(
        row=0,
        column=1,
        sticky="w",
        pady=(0, 0),
    )

    # -------------------------------------------------------
    # Version
    # -------------------------------------------------------

    version = ctk.CTkLabel(
        profile,
        text=f"Version {APP_VERSION}",
        font=("Segoe UI", 10),
        text_color=TEXT_SECONDARY,
    )

    version.grid(
        row=2,
        column=1,
        sticky="w",
        pady=(1, 0),
    )

    # -------------------------------------------------------
    # Settings
    # -------------------------------------------------------

    settings = create_icon_button(
        profile,
        "assets/icons/settings.png",
    )

    settings.configure(
        width=32,
        height=32,
        corner_radius=10,
    )

    settings.grid(
        row=0,
        column=2,
        rowspan=3,
        padx=(24, 0),
        sticky="e",
    )
    # ============================================================
    # SEPARATOR
    # ============================================================

    separator = ctk.CTkFrame(
        header,
        height=1,
        fg_color="#232936",
    )

    separator.grid(
        row=1,
        column=0,
        columnspan=3,
        sticky="ew",
    )

    return header, {
        "player_name": player,
        "player_avatar": avatar,
        "settings_button": settings,
        "theme_button": None,
        "kpi_values": header_kpis,
    }
