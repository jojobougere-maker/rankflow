import customtkinter as ctk

from PIL import Image

from src.theme_v2 import *
from src.ui.v2.components import RFButton, RFCard, RFProgress
from src.dialogs.new_match_dialog import NewMatchDialog
from src.ui.v2.cards.sr_card_controller import SRCardController
from src.utils.resource_path import resource_path

def create_sr_card(parent, context):
    """Create the dashboard's primary rank card without changing its public API."""
    card = RFCard(parent)
    card.pack(fill="both", expand=True)
    card.configure(corner_radius=RADIUS, border_color=BORDER)
    card.pack_propagate(False)

    # Header stays deliberately quiet so the rank visual remains the focal point.
    rank_label = ctk.CTkLabel(
        card,
        text="RANG ACTUEL",
        font=CARD_TITLE_FONT,
        text_color=SUBTITLE_COLOR,
    )
    rank_label.pack(pady=(PADDING, 0))

    # Rank visual
    rank_image = ctk.CTkImage(
        light_image=Image.open(resource_path("assets/ranks/iridescent.png")),
        dark_image=Image.open(resource_path("assets/ranks/iridescent.png")),
        size=(150, 150),
    )
    rank_icon = ctk.CTkLabel(card, text="", image=rank_image)
    rank_icon.image = rank_image
    rank_icon.pack(pady=(10, 8))

    rank_name = ctk.CTkLabel(
        card,
        text="Iridescent",
        font=("Segoe UI", 34, "bold"),
        text_color=PRIMARY,
    )
    rank_name.pack(pady=(0, 0))

    # The SR is the primary numeric anchor of the entire card.
    sr_value = ctk.CTkLabel(
        card,
        text="9300 SR",
        font=VALUE_FONT,
        text_color=TEXT,
    )
    sr_value.pack(pady=(0, 2))

    sr_text = ctk.CTkLabel(
        card,
        text="Prochain Rang",
        font=("Segoe UI", 13),
        text_color=SUBTITLE_COLOR,
    )
    sr_text.pack(pady=(0, 14))

    # A compact badge gives Top250 the visual weight of an achievement.
    top250_badge = ctk.CTkFrame(
        card,
        fg_color="#1A1F2C",
        corner_radius=18,
        border_width=1,
        border_color="#454F68",
    )
    top250_badge.pack(pady=(0, 10))

    top250_image = ctk.CTkImage(
        light_image=Image.open(resource_path("assets/ranks/top250.png")),
        dark_image=Image.open(resource_path("assets/ranks/top250.png")),
        size=(56, 56),
    )
    top250 = ctk.CTkLabel(top250_badge, image=top250_image, text="")
    top250.image = top250_image
    top250.pack(side="left", padx=(10, 7), pady=7)

    top250_text = ctk.CTkLabel(
        top250_badge,
        text="TOP 250",
        font=("Segoe UI", 14, "bold"),
        text_color=TEXT,
    )
    top250_text.pack(side="left", padx=(0, 11))

    next_rank = ctk.CTkLabel(
        card,
        text="Encore 700 SR pour le rang suivant",
        font=("Segoe UI", 13),
        text_color=SUBTITLE_COLOR,
    )
    next_rank.pack(pady=(0, 8))

    # Current-rank progress
    progress = RFProgress(card)
    progress.configure(height=18, corner_radius=999, progress_color=PRIMARY, fg_color="#303746")
    progress.set(10)
    progress.pack(fill="x", padx=PADDING, pady=(6, 8))

    progress_label = ctk.CTkLabel(
        card,
        text="700 SR restants",
        font=("Segoe UI", 12),
        text_color=SUBTITLE_COLOR,
    )
    progress_label.pack(pady=(0, 4))

    # Goal
    goal_title = ctk.CTkLabel(
        card,
        text="🎯 Objectif personnel",
        font=("Segoe UI", 15, "bold"),
        text_color=TEXT,
    )
    goal_title.pack(pady=(4, 6))

    goal_frame = ctk.CTkFrame(
        card,
        width=280,
        height=54,
        fg_color="#171C27",
        border_color="#3F4A63",
        border_width=1,
        corner_radius=16,
    )
    goal_frame.pack(pady=(0, 8))
    goal_frame.pack_propagate(False)

    goal_value = ctk.CTkLabel(
        goal_frame,
        text="10 000 SR",
        font=("Segoe UI", 22, "bold"),
        text_color=TEXT,
    )
    goal_value.pack(expand=True)

    goal_progress = RFProgress(card)
    goal_progress.configure(height=15, corner_radius=999, progress_color=SUCCESS, fg_color="#303746")
    goal_progress.set(0.93)
    goal_progress.pack(fill="x", padx=PADDING, pady=(0, 9))

    goal_percent = ctk.CTkLabel(
        card,
        text="93 %",
        font=("Segoe UI", 26, "bold"),
        text_color=SUCCESS,
    )
    goal_percent.pack(pady=(0, 2))

    goal_message = ctk.CTkLabel(
        card,
        text="Objectif presque atteint",
        font=("Segoe UI", 15, "bold"),
        text_color=TEXT,
    )
    goal_message.pack(pady=(0, 8))

    # Matching action buttons balance the base of the card.
    # ==========================
    # ACTIONS
    # ==========================

    actions = ctk.CTkFrame(
        card,
        fg_color="transparent",
        height=48
    )
    actions.pack(
        side="bottom",
        fill="x",
        padx=PADDING,
        pady=(0, PADDING)
    )
    actions.pack_propagate(False)

    actions.grid_columnconfigure(0, weight=1)
    actions.grid_columnconfigure(1, weight=1)

    win_button = RFButton(
        actions,
        "✓  Victoire",
        SUCCESS,
        "#2BBF85",
        command=lambda: NewMatchDialog(
            parent.winfo_toplevel(),
            result="Victory",
            on_save=context.match_service.save_match,
        )
    )

    win_button.configure(
        height=48,
        corner_radius=12,
        font=("Segoe UI", 15, "bold")
    )

    win_button.grid(
        row=0,
        column=0,
        sticky="ew",
        padx=(0, 6),
        pady=4
    )

    loss_button = RFButton(
        actions,
        "✕  Défaite",
        DANGER,
        "#E05252",
        command=lambda: NewMatchDialog(
            parent.winfo_toplevel(),
            result="Defeat",
            on_save=context.match_service.save_match,
        )
    )

    loss_button.configure(
        height=48,
        corner_radius=12,
        font=("Segoe UI", 15, "bold")
    )

    loss_button.grid(
        row=0,
        column=1,
        sticky="ew",
        padx=(6, 0),
        pady=4
    )

    widgets = {
        "rank_label": rank_label,
        "rank_name": rank_name,
        "icon": rank_icon,

        "sr": sr_value,

        "progress": progress,
        "progress_label": progress_label,
        "next_rank": next_rank,

        "goal": goal_value,
        "goal_edit": None,
        "goal_progress": goal_progress,
        "goal_percent": goal_percent,
        "goal_message": goal_message,

        "next_rank_badge": top250_badge,
        "next_rank_icon": top250,
        "next_rank_text": top250_text,

        "win": win_button,
        "loss": loss_button,
    }

    return card, SRCardController(widgets)
