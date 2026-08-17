import customtkinter as ctk

from src.database.repository import get_matches
from src.services.rank_service import RankService
from src.theme_v2 import *


def _blend_hex(base, overlay, amount):
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


def _enable_row_hover(row, widgets, default_color, hover_color):
    def set_hovered(_event=None):
        row.configure(fg_color=hover_color)

    def set_default(_event=None):
        row.configure(fg_color=default_color)

    for widget in (row, *widgets):
        widget.bind("<Enter>", set_hovered)
        widget.bind("<Leave>", set_default)


def _longest_streak(matches, result):
    best = 0
    current = 0

    for match in matches:
        if match["result"] == result:
            current += 1
            best = max(best, current)
        else:
            current = 0

    return best


class _StatsCardController:
    """Refresh the existing statistics view from the match repository."""

    def __init__(self, widgets):
        self.widgets = widgets
        self.rank_service = RankService()

    def refresh(self):
        matches = get_matches()
        self._update_streaks(matches)
        self._update_latest_rank(matches)
        self._update_session(matches)
        self.widgets["matches"].configure(text=str(len(matches)))

    def _update_streaks(self, matches):
        self.widgets["winstreak"].configure(
            text=f"x{_longest_streak(matches, 'Victory')}"
        )
        self.widgets["loss_streak"].configure(
            text=f"x{_longest_streak(matches, 'Defeat')}"
        )

    def _update_latest_rank(self, matches):
        if not matches:
            self.widgets["promotion"].configure(text="\u2014")
            return

        rank = self.rank_service.get_rank(int(matches[0]["sr_after"]))
        self.widgets["promotion"].configure(text=rank.name)

    def _update_session(self, matches):
        session_sr = sum(int(match["sr_change"]) for match in matches)
        self.widgets["session"].configure(text=f"{session_sr:+d} SR")


def create_stats_card(parent):
    """Build the compact statistics panel while preserving the existing API."""
    try:
        parent.configure(corner_radius=RADIUS, border_width=1, border_color=BORDER)
    except (AttributeError, TypeError):
        pass

    title_row = ctk.CTkFrame(parent, fg_color="transparent")
    title_row.pack(fill="x", padx=PADDING, pady=(PADDING, PADDING_SECONDARY))

    title_icon = ctk.CTkLabel(
        title_row,
        text="\u25c8",
        font=("Segoe UI Symbol", ICON_SIZE, "bold"),
        text_color=PRIMARY,
    )
    title_icon.pack(side="left", padx=(0, 8))

    title = ctk.CTkLabel(
        title_row,
        text="STATISTIQUES",
        font=CARD_TITLE_FONT,
        text_color=TEXT,
    )
    title.pack(side="left")

    stats = [
        ("winstreak", "\U0001F3C6", SUCCESS, "x0", "PLUS GROSSE WINSTREAK"),
        ("loss_streak", "\U0001F4A5", DANGER, "x0", "PLUS GROSSE S\u00c9RIE DE D\u00c9FAITES"),
        ("promotion", "\u2b06", PRIMARY, "\u2014", "PROMOTION LA PLUS R\u00c9CENTE"),
        ("session", "\U0001F4C8", PRIMARY, "+0 SR", "MEILLEURE SESSION"),
        ("matches", "\U0001F3AE", TEXT_SECONDARY, "0", "PARTIES JOU\u00c9ES"),
    ]

    stats_list = ctk.CTkFrame(parent, fg_color="transparent")
    stats_list.pack(fill="x", padx=PADDING, pady=(0, PADDING))

    widgets = {}
    for key, icon, color, value, label in stats:
        row_color = "#191E29"
        hover_color = _blend_hex(row_color, PRIMARY, 0.12)

        row = ctk.CTkFrame(
            stats_list,
            fg_color=row_color,
            height=46,
            corner_radius=RADIUS_SMALL,
            border_width=1,
            border_color=BORDER,
        )
        row.pack(fill="x", pady=3)
        row.pack_propagate(False)

        icon_ring = ctk.CTkFrame(
            row,
            width=34,
            height=34,
            corner_radius=17,
            fg_color=row_color,
            border_width=2,
            border_color=_blend_hex(row_color, color, 0.22),
        )

        icon_ring.pack(side="left", padx=(10, 10), pady=8)
        icon_ring.pack_propagate(False)

        icon_label = ctk.CTkLabel(
            icon_ring,
            text=icon,
            font=("Segoe UI Emoji", ICON_SIZE),
            text_color=color,
        )

        icon_label.place(relx=0.5, rely=0.5, anchor="center")

        description = ctk.CTkLabel(
            row,
            text=label,
            font=("Segoe UI", 10, "bold"),
            text_color=TEXT_SECONDARY,
        )
        description.pack(side="left", fill="x", expand=True)

        value_label = ctk.CTkLabel(
            row,
            text=value,
            font=VALUE_COMPACT_FONT,
            text_color=color,
        )
        value_label.pack(side="right", padx=(10, 14))
        widgets[key] = value_label

        _enable_row_hover(
            row,
            (icon_ring, icon_label, description, value_label),
            row_color,
            hover_color,
        )

    controller = _StatsCardController(widgets)
    parent.refresh = controller.refresh
    parent._stats_controller = controller
    controller.refresh()
    return parent
