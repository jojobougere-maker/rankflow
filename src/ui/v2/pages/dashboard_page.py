import customtkinter as ctk

from src.theme_v2 import BORDER, CARD, RADIUS


class DashboardPage(ctk.CTkFrame):
    """Host the existing dashboard regions without owning their controllers."""

    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.regions = self._build_regions()

    def _build_regions(self):
        left = ctk.CTkFrame(self, fg_color="transparent", width=470)
        left.pack(side="left", fill="both", expand=True, padx=(0, 12))

        right = ctk.CTkFrame(self, fg_color="transparent")
        right.pack(side="left", fill="both", expand=True, padx=(6, 0))

        kpi = ctk.CTkFrame(right, fg_color="transparent")
        kpi.pack(fill="x", pady=(0, 20))

        graph = self._card(right, height=255)
        graph.pack(fill="x")
        graph.pack_propagate(False)

        bottom = ctk.CTkFrame(right, fg_color="transparent")
        bottom.pack(fill="both", expand=True, pady=(18, 0))

        history = self._card(bottom)
        history.pack(side="left", fill="both", expand=True, padx=(0, 12))

        stats = self._card(bottom)
        stats.pack(side="left", fill="both", expand=True)

        return {
            "left": left,
            "right": right,
            "kpi": kpi,
            "graph": graph,
            "history": history,
            "stats": stats,
        }

    @staticmethod
    def _card(parent, **options):
        return ctk.CTkFrame(
            parent,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
            **options,
        )
