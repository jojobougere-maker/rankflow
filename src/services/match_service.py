from dataclasses import dataclass
from datetime import datetime

from src.database.models import Match
from src.database.repository import add_match, get_matches
from src.database.settings_repository import SettingsRepository
from src.controllers.overlay_controller import OverlayController


@dataclass
class MatchData:
    result: str
    sr: int


class MatchService:

    def __init__(self, dashboard=None, starting_sr: int = 0):
        self.dashboard = dashboard
        self.starting_sr = starting_sr
        self.settings = SettingsRepository()

    # -------------------------------------------------
    # Public API
    # -------------------------------------------------

    def save_match(self, data: dict) -> Match:

        match_data = MatchData(
            result=data["result"],
            sr=self._parse_sr(data["sr"]),
        )

        current_sr = self.get_current_sr()

        sr_change = (
            match_data.sr
            if match_data.result.lower() == "victory"
            else -match_data.sr
        )

        new_sr = current_sr + sr_change

        match = Match(
            played_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            result=match_data.result,
            sr_change=sr_change,
            sr_after=new_sr,
        )

        add_match(match)

        self.settings.update_sr(new_sr)

        OverlayController().refresh()

        if self.dashboard:
            self.dashboard.refresh()

        return match

    # -------------------------------------------------
    # Helpers
    # -------------------------------------------------

    def get_current_sr(self) -> int:

        settings = self.settings.get()

        if settings is None:
            return self.starting_sr

        return int(settings["current_sr"])

    @staticmethod
    def _parse_sr(value) -> int:

        return abs(
            int(
                str(value)
                .replace("+", "")
                .replace("-", "")
                .replace("SR", "")
                .strip()
            )
        )