import customtkinter as ctk

from src.theme_v2 import BACKGROUND, OUTER_MARGIN, PADDING_SECONDARY
from src.ui.v2.pages.dashboard_page import DashboardPage
from src.ui.v2.sidebar import create_sidebar


def create_layout(app):
    """Create the stable application shell and its initial DashboardPage."""
    app.configure(fg_color=BACKGROUND)

    root = ctk.CTkFrame(app, fg_color=BACKGROUND)
    root.pack(fill="both", expand=True)

    header = ctk.CTkFrame(root, fg_color="transparent", height=110)
    header.pack(fill="x", padx=OUTER_MARGIN, pady=(OUTER_MARGIN, PADDING_SECONDARY))
    header.pack_propagate(False)

    body = ctk.CTkFrame(root, fg_color="transparent")
    body.pack(fill="both", expand=True, padx=OUTER_MARGIN, pady=(0, OUTER_MARGIN))

    sidebar, sidebar_buttons = create_sidebar(body)
    sidebar.pack(side="left", fill="y", padx=(0, 4))
    sidebar.pack_propagate(False)

    page_container = ctk.CTkFrame(body, fg_color="transparent")
    page_container.pack(side="left", fill="both", expand=True)
    page_container.grid_rowconfigure(0, weight=1)
    page_container.grid_columnconfigure(0, weight=1)

    dashboard_page = DashboardPage(page_container)
    dashboard_page.grid(row=0, column=0, sticky="nsew")

    return {
        "root": root,
        "header": header,
        "sidebar": sidebar,
        "sidebar_buttons": sidebar_buttons,
        "content": page_container,
        "dashboard_page": dashboard_page,
        **dashboard_page.regions,
    }
