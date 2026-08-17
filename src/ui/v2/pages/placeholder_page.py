import customtkinter as ctk

from src.theme_v2 import BORDER, CARD, PADDING, RADIUS, TEXT_PRIMARY, TEXT_SECONDARY


class PlaceholderPage(ctk.CTkFrame):
    """Clean empty state for a future navigation destination."""

    def __init__(self, parent, title, subtitle):
        super().__init__(parent, fg_color="transparent")

        panel = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
        )
        panel.pack(fill="both", expand=True)

        ctk.CTkLabel(
            panel,
            text=title,
            text_color=TEXT_PRIMARY,
            font=("Segoe UI", 24, "bold"),
        ).pack(anchor="w", padx=PADDING, pady=(PADDING, 6))

        ctk.CTkLabel(
            panel,
            text=subtitle,
            text_color=TEXT_SECONDARY,
            font=("Segoe UI", 13),
        ).pack(anchor="w", padx=PADDING)

        ctk.CTkFrame(panel, fg_color="transparent").pack(fill="both", expand=True)
