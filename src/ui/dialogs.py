import customtkinter as ctk

from src.settings import save_settings
from src.storage import save_session

def open_settings(app, session, settings, refresh_ui):

    window = ctk.CTkToplevel(app)
    window.transient(app)
    window.attributes("-topmost", True)

    window.after(100, lambda: window.attributes("-topmost", False))
    window.after(100, window.focus_force)
    window.after(100, window.grab_set)
    window.title("Paramètres")
    window.geometry("420x380")
    window.resizable(False, False)

    ctk.CTkLabel(
        window,
        text="⚙ Paramètres",
        font=("Arial", 24, "bold")
    ).pack(pady=20)

    # Joueur
    ctk.CTkLabel(window, text="Nom du joueur").pack()

    player_entry = ctk.CTkEntry(window, width=250)
    player_entry.insert(0, settings["player"])
    player_entry.pack(pady=5)

    # Objectif
    ctk.CTkLabel(window, text="Objectif SR").pack()

    goal_entry = ctk.CTkEntry(window, width=250)
    goal_entry.insert(0, str(settings["goal"]))
    goal_entry.pack(pady=5)

    # Sons
    sounds_var = ctk.BooleanVar(value=settings["sounds"])

    ctk.CTkCheckBox(
        window,
        text="Activer les sons",
        variable=sounds_var
    ).pack(pady=8)

    # Animations
    animations_var = ctk.BooleanVar(value=settings["animations"])

    ctk.CTkCheckBox(
        window,
        text="Activer les animations",
        variable=animations_var
    ).pack(pady=8)

    def save():

        settings["player"] = player_entry.get()
        new_goal = int(goal_entry.get())

        settings["goal"] = new_goal
        session.goal = new_goal

        settings["sounds"] = sounds_var.get()
        settings["animations"] = animations_var.get()

        save_settings(settings)
        save_session(session)

        refresh_ui()

        window.destroy()

    ctk.CTkButton(
        window,
        text="💾 Enregistrer",
        command=save
    ).pack(pady=25)