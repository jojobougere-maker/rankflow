import json
import time
from datetime import datetime

from src.analytics.statistics import current_sr
from src.services.rank_service import RankService
from src.database.repository import get_matches

from src.core.paths import overlay_json_path


class OverlayController:

    def __init__(self):

        self.rank_service = RankService()

        self.path = overlay_json_path()

    def refresh(self):

        print(self.path)
        print(self.path.exists())

        sr = current_sr()

        rank = self.rank_service.get_rank(sr)

        matches = get_matches()

        session = sum(
            match["sr_change"]
            for match in matches
        )

        data = {
            "rank": rank.name,
            "rank_icon": rank.icon,
            "sr": sr,
            "session": session,
            "last_result": "Victory" if session >= 0 else "Defeat",
            "event_id": int(time.time()),
            "updated_at": datetime.now().isoformat()
        }

        self.path.parent.mkdir(parents=True, exist_ok=True)

        self.path.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8"
        )

        self.path.write_text(
            json.dumps(data, indent=4),
            encoding="utf-8"
        )