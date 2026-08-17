import customtkinter as ctk
from PIL import Image

from src.ui.v2.layout import create_layout
from src.ui.v2.navigation import PageRouter
from src.ui.v2.pages.placeholder_page import PlaceholderPage
from src.ui.v2.pages.history_page import HistoryPage
from src.ui.v2.header import create_header
from src.ui.v2.cards.sr_card import create_sr_card
from src.ui.v2.cards.kpi import create_kpi_grid
from src.ui.v2.progress_chart import create_progress_chart
from src.ui.v2.cards.history_card import create_history_card
from src.ui.v2.cards.stats_card import create_stats_card
from src.database.migrations import initialize_database
from src.core.app_context import AppContext
from src.ui.v2.pages.settings_page import SettingsPage
from src.controllers.settings_controller import SettingsController
from src.ui.v2.pages.statistics_page import StatisticsPage
from src.controllers.header_controller import HeaderController
from src.utils.resource_path import resource_path
from src.services.overlay_server import OverlayServer
from src.ui.v2.pages.overlay_page import OverlayPage
from src.core.version import APP_VERSION
from src.services.updater import check_for_update, install_update

import os
import sys

def resource_path(relative_path):
    """Retourne le bon chemin en développement et après compilation."""
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

initialize_database()

context = AppContext()

app = ctk.CTk()

app.title("RankFlow")
app.iconbitmap(resource_path("assets/icon.ico"))

app.geometry("1600x1180")

logo = ctk.CTkImage(
    light_image=Image.open(resource_path("assets/ranks/header_logo.png")),
    dark_image=Image.open(resource_path("assets/ranks/header_logo.png")),
    size=(76, 76)
)

layout = create_layout(app)

router = PageRouter(layout["sidebar_buttons"])
router.register("Dashboard", layout["dashboard_page"])

router.register(
    "Historique",
    HistoryPage(
        layout["content"],
        context
    )
)

overlay_page = OverlayPage(
    layout["content"]
)

router.register(
    "Stream Overlay",
    overlay_page,
)

statistics_page = StatisticsPage(
    layout["content"],
    context,
)

context.dashboard.register_statistics_page(
    statistics_page
)

router.register(
    "Statistiques",
    statistics_page,
)

settings_page = SettingsPage(
    layout["content"]
)

router.register(
    "Paramètres",
    settings_page
)

router.show("Dashboard")

settings = context.settings.get()

player_name = settings["activision_name"] or "Joueur"

header, header_ui = create_header(
    layout["header"],
    logo,
    player_name
)

header_ui["settings_button"].configure(
    command=lambda: router.show("Paramètres")
)

header.pack(fill="x", padx=20, pady=20)

header_controller = HeaderController(header_ui)

context.dashboard.register_header(header_controller)

settings_controller = SettingsController(
    settings_page,
    context.dashboard,
    header_ui,
    router
)

sr_card, sr_controller = create_sr_card(
    layout["left"],
    context,
)

context.dashboard.register_sr_card(sr_controller)

_, kpi_controller = create_kpi_grid(
    layout["kpi"]
)

kpi_controller.set_header_widgets(header_ui["kpi_values"])

context.dashboard.register_kpi_card(
    kpi_controller
)

chart, chart_controller = create_progress_chart(
    layout["graph"],
    compact=True,
)

context.dashboard.register_chart_controller(chart_controller)

chart.pack(
    fill="both",
    expand=True
)

history = create_history_card(layout["history"])
history.pack(
    fill="both",
    expand=True
)

context.dashboard.register_history_card(history)

stats = create_stats_card(layout["stats"])
stats.pack(
    fill="both",
    expand=True
)

context.dashboard.register_stats_card(stats)

context.dashboard.refresh()

overlay_server = OverlayServer()
overlay_server.start()


def handle_update_result(update_info):
    if not update_info:
        return

    latest = update_info["version"]

    from tkinter import messagebox

    if not messagebox.askyesno(
        "Mise à jour disponible",
        (
            f"RankFlow v{latest} est disponible.\\n\\n"
            "Voulez-vous télécharger et installer la mise à jour maintenant ?"
        ),
        parent=app,
    ):
        return

    def on_update_error(error):
        app.after(
            0,
            lambda: messagebox.showerror(
                "Mise à jour impossible",
                f"Impossible d'installer la mise à jour.\\n\\n{error}",
                parent=app,
            ),
        )

    def do_update():
        if install_update(update_info, on_error=on_update_error):
            app.after(0, app.destroy)

    import threading
    threading.Thread(
        target=do_update,
        daemon=True,
        name="RankFlowUpdateInstall",
    ).start()


def schedule_update_check():
    def result_callback(update_info):
        app.after(0, lambda: handle_update_result(update_info))

    check_for_update(APP_VERSION, result_callback)


app.after(1500, schedule_update_check)

app.mainloop()
