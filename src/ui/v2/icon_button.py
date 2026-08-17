import customtkinter as ctk
from PIL import Image
from src.theme_v2 import ICON_SIZE
from src.utils.resource_path import resource_path


def create_icon_button(parent, image_path, command=None):

    icon = ctk.CTkImage(
        light_image=Image.open(resource_path(image_path)),
        dark_image=Image.open(resource_path(image_path)),
        size=(ICON_SIZE, ICON_SIZE)
    )

    button = ctk.CTkButton(
        parent,
        image=icon,
        text="",
        width=34,
        height=34,
        corner_radius=17,
        fg_color="#1B2230",
        hover_color="#2A3245",
        border_width=1,
        border_color="#2F384B",
        command=command
    )

    button.image = icon

    return button
