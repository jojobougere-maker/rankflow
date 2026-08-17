from datetime import datetime, timedelta

from src.analytics.statistics import sr_history

from src.database.settings_repository import SettingsRepository

_settings = SettingsRepository()


class ProgressChartController:

    def __init__(self, widgets, compact=False):

        self.widgets = widgets
        self.filter = "7J"
        self.compact = compact

    def refresh(self):

        chart = self.build_chart_data()

        self.widgets["chart"] = chart

        self._update_buttons()

        self.widgets["draw"](chart)

    def set_filter(self, value):

        self.filter = value
        self.refresh()

    def build_chart_data(self):

        history = self._apply_filter(sr_history())

        if not history:
            return None

        values = [item["sr"] for item in history]

        minimum = min(values)
        maximum = max(values)

        goal_sr = _settings.get()["goal_sr"]

        if self.compact:

            # Dashboard : zoom sur les derniers SR
            span = max(maximum - minimum, 1)

            padding = max(span * 0.35, 75)

            minimum -= padding
            maximum += padding

            # On arrondit les bornes à 25 SR
            minimum = int(minimum // 25) * 25
            maximum = int((maximum + 24) // 25) * 25
        else:
            # Statistiques : inclure l'objectif
            minimum = min(minimum, goal_sr)
            maximum = max(maximum, goal_sr)

            padding = max((maximum - minimum) * 0.10, 50)

            minimum -= padding
            maximum += padding

        dates = []

        for item in history:

            try:
                dates.append(
                    datetime.fromisoformat(
                        item["date"]
                    ).strftime("%d/%m")
                )

            except Exception:

                dates.append("")

        matches = len(history)

        wins = sum(
            1
            for item in history
            if item["result"] == "Victory"
        )

        winrate = (
            round((wins / matches) * 100)
            if matches
            else 0
        )

        gain = sum(item["change"] for item in history)

        return {
            "history": history,
            "values": values,
            "dates": dates,
            "minimum": minimum,
            "maximum": maximum,
            "current_sr": values[-1],
            "goal_sr": goal_sr,
            "matches": matches,
            "winrate": winrate,
            "gain": gain,
        }

    def _apply_filter(self, history):

        if self.filter == "TOUT":
            return history

        days = {
            "7J": 7,
            "30J": 30,
            "90J": 90,
        }.get(self.filter)

        if days is None:
            return history

        limit = datetime.now() - timedelta(days=days)

        filtered = []

        for match in history:

            try:

                date = datetime.fromisoformat(match["date"])

                if date >= limit:
                    filtered.append(match)

            except Exception:
                pass

        return filtered if filtered else history

    def _update_buttons(self):

        for name, button in self.widgets["buttons"].items():

            if name == self.filter:

                button.configure(
                    fg_color="#A855F7"
                )

            else:

                button.configure(
                    fg_color="#232838"
                )