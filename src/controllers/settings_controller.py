from src.database.settings_repository import SettingsRepository

from tkinter import messagebox

from src.database.repository import clear_matches
from src.controllers.overlay_controller import OverlayController


class SettingsController:

    def __init__(self, page, dashboard, header_ui, router,):

        self.router = router

        self.header_ui = header_ui

        self.page = page
        self.dashboard = dashboard

        self.repository = SettingsRepository()

        self.load()

        self.page.save_button.configure(
            command=self.save
        )

        self.page.reset_button.configure(
            command=self.reset_statistics
        )

        self.page.username.bind(
            "<Return>",
            lambda event: self.save()
        )

        self.page.current_sr.bind(
            "<Return>",
            lambda event: self.save()
        )

        self.page.goal_sr.bind(
            "<Return>",
            lambda event: self.save()
        )

    # ----------------------------------
    # Chargement
    # ----------------------------------

    def load(self):

        settings = self.repository.get()

        self.page.username.delete(0, "end")
        self.page.username.insert(
            0,
            settings["activision_name"]
        )

        self.page.current_sr.delete(0, "end")
        self.page.current_sr.insert(
            0,
            str(settings["current_sr"])
        )

        self.page.goal_sr.delete(0, "end")
        self.page.goal_sr.insert(
            0,
            str(settings["goal_sr"])
        )

    # ----------------------------------
    # Sauvegarde
    # ----------------------------------

    def save(self):

        self.page.after(
            1000,
            self.go_dashboard
        )

        self.repository.update_name(
            self.page.username.get()
        )

        self.repository.update_sr(
            int(self.page.current_sr.get())
        )

        self.repository.update_goal(
            int(self.page.goal_sr.get())
        )

        OverlayController().refresh()

        self.header_ui["player_name"].configure(
            text=self.page.username.get()
        )

        self.dashboard.refresh()

        self.page.status.configure(
            text="✓ Paramètres enregistrés\nRetour au tableau de bord..."
        )

    def go_dashboard(self):

        self.page.status.configure(text="")

        self.router.show("Dashboard")

    def reset_statistics(self):

        confirm = messagebox.askyesno(
            "Réinitialiser",
            (
                "Supprimer tout l'historique des matchs ?\n\n"
                "Les paramètres seront conservés."
            ),
        )

        if not confirm:
            return

        clear_matches()

        self.dashboard.refresh()

        OverlayController().refresh()

        self.page.status.configure(
            text="✓ Statistiques réinitialisées",
            text_color="#4ADE80",
        )
