from src.database.repository import get_matches


class StatisticsController:

    def __init__(self, page):

        self.page = page

    def refresh(self):

        matches = get_matches()

        total = len(matches)

        wins = sum(
            1
            for match in matches
            if match["result"].lower() == "victory"
        )

        losses = total - wins

        winrate = (
            round((wins / total) * 100, 1)
            if total
            else 0
        )

        self.page.kpis["Winrate"].set_value(
            f"{winrate} %"
        )

        self.page.kpis["Victoires"].set_value(
            wins
        )

        self.page.kpis["Défaites"].set_value(
            losses
        )

        self.page.kpis["Parties"].set_value(
            total
        )

        peak_sr = 0
        sr_gain = 0

        if matches:

            peak_sr = max(
                match["sr_after"]
                for match in matches
            )

            sr_gain = sum(
                match["sr_change"]
                for match in matches
            )

        current_sr = self.page.context.settings.get()["current_sr"]

        goal_sr = self.page.context.settings.get()["goal_sr"]

        goal_percent = (
            round((current_sr / goal_sr) * 100)
            if goal_sr
            else 0
        )

        self.page.summary.set_value(
            "🏆 Peak SR",
            peak_sr,
        )

        self.page.summary.set_value(
            "📈 SR gagné",
            f"{sr_gain:+}",
        )

        self.page.summary.set_value(
            "🎯 Objectif",
            f"{goal_percent} %",
        )