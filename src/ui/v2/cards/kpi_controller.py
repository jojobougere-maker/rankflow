from src.analytics.statistics import (
    best_winstreak,
    current_sr,
    current_winstreak,
    current_winrate,
    session_sr,
    total_losses,
    total_matches,
    total_wins,
)


class KPICardController:
    """Keep the KPI grid and the header capsule in sync from one snapshot."""

    def __init__(self, widgets):
        self.widgets = widgets
        self.header_widgets = None

    def set_header_widgets(self, widgets):
        """Attach the header values without changing the dashboard API."""
        self.header_widgets = widgets

    def refresh(self):
        snapshot = self._statistics_snapshot()
        self._refresh_grid(snapshot)
        self._refresh_header(snapshot)

    @staticmethod
    def _statistics_snapshot():
        return {
            "session": session_sr(),
            "winrate": current_winrate(),
            "matches": total_matches(),
            "wins": total_wins(),
            "losses": total_losses(),
            "current_streak": current_winstreak(),
            "best_streak": best_winstreak(),
            "current_sr": current_sr(),
        }

    def _refresh_grid(self, snapshot):
        session = self.widgets["session"]
        session_sign = "+" if snapshot["session"] >= 0 else ""
        session["value"].configure(text=f"{session_sign}{snapshot['session']} SR")
        session["trend"].configure(text="Session")
        session["subtitle"].configure(text=f"{snapshot['matches']} parties")

        winrate = self.widgets["winrate"]
        winrate["value"].configure(text=f"{snapshot['winrate']}%")
        winrate["trend"].configure(text=f"{snapshot['wins']}V \u2022 {snapshot['losses']}D")
        winrate["subtitle"].configure(text=f"{snapshot['matches']} parties")

        streak = self.widgets["streak"]
        streak["value"].configure(text=f"x{snapshot['current_streak']}")
        streak["trend"].configure(text=f"Record : x{snapshot['best_streak']}")
        streak["subtitle"].configure(text="S\u00e9rie actuelle")

        current = self.widgets["current"]
        current["value"].configure(text=f"{snapshot['current_sr']} SR")
        current["trend"].configure(text="SR actuel")
        current["subtitle"].configure(text=f"{snapshot['matches']} parties")

    def _refresh_header(self, snapshot):
        if not self.header_widgets:
            return

        session_sign = "+" if snapshot["session"] >= 0 else ""
        self.header_widgets["session"].configure(
            text=f"{session_sign}{snapshot['session']} SR"
        )
        self.header_widgets["wins"].configure(text=str(snapshot["wins"]))
        self.header_widgets["losses"].configure(text=str(snapshot["losses"]))
        self.header_widgets["winrate"].configure(text=f"{snapshot['winrate']}%")
        self.header_widgets["winstreak"].configure(
            text=f"\U0001F525 x{snapshot['current_streak']}"
        )
