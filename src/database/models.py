from dataclasses import dataclass


@dataclass
class Match:
    played_at: str
    result: str
    sr_change: int
    sr_after: int