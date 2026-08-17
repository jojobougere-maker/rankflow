from dataclasses import dataclass, field


@dataclass
class ApplicationState:
    # Profil
    activision_name: str = ""

    # Rang
    current_sr: int = 0
    current_rank: str = "Bronze I"
    goal_sr: int = 10000

    # Session
    session_sr: int = 0
    wins: int = 0
    losses: int = 0
    total_games: int = 0
    winrate: float = 0.0

    # Statistiques
    average_win: float = 0.0
    average_loss: float = 0.0
    current_streak: int = 0
    best_streak: int = 0

    # Historique
    history: list = field(default_factory=list)