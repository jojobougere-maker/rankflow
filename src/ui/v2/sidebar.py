import customtkinter as ctk

from src.theme_v2 import *


def create_sidebar(parent):

    sidebar = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=RADIUS,
        border_width=1,
        border_color=BORDER,
        width=180
    )

    sidebar.pack_propagate(False)


    title = ctk.CTkLabel(
        sidebar,
        text="",
        height=40
    )

    title.pack(
        pady=(30,20)
    )


    menu = [
        ("🏠", "Dashboard", "Tableau de bord"),
        ("📊", "Statistiques", "Statistiques"),
        ("🕒", "Historique", "Historique"),
        ("🎥", "Stream Overlay", "Stream Overlay"),
        ("⚙️", "Paramètres", "Paramètres"),
    ]


    buttons = {}


    for icon, key, label in menu:

        button = ctk.CTkButton(
            sidebar,
            text=f"{icon}   {label}",
            height=46,
            anchor="w",
            corner_radius=RADIUS_SMALL,
            fg_color="transparent",
            hover_color="#262D3D",
            text_color=TEXT
        )

        button.pack(
            fill="x",
            padx=PADDING_SECONDARY,
            pady=7
        )

        buttons[key] = button


    # Dashboard actif

    buttons["Dashboard"].configure(
        fg_color=PRIMARY
    )


    return sidebar, buttons
