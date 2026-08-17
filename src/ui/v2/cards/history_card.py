"""Modern match-history card for the V2 dashboard.

The public factories keep their original signatures.  Data loading is kept in
the private controller below and refreshes through the existing dashboard flow.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import customtkinter as ctk
from PIL import Image

from src.database.repository import get_matches
from src.services.rank_service import RankService
from src.theme_v2 import (
    BORDER,
    CARD,
    CARD_TITLE_FONT,
    DANGER,
    PADDING,
    RADIUS,
    RADIUS_BADGE,
    RADIUS_SMALL,
    SUCCESS,
    TEXT,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)
from src.utils.resource_path import resource_path


ROW_COLOR = "#222836"
ROW_HOVER_COLOR = "#2A3141"
ROW_BORDER_COLOR = "#252C3A"
ROW_HOVER_BORDER = "#5B4A87"
WIN_TINT = "#19382F"
LOSS_TINT = "#3A222B"
PROJECT_ROOT = Path(__file__).resolve().parents[4]


def _is_victory(result: Any) -> bool:
    return str(result).strip().upper() in {"VICTOIRE", "VICTORY", "WIN", "W"}


def _parse_datetime(value: Any) -> datetime | None:
    if isinstance(value, datetime):
        return value

    if not value:
        return None

    for pattern in ("%d/%m/%Y %H:%M", "%d/%m/%Y", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(value), pattern)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(str(value))
    except ValueError:
        pass
    return None


def _group_label(match_date: Any) -> str:
    parsed = _parse_datetime(match_date)
    if parsed is None:
        return "Historique récent"

    today = datetime.now().date()
    if parsed.date() == today:
        return "Aujourd’hui"
    if parsed.date() == today - timedelta(days=1):
        return "Hier"
    months = (
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre",
    )
    return f"{parsed.day} {months[parsed.month - 1]}"


def _display_date(match_date: Any) -> str:
    parsed = _parse_datetime(match_date)
    if parsed is None:
        return str(match_date or "Date inconnue")

    today = datetime.now().date()
    time = parsed.strftime("%H:%M")
    if parsed.date() == today:
        return f"Aujourd’hui · {time}"
    if parsed.date() == today - timedelta(days=1):
        return f"Hier · {time}"
    return f"{_group_label(parsed)} · {time}"


def _normalise_match(result, sr, mode, duration, date) -> dict[str, Any]:
    """Accept the legacy arguments as well as a richer mapping in ``result``."""
    if isinstance(result, dict):
        match = dict(result)
        match.setdefault("result", match.get("outcome", "Défaite"))
        match.setdefault("delta", match.get("sr_delta", sr))
        match.setdefault("mode", mode)
        match.setdefault("duration", duration)
        match.setdefault("date", date)
    else:
        match = {"result": result, "delta": sr, "mode": mode, "duration": duration, "date": date}

    match.setdefault("rank", "Iridescent")
    match.setdefault("rank_icon", None)
    match.setdefault("before", "—")
    match.setdefault("after", "—")
    return match


def _rank_image(icon_path: str | None) -> ctk.CTkImage | None:
    if not icon_path:
        return None

    image_path = Path(icon_path)
    if not image_path.is_absolute():
        image_path = PROJECT_ROOT / image_path
    if not image_path.is_file():
        return None

    try:
        image = Image.open(resource_path(image_path))
        return ctk.CTkImage(light_image=image, dark_image=image, size=(34, 34))
    except (OSError, ValueError):
        return None


def _label(parent, text, *, color=TEXT, font=("Segoe UI", 12), **grid_options):
    label = ctk.CTkLabel(parent, text=text, text_color=color, font=font)
    label.grid(**grid_options)
    return label


def _blend_hex(start: str, end: str, progress: float) -> str:
    """Interpolate two theme colours for the short row-hover transition."""
    start_rgb = tuple(int(start[index:index + 2], 16) for index in (1, 3, 5))
    end_rgb = tuple(int(end[index:index + 2], 16) for index in (1, 3, 5))
    mixed = tuple(round(first + (second - first) * progress) for first, second in zip(start_rgb, end_rgb))
    return "#{:02X}{:02X}{:02X}".format(*mixed)


def _animate_row(row: ctk.CTkFrame, fill: str, border: str) -> None:
    """Run a restrained, interruption-safe colour transition on a match row."""
    row._hover_token = getattr(row, "_hover_token", 0) + 1
    token = row._hover_token
    start_fill = getattr(row, "_display_fill", ROW_COLOR)
    start_border = getattr(row, "_display_border", ROW_BORDER_COLOR)

    def step(index: int = 1) -> None:
        if token != row._hover_token:
            return
        progress = index / 5
        eased = 1 - (1 - progress) ** 2
        row._display_fill = _blend_hex(start_fill, fill, eased)
        row._display_border = _blend_hex(start_border, border, eased)
        row.configure(fg_color=row._display_fill, border_color=row._display_border)
        if index < 5:
            row.after(16, lambda: step(index + 1))

    step()


def _enable_row_hover(row: ctk.CTkFrame) -> None:
    row._display_fill = ROW_COLOR
    row._display_border = ROW_BORDER_COLOR
    row.bind("<Enter>", lambda _event: _animate_row(row, ROW_HOVER_COLOR, ROW_HOVER_BORDER))
    row.bind("<Leave>", lambda _event: _animate_row(row, ROW_COLOR, ROW_BORDER_COLOR))


def _create_history_item(parent, match: dict[str, Any]) -> ctk.CTkFrame:
    victory = _is_victory(match["result"])
    accent = SUCCESS if victory else DANGER
    tint = WIN_TINT if victory else LOSS_TINT
    item = ctk.CTkFrame(
        parent,
        fg_color=ROW_COLOR,
        corner_radius=RADIUS_SMALL,
        border_width=1,
        border_color=ROW_BORDER_COLOR,
        height=78,
    )
    item.pack(fill="x", pady=(0, 7))
    item.pack_propagate(False)

    for column, weight in enumerate((15, 17, 16, 24)):
        item.grid_columnconfigure(column, weight=weight)

    badge = ctk.CTkLabel(
        item,
        text="VICTORY" if victory else "DEFEAT",
        fg_color=tint,
        corner_radius=RADIUS_BADGE,
        text_color=accent,
        font=("Segoe UI", 10, "bold"),
        width=70,
        height=24,
    )
    badge.grid(row=0, column=0, padx=(16, 8), pady=(15, 0), sticky="w")
    _label(item, str(match["delta"]), color=accent, font=("Segoe UI", 13, "bold"), row=1, column=0, padx=(16, 8), pady=(0, 13), sticky="w")

    rank_frame = ctk.CTkFrame(item, fg_color="transparent")
    rank_frame.grid(row=0, column=1, rowspan=2, padx=8, sticky="w")
    image = _rank_image(match.get("rank_icon"))
    if image:
        icon = ctk.CTkLabel(rank_frame, text="", image=image)
        icon.image = image
        icon.pack(side="left", padx=(0, 7))
    ctk.CTkLabel(rank_frame, text=str(match["rank"]), text_color=TEXT, font=("Segoe UI", 12, "bold")).pack(side="left")

    _label(item, "SR", color=TEXT_SECONDARY, font=("Segoe UI", 10, "bold"), row=0, column=2, padx=8, pady=(15, 0), sticky="sw")
    _label(item, f"{match['before']}  →  {match['after']}", color=TEXT, font=("Segoe UI", 12, "bold"), row=1, column=2, padx=8, pady=(0, 13), sticky="nw")

    _label(item, _display_date(match["date"]), color=TEXT_SECONDARY, font=("Segoe UI", 11), row=0, column=3, padx=(8, 16), pady=(15, 0), sticky="sw")
    _label(item, str(match["mode"]), color=TEXT, font=("Segoe UI", 12), row=1, column=3, padx=(8, 16), pady=(0, 13), sticky="nw")
    _enable_row_hover(item)
    return item


def create_history_item(parent, result, sr, mode, duration, date):
    """Create a match row while preserving the original public API."""
    return _create_history_item(parent, _normalise_match(result, sr, mode, duration, date))


def _render_matches(container, matches) -> None:
    for child in container.winfo_children():
        child.destroy()

    if not matches:
        ctk.CTkLabel(container, text="Aucune partie récente.", text_color=TEXT_SECONDARY, font=("Segoe UI", 12)).pack(pady=28)
        return

    current_group = None
    for match in matches:
        group = _group_label(match["date"])
        if group != current_group:
            ctk.CTkLabel(container, text=group, text_color=TEXT_SECONDARY, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(12 if current_group else 0, 8))
            current_group = group
        _create_history_item(container, match)


def _format_sr(value: int) -> str:
    return f"{value:,}".replace(",", " ")


class _HistoryCardController:
    """Map the existing match repository to the view's display model."""

    def __init__(self, results: ctk.CTkScrollableFrame):
        self.results = results
        self.rank_service = RankService()

    def refresh(self) -> None:
        _render_matches(self.results, self._load_matches())

    def _load_matches(self) -> list[dict[str, Any]]:
        matches = []
        for record in get_matches():
            sr_after = int(record["sr_after"])
            sr_change = int(record["sr_change"])
            rank = self.rank_service.get_rank(sr_after)
            matches.append(
                {
                    "result": record["result"],
                    "delta": f"{sr_change:+d} SR",
                    "rank": rank.name,
                    "rank_icon": rank.icon,
                    "before": _format_sr(sr_after - sr_change),
                    "after": _format_sr(sr_after),
                    "mode": "Classé",
                    "date": record["played_at"],
                }
            )
        return matches


def create_history_card(parent):
    """Create the complete card while preserving the original public API."""
    try:
        parent.configure(fg_color=CARD, corner_radius=RADIUS, border_width=1, border_color=BORDER)
    except (AttributeError, TypeError):
        pass

    header = ctk.CTkFrame(parent, fg_color="transparent")
    header.pack(fill="x", padx=PADDING, pady=(PADDING, 10))
    ctk.CTkLabel(header, text="DERNIÈRES PARTIES", text_color=TEXT_PRIMARY, font=CARD_TITLE_FONT).pack(side="left")
    ctk.CTkLabel(header, text="Historique récent", text_color=TEXT_SECONDARY, font=("Segoe UI", 11)).pack(side="right")

    results = ctk.CTkScrollableFrame(parent, fg_color="transparent", height=390)
    results.pack(fill="both", expand=True, padx=PADDING, pady=(0, PADDING))
    controller = _HistoryCardController(results)
    parent.refresh = controller.refresh
    parent._history_controller = controller
    controller.refresh()
    return parent
