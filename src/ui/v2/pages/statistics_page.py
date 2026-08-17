import customtkinter as ctk

from src.theme_v2 import (
    BORDER,
    CARD,
    PADDING,
    RADIUS,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)

from src.ui.v2.progress_chart import create_progress_chart
from src.ui.v2.statistics.statistics_summary import (
    create_statistics_summary,
)
from src.ui.v2.statistics.statistics_kpi import create_statistics_kpis
from src.controllers.statistics_controller import (
    StatisticsController,
)

class StatisticsPage(ctk.CTkFrame):
    """Full statistics page."""

    def __init__(self, parent, context):
        super().__init__(parent, fg_color="transparent")

        self.context = context

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self._build_content()

        self.controller = StatisticsController(self)

    def _build_header(self):

        header = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=PADDING,
            pady=(PADDING, 12),
        )

        ctk.CTkLabel(
            header,
            text="STATISTIQUES",
            text_color=TEXT_PRIMARY,
            font=("Segoe UI", 26, "bold"),
        ).pack(anchor="w", padx=PADDING, pady=(PADDING, 2))

        ctk.CTkLabel(
            header,
            text="Analyse complète de tes performances.",
            text_color=TEXT_SECONDARY,
            font=("Segoe UI", 13),
        ).pack(anchor="w", padx=PADDING, pady=(0, PADDING))

    def _build_content(self):

        body = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )

        body.grid(
            row=1,
            column=0,
            sticky="nsew",
        )

        body.grid_columnconfigure(0, weight=3)
        body.grid_columnconfigure(1, weight=2)

        body.grid_rowconfigure(0, weight=0)   # KPI
        body.grid_rowconfigure(1, weight=1)   # Contenu principal

        kpi_frame, self.kpis = create_statistics_kpis(body)

        kpi_frame.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=PADDING,
            pady=(0, 16),
        )

        graph_container = ctk.CTkFrame(
            body,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
        )

        graph_container.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(PADDING, 8),
            pady=(0, PADDING),
        )

        chart, controller = create_progress_chart(graph_container)

        chart.pack(
            fill="both",
            expand=True,
        )

        stats_container = ctk.CTkFrame(
            body,
            fg_color=CARD,
            corner_radius=RADIUS,
            border_width=1,
            border_color=BORDER,
        )

        stats_container.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(8, PADDING),
            pady=(0, PADDING),
        )

        summary = create_statistics_summary(
            stats_container
        )

        summary.pack(
            fill="both",
            expand=True,
        )

        self.chart = controller
        self.summary = summary

    def refresh(self):
        self.controller.refresh()

        if self.chart:
            self.chart.refresh()