import customtkinter as ctk

from src.theme_v2 import *
from src.ui.v2.components import (
    RFCard,
    RFSectionTitle,
    RFLabel,
    RFButton,
)

class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")

        self._build_ui()

    def _build_ui(self):

        container = RFCard(self)
        container.pack(
            fill="both",
            expand=True,
            padx=OUTER_MARGIN,
            pady=OUTER_MARGIN,
        )

        RFSectionTitle(
            container,
            "Profil du joueur"
        ).pack(
            anchor="w",
            padx=36,
            pady=(30, 26),
        )

        ctk.CTkLabel(
            container,
            text="Personnalisez votre profil et vos objectifs de progression.",
            font=("Segoe UI", 13),
            text_color=TEXT_SECONDARY,
        ).pack(
            anchor="w",
            padx=36,
            pady=(0, 28),
        )

        content = ctk.CTkFrame(
            container,
            fg_color="transparent",
        )
        content.pack(
            anchor="center",
            pady=(0, 20),
        )

        form = ctk.CTkFrame(
            content,
            fg_color="transparent",
        )

        form.pack()

        self.username = self._entry(
            form,
            "Pseudo Activision",
        )

        self.current_sr = self._entry(
            form,
            "SR actuel",
        )

        self.goal_sr = self._entry(
            form,
            "Objectif SR",
        )

        self.status = ctk.CTkLabel(
            container,
            text="",
            font=("Segoe UI", 13, "bold"),
            text_color="#4ADE80",   # Vert
        )

        self.status.pack(
            pady=(10, 0)
        )

        self.save_button = RFButton(
            container,
            text="Enregistrer",
            color=PRIMARY,
            hover="#6D50FF",
        )

        self.save_button.pack(
            pady=(20, 30),
        )

        # ==========================
        # Maintenance
        # ==========================

        ctk.CTkFrame(
            container,
            height=1,
            fg_color=BORDER,
        ).pack(
            fill="x",
            padx=36,
            pady=(10, 30),
        )

        RFSectionTitle(
            container,
            "Maintenance",
        ).pack(
            anchor="w",
            padx=36,
        )

        ctk.CTkLabel(
            container,
            text="Supprime l'historique des matchs et remet les statistiques à zéro.",
            font=("Segoe UI", 13),
            text_color=TEXT_SECONDARY,
        ).pack(
            anchor="w",
            padx=36,
            pady=(0, 20),
        )

        self.reset_button = RFButton(
            container,
            text="🗑 Réinitialiser les statistiques",
            color="#DC2626",
            hover="#B91C1C",
        )

        self.reset_button.pack(
            padx=36,
            pady=(0, 30),
        )
        
    def _entry(self, parent, text):

        RFLabel(
            parent,
            text,
        ).pack(
            anchor="w",
            pady=(0, 6),
        )

        entry = ctk.CTkEntry(
            parent,
            width=380,
            height=44,
            fg_color=SURFACE,
            border_color=BORDER,
            text_color=TEXT_PRIMARY,
            corner_radius=10,
            font=LABEL_FONT,
        )

        entry.pack(
            pady=(0, 18),
        )

        return entry
        return combo