from src.database.repository import get_matches
from src.database.settings_repository import SettingsRepository


_settings = SettingsRepository()


def total_matches():
    return len(get_matches())


def total_wins():
    matches = get_matches()

    return sum(
        1
        for match in matches
        if match["result"] == "Victory"
    )


def total_losses():
    matches = get_matches()

    return sum(
        1
        for match in matches
        if match["result"] == "Defeat"
    )


def current_sr():

    settings = _settings.get()

    if settings is None:
        return 0

    return int(settings["current_sr"])


def current_winrate():

    games = total_matches()

    if games == 0:
        return 0

    return round((total_wins() / games) * 100, 1)

def current_winstreak():
    """
    Série de victoires actuelle.
    """

    streak = 0

    # The repository returns the newest match first.  Counting from that end
    # yields the streak that is active right now.
    matches = get_matches()

    for match in matches:
        if match["result"] == "Victory":
            streak += 1
        else:
            break

    return streak


def best_winstreak():
    """
    Meilleure série de victoires.
    """

    best = 0
    current = 0

    for match in get_matches():

        if match["result"] == "Victory":
            current += 1
            best = max(best, current)

        else:
            current = 0

    return best


def session_sr():
    """
    Somme des SR gagnés/perdus.
    """

    total = 0

    for match in get_matches():
        total += int(match["sr_change"])

    return total

from datetime import datetime


def sr_history():
    """
    Historique du SR dans l'ordre chronologique.
    """

    matches = list(reversed(get_matches()))

    return [
        {
            "date": match["played_at"],
            "sr": int(match["sr_after"]),
            "result": match["result"],
            "change": int(match["sr_change"]),
        }
        for match in matches
    ]
