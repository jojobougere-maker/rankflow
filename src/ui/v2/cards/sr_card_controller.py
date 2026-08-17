from PIL import Image
import customtkinter as ctk

from src.analytics.statistics import current_sr
from src.database.settings_repository import SettingsRepository
from src.services.rank_service import RankService
from src.utils.resource_path import resource_path


class SRCardController:

    def __init__(self, widgets):
        self.widgets = widgets
        self.rank_service = RankService()
        self.settings = SettingsRepository()

    def refresh(self):

        settings = self.settings.get()

        sr = current_sr()
        goal = int(settings["goal_sr"])

        rank = self.rank_service.get_rank(sr)
        next_rank = self.rank_service.next_rank(sr)

        # -----------------------
        # Logo du rang
        # -----------------------

        image = ctk.CTkImage(
            light_image=Image.open(resource_path(rank.icon)),
            dark_image=Image.open(resource_path(rank.icon)),
            size=(150, 150),
        )

        self.widgets["icon"].configure(image=image)
        self.widgets["icon"].image = image

        # -----------------------
        # Nom du rang
        # -----------------------

        self.widgets["rank_name"].configure(
            text=rank.name
        )

        # -----------------------
        # SR
        # -----------------------

        self.widgets["sr"].configure(
            text=f"{sr:,} SR".replace(",", " ")
        )

        # -----------------------
        # Progression du rang
        # -----------------------

        progress = self.rank_service.progress(sr)

        self.widgets["progress"].set(progress)

        remaining = self.rank_service.remaining(sr)

        if next_rank:

            next_image = ctk.CTkImage(
                light_image=Image.open(resource_path(next_rank.icon)),
                dark_image=Image.open(resource_path(next_rank.icon)),
                size=(56, 56),
            )

            self.widgets["next_rank_icon"].configure(
                image=next_image
            )
            self.widgets["next_rank_icon"].image = next_image

            self.widgets["next_rank_text"].configure(
                text=next_rank.name
            )

        if rank.name == "Iridescent":
            self.widgets["next_rank"].configure(
                text="Rang maximum atteint"
            )

            self.widgets["progress_label"].configure(
                text=""
            )

            top250 = ctk.CTkImage(
                light_image=Image.open(resource_path("assets/ranks/top250.png")),
                dark_image=Image.open(resource_path("assets/ranks/top250.png")),
                size=(56, 56),
            )

            self.widgets["next_rank_icon"].configure(
                image=top250
            )
            self.widgets["next_rank_icon"].image = top250

            self.widgets["next_rank_text"].configure(
                text="Top 250"
            )

        else:
            self.widgets["next_rank"].configure(
                text=f"Encore {remaining} SR pour le rang suivant"
            )

            self.widgets["progress_label"].configure(
                text=f"{remaining} SR restants"
            )

        # -----------------------
        # Objectif personnel
        # -----------------------

        self.widgets["goal"].configure(
            text=f"{goal:,} SR".replace(",", " ")
        )

        ratio = min(sr / goal, 1) if goal > 0 else 0

        self.widgets["goal_progress"].set(ratio)

        self.widgets["goal_percent"].configure(
            text=f"{int(ratio*100)} %"
        )

        if ratio >= 1:
            message = "🎉 Objectif atteint !"
        elif ratio >= 0.75:
            message = "Objectif presque atteint"
        elif ratio >= 0.50:
            message = "Tu tiens le rythme"
        elif ratio >= 0.25:
            message = "Tu progresses bien"
        else:
            message = "Objectif lancé"

        self.widgets["goal_message"].configure(
            text=message
        )