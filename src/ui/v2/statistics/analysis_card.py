import customtkinter as ctk

from src.theme_v2 import *


class AnalysisCard(ctk.CTkFrame):

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
            text="🧠 Analyse",
            font=("Segoe UI", 20, "bold"),
            text_color=TEXT_PRIMARY,
        )

        title.pack(
            anchor="w",
            padx=20,
            pady=(20, 16),
        )

        self.messages = []

        examples = [
            "🔥 Excellent winrate.",
            "📈 Votre progression est régulière.",
            "🎯 Objectif atteint à 58 %.",
            "💪 Continuez sur ce rythme !",
        ]

        for text in examples:

            label = ctk.CTkLabel(
                self,
                text=text,
                anchor="w",
                justify="left",
                font=("Segoe UI", 14),
                text_color=TEXT_SECONDARY,
            )

            label.pack(
                fill="x",
                padx=20,
                pady=5,
            )

            self.messages.append(label)

    def set_messages(self, messages):

        for label, message in zip(self.messages, messages):
            label.configure(text=message)


def create_analysis_card(parent):

    return AnalysisCard(parent)