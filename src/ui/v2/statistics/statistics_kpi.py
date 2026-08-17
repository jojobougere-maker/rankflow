import customtkinter as ctk

from src.theme_v2 import *


class StatisticsKPI(ctk.CTkFrame):

    def __init__(self, parent, title, value):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
        )

        self.grid_columnconfigure(0, weight=1)

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 13),
            text_color=TEXT_SECONDARY,
        )

        self.title.pack(
            pady=(16, 4)
        )

        self.value = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI", 28, "bold"),
            text_color=TEXT_PRIMARY,
        )

        self.value.pack(
            pady=(0, 16)
        )

    def set_value(self, value):

        self.value.configure(
            text=str(value)
        )

def create_statistics_kpis(parent):

    frame = ctk.CTkFrame(
        parent,
        fg_color="transparent",
    )

    frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

    cards = {}

    data = [
        ("Winrate", "0 %"),
        ("Victoires", "0"),
        ("Défaites", "0"),
        ("Parties", "0"),
    ]

    for i, (title, value) in enumerate(data):

        card = StatisticsKPI(
            frame,
            title,
            value,
        )

        card.grid(
            row=0,
            column=i,
            padx=8,
            sticky="nsew",
        )

        cards[title] = card

    return frame, cards