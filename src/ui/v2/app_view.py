import customtkinter as ctk

from src.ui.v2.layout import create_layout
from src.ui.v2.header import create_header
from src.ui.v2.sr_card import create_sr_card
from src.ui.v2.kpi import create_kpi_grid


def create_app_view(app, logo_image, player_name="Josh"):

    layout = create_layout(app)

    # ==========================
    # HEADER
    # ==========================

    header, header_ui = create_header(
        layout["content"],
        logo_image,
        player_name
    )

    header.pack(
        fill="x",
        padx=20,
        pady=(20, 15)
    )

    # ==========================
    # SR CARD
    # ==========================

    sr_card, sr_ui = create_sr_card(
        layout["left"]
    )

    sr_card.pack(
        fill="both",
        expand=True
    )

    # ==========================
    # KPI
    # ==========================

    kpi_parent, kpi_ui = create_kpi_grid(
        layout["kpi"]
    )

    return {
        "layout": layout,
        "header": header_ui,
        "sr": sr_ui,
        "kpi": kpi_ui,
    }