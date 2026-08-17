import customtkinter as ctk

from src.theme_v2 import *


class RFCard(ctk.CTkFrame):

    def __init__(self, parent, **kwargs):

        super().__init__(
            parent,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
            **kwargs
        )

class RFStatCard(RFCard):

    def __init__(
        self,
        parent,
        icon,
        title,
        value,
        accent,
        badge,
        subtitle
    ):

        super().__init__(parent)

        self.configure(
            width=340,
            height=170,
            fg_color=CARD,
            corner_radius=18,
            border_width=1,
            border_color=BORDER
        )

        self.icon = icon
        self.title = title
        self.value = value
        self.accent = accent
        self.badge = badge
        self.subtitle = subtitle

        self.pack_propagate(False)
        self.grid_propagate(False)

        self._build()

    def _build(self):

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.grid_columnconfigure(0, weight=1)

class RFSectionTitle(ctk.CTkLabel):

    def __init__(self, parent, text):

        super().__init__(
            parent,
            text=text,
            font=SUBTITLE_FONT,
            text_color=TEXT_PRIMARY
        )


class RFValue(ctk.CTkLabel):

    def __init__(self, parent, text):

        super().__init__(
            parent,
            text=text,
            font=VALUE_FONT,
            text_color=TEXT_PRIMARY
        )


class RFLabel(ctk.CTkLabel):

    def __init__(self, parent, text):

        super().__init__(
            parent,
            text=text,
            font=LABEL_FONT,
            text_color=TEXT_SECONDARY
        )


class RFProgress(ctk.CTkProgressBar):

    def __init__(self, parent):

        super().__init__(
            parent,
            height=14,
            corner_radius=999,
            border_width=0,
            progress_color="#7C5CFF",
            fg_color="#2C3240"
        )

class RFButton(ctk.CTkButton):

    def __init__(
        self,
        parent,
        text,
        color,
        hover,
        command=None,
        **kwargs
    ):

        super().__init__(
            parent,
            text=text,
            width=150,
            height=48,
            corner_radius=6,
            border_width=1,
            fg_color=color,
            hover_color=hover,
            font=("Segoe UI", 15, "bold"),
            command=command,
            **kwargs
        )