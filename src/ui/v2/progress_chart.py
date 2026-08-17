"""Progression SR chart view.

This module owns presentation only.  Data filtering and formatting remain in
``ProgressChartController``; the controller calls the ``draw`` callback with
its chart dictionary whenever the selected period changes.
"""

from __future__ import annotations

import math

import customtkinter as ctk

from src.theme_v2 import (
    BORDER,
    CARD,
    CARD_TITLE_FONT,
    PADDING,
    PADDING_SECONDARY,
    RADIUS,
    RADIUS_BADGE,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)


# Kept local so the chart remains visually consistent regardless of the
# operating-system theme selected for the rest of the interface.
CHART_BACKGROUND = "#151924"
GRID_COLOR = "#2A3040"
LINE_COLOR = "#A855F7"
LINE_HIGHLIGHT = "#C4B5FD"
FILL_COLOR = "#211B38"
MUTED_TEXT = "#7E879B"

_PLOT_LEFT = 54
_PLOT_RIGHT = 22
_PLOT_TOP = 34
_PLOT_BOTTOM = 34


def _nice_number(value: float) -> int:
    """
    Retourne un pas adapté aux valeurs SR.
    """

    if value <= 10:
        return 10

    if value <= 25:
        return 25

    if value <= 50:
        return 50

    if value <= 100:
        return 100

    if value <= 250:
        return 250

    if value <= 500:
        return 500

    if value <= 1000:
        return 1000

    return int(math.ceil(value / 1000) * 1000)


def _axis_levels(minimum: float, maximum: float) -> list[float]:

    span = max(maximum - minimum, 1)

    step = 100 if span <= 500 else _nice_number(span / 4)

    lower = math.floor(minimum / step) * step
    upper = math.ceil(maximum / step) * step

    if upper - lower < 300:
        upper += step
        lower -= step

    levels = []

    value = upper

    while value >= lower:
        levels.append(value)
        value -= step

    return levels


def _format_sr(value: float) -> str:
    """Avoid visual noise from floating-point padding values."""
    return f"{int(round(value)):,}".replace(",", " ")


def _date_label_indexes(count: int) -> list[int]:
    """Select up to four evenly distributed labels, including both ends."""
    if count <= 1:
        return [0]

    label_count = min(4, count)
    indexes = {round(i * (count - 1) / (label_count - 1)) for i in range(label_count)}
    return sorted(indexes)


def _smooth_path(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Sample a Catmull-Rom spline without adding a plotting dependency."""
    if len(points) < 3:
        return points

    path: list[tuple[float, float]] = [points[0]]
    samples_per_segment = 12

    for index in range(len(points) - 1):
        p0 = points[max(index - 1, 0)]
        p1 = points[index]
        p2 = points[index + 1]
        p3 = points[min(index + 2, len(points) - 1)]

        for sample in range(1, samples_per_segment + 1):
            t = sample / samples_per_segment
            t2 = t * t
            t3 = t2 * t
            x = 0.5 * (
                (2 * p1[0])
                + (-p0[0] + p2[0]) * t
                + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3
            )
            y = 0.5 * (
                (2 * p1[1])
                + (-p0[1] + p2[1]) * t
                + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3
            )
            path.append((x, y))

    return path


def create_progress_chart(parent, compact=False):
    """Create the chart card and return ``(card, controller)`` unchanged."""
    card = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=RADIUS,
        border_width=1,
        border_color=BORDER,
    )

    header = ctk.CTkFrame(card, fg_color="transparent")
    header.pack(fill="x", padx=PADDING, pady=(PADDING, PADDING_SECONDARY))

    title_frame = ctk.CTkFrame(
        header,
        fg_color="transparent",
    )
    title_frame.pack(
        side="left",
        fill="x",
        expand=True,
    )

    ctk.CTkLabel(
        title_frame,
        text="PROGRESSION SR",
        font=CARD_TITLE_FONT,
        text_color=TEXT_PRIMARY,
    ).pack(
        anchor="w",
    )

    stats_label = ctk.CTkLabel(
        title_frame,
        text="",
        font=("Segoe UI", 10),
        text_color=TEXT_SECONDARY,
    )

    stats_label.pack(
        anchor="w",
        pady=(2, 0),
    )

    filters = ctk.CTkFrame(header, fg_color="transparent")
    filters.pack(side="right")

    buttons = {}
    for label in ("7J", "30J", "90J", "TOUT"):
        button = ctk.CTkButton(
            filters,
            text=label,
            width=40 if label == "7J" else 44,
            height=26,
            corner_radius=RADIUS_BADGE,
            fg_color="#A855F7" if label == "7J" else "#232838",
            hover_color="#7C3AED",
            font=("Segoe UI", 11, "bold"),
        )
        button.pack(side="left", padx=2)
        buttons[label] = button

    graph = ctk.CTkCanvas(card, bg=CHART_BACKGROUND, highlightthickness=0)
    graph.pack(fill="both", expand=True, padx=PADDING, pady=(0, PADDING))

    def draw_empty_state() -> None:
        graph.create_text(
            graph.winfo_width() / 2,
            graph.winfo_height() / 2,
            text="Aucune donnée de progression disponible",
            fill=TEXT_SECONDARY,
            font=("Segoe UI", 11),
        )

    def draw_chart(chart=None, _event=None) -> None:
        """Render the controller data; no state or filtering is performed here."""
        graph.delete("all")
        width, height = graph.winfo_width(), graph.winfo_height()
        if width < 120 or height < 120:
            return
        if not chart or not chart.get("values"):

            stats_label.configure(
                text="▲ +0 SR   •   🎮 0 match   •   🏆 0 % WR"
            )

            draw_empty_state()

            return

        values = chart["values"]
        stats = widgets["stats_label"]

        gain = chart.get("gain", 0)
        matches = chart.get("matches", 0)
        winrate = chart.get("winrate", 0)

        arrow = "▲" if gain >= 0 else "▼"

        stats.configure(
            text=f"{arrow} {gain:+} SR   •   🎮 {matches} matchs   •   🏆 {winrate} % WR"
        )
        dates = chart.get("dates", [])
        source_min = float(chart["minimum"])
        source_max = float(chart["maximum"])
        if source_max <= source_min:
            source_min -= 1
            source_max += 1

        left, right = _PLOT_LEFT, width - _PLOT_RIGHT
        top, bottom = _PLOT_TOP, height - _PLOT_BOTTOM
        plot_width, plot_height = right - left, bottom - top
        levels = _axis_levels(source_min, source_max)
        axis_min, axis_max = levels[-1], levels[0]
        if axis_max <= axis_min:
            axis_min, axis_max = source_min, source_max

        # Exactly three quiet horizontal references; deliberately no vertical grid.
        count = len(levels)

        for row, value in enumerate(levels):

            if count == 1:
                y = (top + bottom) / 2
            else:
                y = top + plot_height * (row / (count - 1))

            graph.create_line(
                left,
                y,
                right,
                y,
                fill=GRID_COLOR,
                width=1,
            )

            graph.create_text(
                left - 12,
                y,
                text=_format_sr(value),
                anchor="e",
                fill=MUTED_TEXT,
                font=("Segoe UI", 9),
            )

        count = len(values)
        if count == 1:
            x_positions = [(left + right) / 2]
        else:
            x_positions = [left + plot_width * index / (count - 1) for index in range(count)]

        def y_for(value: float) -> float:
            ratio = (float(value) - axis_min) / (axis_max - axis_min)
            return bottom - max(0, min(1, ratio)) * plot_height

        goal_sr = chart.get("goal_sr")
        goal_y = y_for(goal_sr)

        if goal_sr and axis_min <= goal_sr <= axis_max:

            goal_y = y_for(goal_sr)

            # Ligne pointillée
            for x in range(int(left), int(right), 12):
                graph.create_line(
                    x,
                    goal_y,
                    x + 6,
                    goal_y,
                    fill="#FBBF24",
                    width=2,
                )

            graph.create_text(
                right - 8,
                goal_y - 12,
                text="🎯 Objectif",
                anchor="e",
                fill="#FBBF24",
                font=("Segoe UI", 10, "bold"),
            )

        raw_points = list(zip(x_positions, (y_for(value) for value in values)))
        curve_points = _smooth_path(raw_points)
        curve_points = [(x, max(top, min(bottom, y))) for x, y in curve_points]

        if count > 1:
            fill_points = curve_points + [(curve_points[-1][0], bottom), (curve_points[0][0], bottom)]
            graph.create_polygon(
                [coordinate for point in fill_points for coordinate in point],
                fill=FILL_COLOR,
                outline="",
            )
            graph.create_line(
                [coordinate for point in curve_points for coordinate in point],
                fill=LINE_COLOR,
                width=3,
                capstyle="round",
                joinstyle="round",
            )

        for index in _date_label_indexes(count):
            label = dates[index] if index < len(dates) else ""
            if label:
                graph.create_text(
                    x_positions[index],
                    bottom + 19,
                    text=label,
                    fill=MUTED_TEXT,
                    font=("Segoe UI", 9),
                )

        last_x, last_y = raw_points[-1]
        graph.create_oval(last_x - 8, last_y - 8, last_x + 8, last_y + 8, fill=CHART_BACKGROUND, outline="#FFFFFF", width=2)
        graph.create_oval(last_x - 3.5, last_y - 3.5, last_x + 3.5, last_y + 3.5, fill=LINE_HIGHLIGHT, outline="")

        current_sr = chart.get("current_sr", values[-1])
        label_y = last_y - 22 if last_y > top + 28 else last_y + 22
        graph.create_text(
            last_x,
            label_y,
            text=f"{_format_sr(float(current_sr))} SR",
            fill="#E9E3FF",
            font=("Segoe UI", 11, "bold"),
        )

    widgets = {"graph": graph, "draw": draw_chart, "buttons": buttons, "chart": None, "stats_label": stats_label,}
    graph.bind("<Configure>", lambda event: draw_chart(widgets["chart"], event))

    from src.ui.v2.progress_chart_controller import ProgressChartController

    controller = ProgressChartController(
        widgets,
        compact=compact,
    )
    for name, button in buttons.items():
        button.configure(command=lambda value=name: controller.set_filter(value))

    controller.refresh()
    return card, controller
