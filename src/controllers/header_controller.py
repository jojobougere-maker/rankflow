from src.database.settings_repository import SettingsRepository
import customtkinter as ctk
from PIL import Image

from src.services.rank_service import RankService
from src.analytics.statistics import current_sr
from src.utils.resource_path import resource_path


class HeaderController:

    def __init__(self, widgets):
        self.widgets = widgets
        self.settings = SettingsRepository()
        self.rank_service = RankService()

    def refresh(self):

        settings = self.settings.get()

        self.widgets["player_name"].configure(
            text=settings["activision_name"] or "Player"
        )

        rank = self.rank_service.get_rank(current_sr())

        avatar_image = ctk.CTkImage(
            light_image=Image.open(resource_path(rank.icon)),
            dark_image=Image.open(resource_path(rank.icon)),
            size=(46, 46),
        )

        self.widgets["player_avatar"].configure(
            image=avatar_image
        )

        # Très important : conserver une référence
        self.widgets["player_avatar"].image = avatar_image