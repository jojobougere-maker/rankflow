from pathlib import Path
import sys


def get_app_root() -> Path:
    if getattr(sys, "frozen", False):
        exe_dir = Path(sys.executable).parent

        internal = exe_dir / "_internal"

        if internal.exists():
            return internal

        return exe_dir

    return Path(__file__).resolve().parents[2]


def data_dir() -> Path:
    return get_app_root() / "data"


def assets_dir() -> Path:
    return get_app_root() / "assets"


def overlay_dir() -> Path:
    return get_app_root() / "overlay"


def database_path() -> Path:
    return data_dir() / "rankflow.db"


def overlay_json_path() -> Path:
    return data_dir() / "overlay_data.json"