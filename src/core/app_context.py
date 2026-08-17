from src.core.application_state import ApplicationState
from src.core.dashboard_controller import DashboardController

from src.services.match_service import MatchService
from src.services.rank_service import RankService

from src.database.settings_repository import SettingsRepository


class AppContext:

    def __init__(self):

        # Shared application state
        self.state = ApplicationState()

        self.dashboard = DashboardController(self.state)

        self.settings = SettingsRepository()
        self.rank_service = RankService()

        self.match_service = MatchService(
            dashboard=self.dashboard
        )