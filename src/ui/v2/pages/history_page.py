import customtkinter as ctk

from src.theme_v2 import (
    BORDER,
    CARD,
    PADDING,
    RADIUS,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)

from src.ui.v2.cards.history_card import create_history_card


class HistoryPage(ctk.CTkFrame):
    """Full history page."""

    def __init__(self, parent, context):
        super().__init__(parent, fg_color="transparent")

        self.context = context

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._build_header()
        self._build_content()

    def _build_header(self):

        header = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
        )
        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=PADDING,
            pady=(PADDING, 12),
        )

        ctk.CTkLabel(
            header,
            text="HISTORIQUE",
            text_color=TEXT_PRIMARY,
            font=("Segoe UI", 26, "bold"),
        ).pack(anchor="w", padx=PADDING, pady=(PADDING, 2))

        ctk.CTkLabel(
            header,
            text="Retrouve toutes tes parties classées.",
            text_color=TEXT_SECONDARY,
            font=("Segoe UI", 13),
        ).pack(anchor="w", padx=PADDING, pady=(0, PADDING))

    def _build_content(self):

        body = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        body.grid(
            row=1,
            column=0,
            sticky="nsew",
        )

        card = ctk.CTkFrame(
            body,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
        )

        card.pack(
            fill="both",
            expand=True,
            padx=PADDING,
            pady=(0, PADDING),
        )

        history = create_history_card(card)

        history.pack(
            fill="both",
            expand=True,
        )

        self.history = history

        self.context.dashboard.register_history_card(self.history)