from dataclasses import dataclass


@dataclass
class DashboardStats:

    current_sr: int

    winrate: float

    total_matches: int

    wins: int

    losses: int

    current_streak: int

    best_streak: int