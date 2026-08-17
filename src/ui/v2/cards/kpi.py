import customtkinter as ctk

from src.theme_v2 import *
from src.analytics.statistics import (
    current_sr,
    current_winrate,
    total_matches,
)
from .kpi_controller import KPICardController


def _blend_hex(base, overlay, amount):
    """Blend two hex colours while keeping the KPI API independent of the theme."""
    try:
        base = base.lstrip("#")
        overlay = overlay.lstrip("#")
        base_rgb = tuple(int(base[index:index + 2], 16) for index in (0, 2, 4))
        overlay_rgb = tuple(int(overlay[index:index + 2], 16) for index in (0, 2, 4))
        mixed = tuple(
            round(channel + (accent_channel - channel) * amount)
            for channel, accent_channel in zip(base_rgb, overlay_rgb)
        )
        return "#{:02X}{:02X}{:02X}".format(*mixed)
    except (AttributeError, ValueError):
        return base


def create_kpi_card(parent, icon, title, value, accent, trend, subtitle):
    """Create a polished KPI card without changing the public component contract."""
    card_tint = _blend_hex(CARD, accent, 0.09)
    border_tint = _blend_hex(BORDER, accent, 0.26)
    icon_ring = _blend_hex(CARD, accent, 0.22)
    icon_surface = _blend_hex(accent, "#FFFFFF", 0.08)
    badge_tint = _blend_hex(CARD, accent, 0.18)

    card = ctk.CTkFrame(
        parent,
        fg_color=card_tint,
        corner_radius=RADIUS,
        border_width=1,
        border_color=BORDER,
        height=170,
    )
    card.pack_propagate(False)

    # Main metric: generous spacing keeps the value as the focal point.
    header = ctk.CTkFrame(card, fg_color="transparent")
    header.pack(fill="x", padx=PADDING, pady=(22, PADDING_SECONDARY))

    # The outer ring creates a subtle relief around the accent-coloured icon.
    icon_container = ctk.CTkFrame(
        header,
        width=62,
        height=62,
        corner_radius=31,
        fg_color=icon_surface,
        border_width=4,
        border_color=icon_ring,
    )

    icon_container.pack(side="left")
    icon_container.pack_propagate(False)

    ctk.CTkLabel(
        icon_container,
        text=icon,
        font=("Segoe UI Emoji", ICON_SIZE),
        text_color="white",
    ).place(relx=0.5, rely=0.5, anchor="center")

    text = ctk.CTkFrame(header, fg_color="transparent")
    text.pack(side="left", fill="x", expand=True, padx=(16, 0))

    value_label = ctk.CTkLabel(
        text,
        text=value,
        font=VALUE_SECONDARY_FONT,
        text_color=TEXT,
    )
    value_label.pack(anchor="w")

    title_label = ctk.CTkLabel(
        text,
        text=title,
        font=("Segoe UI", 12, "bold"),
        text_color=SUBTITLE_COLOR,
    )
    title_label.pack(anchor="w", pady=(1, 0))

    # A quiet footer separates the supporting information from the main metric.
    footer = ctk.CTkFrame(card, fg_color="transparent")
    footer.pack(fill="x", padx=PADDING, pady=(0, PADDING))

    trend_frame = ctk.CTkFrame(
        footer,
        fg_color=badge_tint,
        corner_radius=RADIUS_SMALL,
        border_width=1,
        border_color=border_tint,
    )
    trend_frame.pack(side="left")

    trend_label = ctk.CTkLabel(
        trend_frame,
        text=trend,
        font=("Segoe UI", 11, "bold"),
        text_color=accent,
    )
    trend_label.pack(padx=10, pady=5)

    subtitle_label = ctk.CTkLabel(
        footer,
        text=subtitle,
        font=("Segoe UI", 11),
        text_color=SUBTITLE_COLOR,
    )
    subtitle_label.pack(side="left", padx=(10, 0))

    return {
        "frame": card,
        "value": value_label,
        "title": title_label,
        "trend": trend_label,
        "subtitle": subtitle_label,
    }


def create_kpi_grid(parent):
    for i in range(4):
        parent.grid_columnconfigure(i, weight=1)

    parent.grid_rowconfigure(0, weight=1)

    session = create_kpi_card(
        parent,
        "📈",
        "SESSION",
        "+253 SR",
        "#35D07F",
        "↑ +3.2%",
        "Par rapport à hier",
    )

    session["frame"].grid(
        row=0,
        column=0,
        padx=8,
        pady=0,
        sticky="nsew",
    )

    winrate = create_kpi_card(
        parent,
        "📊",
        "WINRATE",
        f"{current_winrate()}%",
        "#3B82F6",
        "↑ +5.4%",
        "Par rapport à hier",
    )

    winrate["frame"].grid(
        row=0,
        column=1,
        padx=8,
        pady=0,
        sticky="nsew",
    )

    streak = create_kpi_card(
        parent,
        "🔥",
        "WINSTREAK",
        "x7",
        "#F59E0B",
        "🔥 Record personnel",
        f"{total_matches()} parties",
    )

    streak["frame"].grid(
        row=0,
        column=2,
        padx=8,
        pady=0,
        sticky="nsew",
    )

    current = create_kpi_card(
        parent,
        "🎯",
        "SR ACTUEL",
        f"{current_sr()} SR",
        "#8B5CF6",
        "Top 0.01%",
        "Iridescent",
    )

    current["frame"].grid(
        row=0,
        column=3,
        padx=8,
        pady=0,
        sticky="nsew",
    )

    widgets = {
        "session": session,
        "winrate": winrate,
        "streak": streak,
        "current": current,
    }

    controller = KPICardController(widgets)
    controller.refresh()

    return parent, controller