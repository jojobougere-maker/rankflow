import os
import subprocess
import tempfile
import threading
import urllib.request
import json
from pathlib import Path
from tkinter import messagebox


API_URL = "https://api.github.com/repos/jojobougere-maker/rankflow/releases/latest"


def _version_tuple(version):
    version = str(version).strip().lstrip("vV")
    parts = []
    for part in version.split("."):
        digits = ""
        for char in part:
            if char.isdigit():
                digits += char
            else:
                break
        parts.append(int(digits or "0"))
    while len(parts) < 3:
        parts.append(0)
    return tuple(parts[:3])


def _get_latest_release():
    request = urllib.request.Request(
        API_URL,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "RankFlow-Updater",
        },
    )

    with urllib.request.urlopen(request, timeout=8) as response:
        return json.loads(response.read().decode("utf-8"))


def _download_installer(asset_url, filename):
    temp_dir = Path(tempfile.gettempdir()) / "RankFlowUpdate"
    temp_dir.mkdir(parents=True, exist_ok=True)

    installer_path = temp_dir / filename

    request = urllib.request.Request(
        asset_url,
        headers={"User-Agent": "RankFlow-Updater"},
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        with installer_path.open("wb") as output:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                output.write(chunk)

    return installer_path


def check_for_update(current_version, on_result):
    """
    Vérifie GitHub en arrière-plan.
    on_result doit être appelé depuis le thread UI via app.after().
    """
    def worker():
        try:
            release = _get_latest_release()

            if release.get("draft") or release.get("prerelease"):
                on_result(None)
                return

            latest_version = str(release.get("tag_name", "")).lstrip("vV")

            if not latest_version:
                on_result(None)
                return

            if _version_tuple(latest_version) <= _version_tuple(current_version):
                on_result(None)
                return

            assets = release.get("assets") or []
            installer = next(
                (
                    asset for asset in assets
                    if str(asset.get("name", "")).lower().endswith(".exe")
                    and "setup" in str(asset.get("name", "")).lower()
                ),
                None,
            )

            if installer is None:
                installer = next(
                    (
                        asset for asset in assets
                        if str(asset.get("name", "")).lower().endswith(".exe")
                    ),
                    None,
                )

            if installer is None:
                on_result(None)
                return

            on_result({
                "version": latest_version,
                "name": release.get("name") or f"RankFlow v{latest_version}",
                "notes": release.get("body") or "",
                "download_url": installer.get("browser_download_url"),
                "filename": installer.get("name") or f"RankFlow_Setup_v{latest_version}.exe",
            })

        except Exception:
            # Une erreur de réseau ne doit jamais empêcher RankFlow de démarrer.
            on_result(None)

    threading.Thread(
        target=worker,
        daemon=True,
        name="RankFlowUpdater",
    ).start()


def install_update(update_info, on_error=None):
    try:
        installer_path = _download_installer(
            update_info["download_url"],
            update_info["filename"],
        )

        subprocess.Popen(
            [str(installer_path)],
            cwd=str(installer_path.parent),
        )

        return True

    except Exception as exc:
        if on_error:
            on_error(str(exc))
        return False
