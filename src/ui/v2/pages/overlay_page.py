import customtkinter as ctk
import webbrowser

from src.theme_v2 import CARD, BORDER, RADIUS


class OverlayPage(ctk.CTkFrame):

    URL = "http://127.0.0.1:4587/overlay/overlay.html"

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.grid_columnconfigure(0, weight=1)

        # ==========================================================
        # HEADER
        # ==========================================================

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=30,
            pady=(26, 20)
        )

        title_frame = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )
        title_frame.pack(
            side="left",
            fill="x",
            expand=True
        )

        ctk.CTkLabel(
            title_frame,
            text="🎥 Stream Overlay",
            font=("Segoe UI", 30, "bold"),
            text_color="white"
        ).pack(anchor="w")

        ctk.CTkLabel(
            title_frame,
            text="Configurez votre overlay OBS en quelques secondes.",
            font=("Segoe UI", 14),
            text_color="#97A0AF"
        ).pack(
            anchor="w",
            pady=(6, 0)
        )

        # ==========================================================
        # MAIN CARD
        # ==========================================================

        self.card = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER
        )

        self.card.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=30,
            pady=(0, 24)
        )

        self.card.grid_columnconfigure(0, weight=1)

        # ==========================================================
        # STATUS
        # ==========================================================

        status_frame = ctk.CTkFrame(
            self.card,
            fg_color="transparent"
        )

        status_frame.pack(
            fill="x",
            padx=28,
            pady=(26, 12)
        )

        ctk.CTkLabel(
            status_frame,
            text="🟢 Overlay prêt",
            font=("Segoe UI", 22, "bold"),
            text_color="white"
        ).pack(anchor="w")

        ctk.CTkLabel(
            status_frame,
            text="Le serveur local est prêt à être utilisé dans OBS.",
            font=("Segoe UI", 13),
            text_color="#97A0AF"
        ).pack(
            anchor="w",
            pady=(6, 0)
        )

        # ==========================================================
        # URL
        # ==========================================================

        ctk.CTkLabel(
            self.card,
            text="URL OBS",
            font=("Segoe UI", 15, "bold"),
            text_color="white"
        ).pack(
            anchor="w",
            padx=28,
            pady=(10, 8)
        )

        self.url_frame = ctk.CTkFrame(
            self.card,
            fg_color="#141923",
            border_width=1,
            border_color=BORDER,
            corner_radius=14
        )

        self.url_frame.pack(
            fill="x",
            padx=28
        )

        self.url_label = ctk.CTkLabel(
            self.url_frame,
            text=self.URL,
            anchor="w",
            padx=18,
            height=48,
            font=("Consolas", 13),
            text_color="white"
        )

        self.url_label.pack(
            fill="x"
        )

        # ==========================================================
        # ACTION BUTTONS
        # ==========================================================

        buttons = ctk.CTkFrame(
            self.card,
            fg_color="transparent"
        )

        buttons.pack(
            anchor="w",
            padx=28,
            pady=(22, 26)
        )

        self.copy_button = ctk.CTkButton(
            buttons,
            text="📋 Copier",
            width=165,
            height=42,
            corner_radius=12,
            command=self.copy_url
        )

        self.copy_button.pack(
            side="left",
            padx=(0, 12)
        )

        self.open_button = ctk.CTkButton(
            buttons,
            text="👁 Ouvrir",
            width=165,
            height=42,
            corner_radius=12,
            command=self.open_overlay
        )

        self.open_button.pack(
            side="left"
        )

        self.status = ctk.CTkLabel(
            self.card,
            text="",
            font=("Segoe UI", 12),
            text_color="#8B95A7"
        )

        self.status.pack(
            anchor="w",
            padx=30,
            pady=(0, 24)
        )

        # ==========================================================
        # SEPARATOR
        # ==========================================================

        separator = ctk.CTkFrame(
            self.card,
            fg_color=BORDER,
            height=1
        )

        separator.pack(
            fill="x",
            padx=28,
            pady=(0, 24)
        )

        # ==========================================================
        # OBS CONFIGURATION
        # ==========================================================

        config_title = ctk.CTkLabel(
            self.card,
            text="📺 Configuration OBS",
            font=("Segoe UI", 19, "bold"),
            text_color="white"
        )

        config_title.pack(
            anchor="w",
            padx=28
        )

        config_subtitle = ctk.CTkLabel(
            self.card,
            text="Ajoutez simplement cette URL dans une source navigateur OBS.",
            font=("Segoe UI", 13),
            text_color="#97A0AF"
        )

        config_subtitle.pack(
            anchor="w",
            padx=28,
            pady=(6, 18)
        )

        self.config_card = ctk.CTkFrame(
            self.card,
            fg_color="#141923",
            corner_radius=16,
            border_width=1,
            border_color=BORDER
        )

        self.config_card.pack(
            fill="x",
            padx=28,
            pady=(0, 28)
        )

        # ==========================================================
        # OBS SETTINGS
        # ==========================================================

        self._setting_row(
            self.config_card,
            "🌐",
            "Type de source",
            "Source navigateur"
        )

        self._setting_row(
            self.config_card,
            "📐",
            "Dimensions",
            "500 × 120 px"
        )

        info = ctk.CTkFrame(
            self.card,
            fg_color="#18212D",
            corner_radius=16,
            border_width=1,
            border_color=BORDER
        )

        info.pack(
            fill="x",
            padx=28,
            pady=(0, 28)
        )

        ctk.CTkLabel(
            info,
            text="💡 Astuce",
            font=("Segoe UI", 15, "bold"),
            text_color="white"
        ).pack(
            anchor="w",
            padx=18,
            pady=(16, 6)
        )

        ctk.CTkLabel(
            info,
            text=(
                "Ajoutez simplement cette URL dans une source navigateur "
                "OBS. Pensez à cocher « Actualiser lorsque la scène devient "
                "active » afin que l'overlay soit toujours synchronisé."
            ),
            wraplength=760,
            justify="left",
            font=("Segoe UI", 12),
            text_color="#97A0AF"
        ).pack(
            anchor="w",
            padx=18,
            pady=(0, 18)
        )

    # ==========================================================
    # HELPERS
    # ==========================================================

    def _setting_row(
        self,
        parent,
        icon,
        title,
        value
    ):

        row = ctk.CTkFrame(
            parent,
            fg_color="transparent",
            height=52
        )
        row.pack(
            fill="x",
            padx=18,
            pady=8
        )

        left = ctk.CTkFrame(
            row,
            fg_color="transparent"
        )
        left.pack(
            side="left",
            fill="x",
            expand=True
        )

        ctk.CTkLabel(
            left,
            text=icon,
            font=("Segoe UI Emoji", 18)
        ).pack(
            side="left",
            padx=(0, 12)
        )

        text = ctk.CTkFrame(
            left,
            fg_color="transparent"
        )
        text.pack(
            side="left",
            fill="x",
            expand=True
        )

        ctk.CTkLabel(
            text,
            text=title,
            font=("Segoe UI", 13, "bold"),
            text_color="white"
        ).pack(anchor="w")

        ctk.CTkLabel(
            text,
            text=value,
            font=("Segoe UI", 12),
            text_color="#97A0AF"
        ).pack(
            anchor="w",
            pady=(2, 0)
        )

        separator = ctk.CTkFrame(
            parent,
            fg_color=BORDER,
            height=1
        )

        separator.pack(
            fill="x",
            padx=18
        )

        # ==========================================================
    # ACTIONS
    # ==========================================================

    def copy_url(self):
        """Copie l'URL de l'overlay dans le presse-papiers."""

        self.clipboard_clear()
        self.clipboard_append(self.URL)
        self.update()

        self.status.configure(
            text="✓ URL copiée dans le presse-papiers",
            text_color="#4ADE80"
        )

        self.after(
            2500,
            lambda: self.status.configure(
                text="",
                text_color="#8B95A7"
            )
        )

    def open_overlay(self):
        """Ouvre l'overlay dans le navigateur par défaut."""

        try:
            webbrowser.open(self.URL)

            self.status.configure(
                text="✓ Overlay ouvert dans votre navigateur",
                text_color="#4ADE80"
            )

        except Exception as error:

            self.status.configure(
                text=f"Erreur : {error}",
                text_color="#EF4444"
            )

        self.after(
            3000,
            lambda: self.status.configure(
                text="",
                text_color="#8B95A7"
            )
        )