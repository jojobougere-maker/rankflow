import customtkinter as ctk

from src.theme_v2 import *


class StatisticsSummary(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
        )

        title = ctk.CTkLabel(
            self,
            text="Résumé",
            font=("Segoe UI", 20, "bold"),
            text_color=TEXT_PRIMARY,
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 16),
        )

        self.rows = {}

        data = [
            ("🏆 Peak SR", "0"),
            ("🔥 Série max", "0"),
            ("📈 SR gagné", "+0"),
            ("🎯 Objectif", "0 %"),
        ]

        for label, value in data:

            row = ctk.CTkFrame(
                self,
                fg_color="transparent",
            )

            row.pack(
                fill="x",
                padx=20,
                pady=6,
            )

            ctk.CTkLabel(
                row,
                text=label,
                font=("Segoe UI", 14),
                text_color=TEXT_SECONDARY,
            ).pack(
                side="left"
            )

            value_label = ctk.CTkLabel(
                row,
                text=value,
                font=("Segoe UI", 16, "bold"),
                text_color=TEXT_PRIMARY,
            )

            value_label.pack(
                side="right"
            )

            self.rows[label] = value_label

    def set_value(self, label, value):

        if label in self.rows:
            self.rows[label].configure(
                text=str(value)
            )


def create_statistics_summary(parent):

    return StatisticsSummary(parent)