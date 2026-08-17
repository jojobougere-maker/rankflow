import customtkinter as ctk

from src.theme_v2 import *
from src.ui.v2.sidebar import create_sidebar


def create_layout(app):

    app.configure(
        fg_color=BACKGROUND
    )

    # ==========================
    # ROOT
    # ==========================

    root = ctk.CTkFrame(
        app,
        fg_color=BACKGROUND
    )

    root.pack(
        fill="both",
        expand=True
    )


    # ==========================
    # HEADER
    # ==========================

    header = ctk.CTkFrame(
        root,
        fg_color="transparent",
        height=110
    )

    header.pack(
        fill="x",
        padx=25,
        pady=(20,10)
    )

    header.pack_propagate(False)


    # ==========================
    # BODY
    # ==========================

    body = ctk.CTkFrame(
        root,
        fg_color="transparent"
    )

    body.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=(0,25)
    )


    # ==========================
    # SIDEBAR
    # ==========================

    sidebar, sidebar_buttons = create_sidebar(body)

    sidebar.pack(
        side="left",
        fill="y",
        padx=(0,20)
    )

    sidebar.pack_propagate(False)


    # ==========================
    # ZONE PRINCIPALE
    # ==========================

    dashboard = ctk.CTkFrame(
        body,
        fg_color="transparent"
    )

    dashboard.pack(
        side="left",
        fill="both",
        expand=True
    )


    # ==========================
    # HAUT DASHBOARD
    # ==========================

    main_top = ctk.CTkFrame(
        dashboard,
        fg_color="transparent"
    )

    main_top.pack(
        fill="x",
        pady=(0,10)
    )


    # SR CARD

    left = ctk.CTkFrame(
        main_top,
        fg_color="transparent",
        width=380
    )

    left.pack(
        side="left",
        fill="both",
        padx=(0,20)
    )

    left.pack_propagate(False)



    # DROITE

    right = ctk.CTkFrame(
        main_top,
        fg_color="transparent"
    )

    right.pack(
        side="left",
        fill="both",
        expand=True
    )


    # KPI

    kpi = ctk.CTkFrame(
        right,
        fg_color="transparent"
    )

    kpi.pack(
        fill="x"
    )


    # GRAPH

    graph = ctk.CTkFrame(
        right,
        fg_color=CARD,
        corner_radius=RADIUS,
        height=170
    )

    graph.pack(
        fill="x",
        pady=10
    )

    graph.pack_propagate(False)


    # ==========================
    # BAS
    # ==========================

    bottom = ctk.CTkFrame(
        dashboard,
        fg_color="transparent",
        height=260
    )

    bottom.pack_propagate(False)

    bottom.pack(
        fill="x",
        pady=(0,10)
    )



    history = ctk.CTkFrame(
        bottom,
        fg_color=CARD,
        corner_radius=RADIUS
    )

    history.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0,10)
    )


    stats = ctk.CTkFrame(
        bottom,
        fg_color=CARD,
        corner_radius=RADIUS
    )

    stats.pack(
        side="left",
        fill="both",
        expand=True
    )


    return {

        "root": root,

        "header": header,

        "sidebar": sidebar,

        "content": dashboard,

        "left": left,

        "kpi": kpi,

        "graph": graph,

        "history": history,

        "stats": stats,

    }