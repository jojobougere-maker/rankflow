import customtkinter as ctk
from PIL import Image
from src.services.rank_service import RankService
from src.analytics.statistics import current_sr
from src.utils.resource_path import resource_path


def create_avatar(parent, size=56):

    rank = RankService().get_rank(current_sr())

    avatar_image = ctk.CTkImage(
        light_image=Image.open(resource_path(rank.icon)),
        dark_image=Image.open(resource_path(rank.icon)),
        size=(size, size)
    )

    avatar = ctk.CTkLabel(
        parent,
        image=avatar_image,
        text=""
    )

    avatar.image = avatar_image

    return avatar