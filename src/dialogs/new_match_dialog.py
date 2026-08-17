import customtkinter as ctk

from src.theme_v2 import (
    BACKGROUND,
    CARD,
    BORDER,
    PRIMARY,
    TEXT,
    TEXT_SECONDARY,
    RADIUS,
)


class NewMatchDialog(ctk.CTkToplevel):

    def __init__(
        self,
        parent,
        result="Victory",
        on_save=None,
    ):

        super().__init__(parent)

        self.result = result

        self.on_save = on_save

        self.title("Nouvelle partie")

        self.geometry("560x500")

        self.resizable(False, False)

        self.grab_set()

        self.focus_force()

        self._build()
        self.bind("<Return>", self._save_on_enter)


    def _build(self):

        self.configure(fg_color="#0F1117")

        # ===== Header =====

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 15)
        )

        title = ctk.CTkLabel(
            header,
            text="🏆 Nouvelle partie",
            font=("Segoe UI", 24, "bold"),
            text_color="white"
        )

        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Enregistre rapidement ton dernier match",
            font=("Segoe UI", 13),
            text_color="#9CA3AF"
        )

        subtitle.pack(anchor="w", pady=(4, 0))

        # ===== Contenu =====

        self.content = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.content.pack(
            fill="both",
            expand=True,
            padx=30
        )

        result_title = ctk.CTkLabel(
            self.content,
            text="Résultat",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT
        )

        result_title.pack(anchor="w", pady=(0, 12))

        buttons = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        buttons.pack(fill="x", pady=(0, 25))

        self.victory_button = ctk.CTkButton(
            buttons,
            text="🟢 Victoire",
            height=46,
            fg_color="#22C55E",
            hover_color="#16A34A"
        )

        self.victory_button.pack(
            side="left",
            expand=True,
            fill="x",
            padx=(0, 8)
        )

        self.defeat_button = ctk.CTkButton(
            buttons,
            text="🔴 Défaite",
            height=46,
            fg_color="#2A3142",
            hover_color="#343C50"
        )

        self.defeat_button.pack(
            side="left",
            expand=True,
            fill="x",
            padx=(8, 0)
        )

        if self.result == "Victory":
            self.victory_button.configure(
                fg_color="#22C55E"
            )
            self.defeat_button.configure(
                fg_color="#2A3142"
            )
        else:
            self.victory_button.configure(
                fg_color="#2A3142"
            )
            self.defeat_button.configure(
                fg_color="#EF4444"
            )

        # ==========================
        # SR
        # ==========================

        sr_title = ctk.CTkLabel(
            self.content,
            text="SR gagné / perdu",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT
        )

        sr_title.pack(
            anchor="w",
            pady=(0, 10)
        )

        self.sr_entry = ctk.CTkEntry(
            self.content,
            height=44,
            corner_radius=12,
            placeholder_text="Ex : +28 ou -25"
        )

        self.sr_entry.pack(
            fill="x",
            pady=(0, 22)
        )

        # ===== Footer =====

        footer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        footer.pack(
            fill="x",
            padx=30,
            pady=(15, 25)
        )

        cancel_button = ctk.CTkButton(
            footer,
            text="Annuler",
            width=120,
            fg_color="#2A3142",
            hover_color="#343C50",
            command=self.destroy
        )

        cancel_button.pack(
            side="left"
        )

        save_button = ctk.CTkButton(
            footer,
            text="Enregistrer",
            width=160,
            fg_color="#8B5CF6",
            hover_color="#7C5CFF",
            command=self.save_match
        )

        save_button.pack(
            side="right"
        )

    def _save_on_enter(self, _event):
        """Submit through the same path as the Enregistrer button."""
        self.save_match()
        return "break"

    def save_match(self):

        sr = self.sr_entry.get().strip()

        if not sr:
            return

        data = {
            "result": self.result,
            "sr": sr,
        }

        if self.on_save:
            self.on_save(data)

        self.destroy()
