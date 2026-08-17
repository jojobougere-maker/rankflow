"""
dashboard_controller.py

Contrôleur principal du dashboard RankFlow.

Son rôle est de synchroniser tous les widgets après
une modification des données (nouveau match, reset,
changement de saison, etc.).

L'UI ne dialogue jamais directement avec la base de
données : tout passe par ce contrôleur.
"""
from src.controllers.overlay_controller import OverlayController

class DashboardController:
    def __init__(
        self,
        sr_card=None,
        history_card=None,
        stats_card=None,
        kpi_card=None,
    ):
        self.sr_card = sr_card
        self.history_card = history_card
        self.stats_card = stats_card
        self.kpi_card = kpi_card
        self.statistics_page = None

        self.overlay = OverlayController()

    # -------------------------------------------------
    # Public API
    # -------------------------------------------------

    def refresh(self):
        """
        Rafraîchit complètement le dashboard.
        """
        self.refresh_sr()
        self.refresh_history()
        self.refresh_stats()
        self.refresh_kpis()

        if self.statistics_page:
            self.statistics_page.refresh()

        self.overlay.refresh()

    # -------------------------------------------------
    # Sections
    # -------------------------------------------------

    def refresh_sr(self):
        """
        Rafraîchit la carte SR.
        """
        if (
            self.sr_card
            and hasattr(self.sr_card, "refresh")
        ):
            self.sr_card.refresh()

    def refresh_history(self):
        """
        Rafraîchit l'historique.
        """
        if (
            self.history_card
            and hasattr(self.history_card, "refresh")
        ):
            self.history_card.refresh()

    def refresh_stats(self):
        """
        Rafraîchit les statistiques.
        """
        if (
            self.stats_card
            and hasattr(self.stats_card, "refresh")
        ):
            self.stats_card.refresh()

    def refresh_kpis(self):
        """
        Rafraîchit les KPI.
        """
        if (
            self.kpi_card
            and hasattr(self.kpi_card, "refresh")
        ):
            self.kpi_card.refresh()

    # -------------------------------------------------
    # Registration
    # -------------------------------------------------

    def register_sr_card(self, widget):
        self.sr_card = widget

    def register_history_card(self, widget):
        self.history_card = widget

    def register_stats_card(self, widget):
        self.stats_card = widget

    def register_kpi_card(self, widget):
        self.kpi_card = widget

    def register_statistics_page(self, page):
        self.statistics_page = page