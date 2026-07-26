import customtkinter as ctk


def create_layout(app):

    # =========================
    # Conteneur principal
    # =========================

    content = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )

    content.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # =========================
    # Ligne du haut
    # =========================

    top = ctk.CTkFrame(
        content,
        fg_color="transparent"
    )

    top.pack(
        fill="both",
        expand=True
    )

    # =========================
    # Colonne gauche
    # =========================

    left = ctk.CTkFrame(
        top,
        fg_color="transparent",
        width=420
    )

    left.pack(
        side="left",
        fill="y",
        padx=(0, 20)
    )

    left.pack_propagate(False)

    # =========================
    # Colonne droite
    # =========================

    right = ctk.CTkFrame(
        top,
        fg_color="transparent"
    )

    right.pack(
        side="left",
        fill="both",
        expand=True
    )

    # =========================
    # KPI
    # =========================

    kpi = ctk.CTkFrame(
        right,
        fg_color="transparent",
        height=170
    )

    kpi.pack(
        fill="x"
    )

    kpi.pack_propagate(False)

    # =========================
    # Graphique
    # =========================

    graph = ctk.CTkFrame(
        right,
        corner_radius=18
    )

    graph.pack(
        fill="both",
        expand=True,
        pady=(20, 0)
    )

    # =========================
    # Bas
    # =========================

    bottom = ctk.CTkFrame(
        content,
        fg_color="transparent",
        height=260
    )

    bottom.pack(
        fill="both",
        pady=(20, 0)
    )

    bottom.pack_propagate(False)

    history = ctk.CTkFrame(
        bottom
    )

    history.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 10)
    )

    stats = ctk.CTkFrame(
        bottom
    )

    stats.pack(
        side="left",
        fill="both",
        expand=True
    )

    return {

        "content": content,

        "left": left,

        "right": right,

        "kpi": kpi,

        "graph": graph,

        "history": history,

        "stats": stats,

    }