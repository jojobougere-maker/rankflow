from src.core.application_state import ApplicationState


class DashboardController:
    def __init__(self, state):
        self.state = state

        self._sr_card = None
        self._history_cards = []
        self._stats_card = None
        self._kpi_card = None
        self.statistics_page = None
        self._header = None

    # ==========================
    # Register UI
    # ==========================

    def register_sr_card(self, card):
        self._sr_card = card

    def register_history_card(self, card):
        if card not in self._history_cards:
            self._history_cards.append(card)

    def register_stats_card(self, card):
        self._stats_card = card

    def register_kpi_card(self, card):
        self._kpi_card = card

    def register_statistics_page(self, page):
        self.statistics_page = page

    def register_chart_controller(self, controller):
        self._chart_controller = controller

    def register_header(self, controller):
        self._header = controller

    # ==========================
    # Refresh
    # ==========================

    def refresh(self):

        if self._sr_card:
            self._sr_card.refresh()

        for card in self._history_cards:
            card.refresh()

        if self._stats_card:
            self._stats_card.refresh()

        if self._kpi_card:
            self._kpi_card.refresh()

        if self._chart_controller:
            self._chart_controller.refresh()

        if self.statistics_page:
            self.statistics_page.refresh()

        if self._header:
            self._header.refresh()
