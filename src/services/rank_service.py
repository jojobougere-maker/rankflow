from dataclasses import dataclass


@dataclass(frozen=True)
class Rank:

    name: str
    min_sr: int
    max_sr: int
    icon: str


RANKS = [

    Rank("Bronze I", 0, 300, "assets/ranks/bronze1.png"),
    Rank("Bronze II", 300, 600, "assets/ranks/bronze2.png"),
    Rank("Bronze III", 600, 900, "assets/ranks/bronze3.png"),

    Rank("Silver I", 900, 1300, "assets/ranks/silver1.png"),
    Rank("Silver II", 1300, 1700, "assets/ranks/silver2.png"),
    Rank("Silver III", 1700, 2100, "assets/ranks/silver3.png"),

    Rank("Gold I", 2100, 2600, "assets/ranks/gold1.png"),
    Rank("Gold II", 2600, 3100, "assets/ranks/gold2.png"),
    Rank("Gold III", 3100, 3600, "assets/ranks/gold3.png"),

    Rank("Platinum I", 3600, 4200, "assets/ranks/platinum1.png"),
    Rank("Platinum II", 4200, 4800, "assets/ranks/platinum2.png"),
    Rank("Platinum III", 4800, 5400, "assets/ranks/platinum3.png"),

    Rank("Diamond I", 5400, 6100, "assets/ranks/diamond1.png"),
    Rank("Diamond II", 6100, 6800, "assets/ranks/diamond2.png"),
    Rank("Diamond III", 6800, 7500, "assets/ranks/diamond3.png"),

    Rank("Crimson I", 7500, 8300, "assets/ranks/crimson1.png"),
    Rank("Crimson II", 8300, 9100, "assets/ranks/crimson2.png"),
    Rank("Crimson III", 9100, 10000, "assets/ranks/crimson3.png"),

    Rank("Iridescent", 10000, 15000, "assets/ranks/iridescent.png"),
]


class RankService:

    def get_rank(self, sr: int) -> Rank:

        for rank in RANKS:

            if rank.min_sr <= sr <= rank.max_sr:
                return rank

        return RANKS[0]

    def progress(self, sr: int) -> float:

        rank = self.get_rank(sr)

        if rank.name == "Iridescent":
            return 1.0

        total = rank.max_sr - rank.min_sr

        current = sr - rank.min_sr

        return current / total

    def remaining(self, sr: int) -> int:

        rank = self.get_rank(sr)

        if rank.name == "Iridescent":
            return 0

        return rank.max_sr - sr

    def next_rank(self, sr: int):

        for index, rank in enumerate(RANKS):

            if rank.min_sr <= sr <= rank.max_sr:

                if index == len(RANKS) - 1:
                    return None

                return RANKS[index + 1]

        return None