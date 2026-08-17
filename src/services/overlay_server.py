from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from datetime import datetime
import traceback

from src.core.paths import get_app_root


LOG_FILE = Path.home() / "rankflow.log"


def log(message):
    try:
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(
                f"[{datetime.now().strftime('%H:%M:%S')}] {message}\n"
            )
    except Exception:
        pass


class LoggingHandler(SimpleHTTPRequestHandler):

    def log_message(self, fmt, *args):
        log(fmt % args)

    def log_error(self, fmt, *args):
        log("ERROR: " + (fmt % args))


class OverlayServer:

    def __init__(self, port=4587):
        self.port = port
        self.server = None
        self.thread = None

    def start(self):

        if self.server:
            log("OverlayServer déjà démarré")
            return

        try:

            root = get_app_root()

            log(f"App root : {root}")

            handler = partial(
                LoggingHandler,
                directory=str(root)
            )

            self.server = ThreadingHTTPServer(
                ("127.0.0.1", self.port),
                handler
            )

            log(f"Serveur créé sur le port {self.port}")

            def run():

                try:
                    log("serve_forever() START")

                    self.server.serve_forever()

                    log("serve_forever() STOP")

                except Exception:

                    log("Exception dans serve_forever()")
                    log(traceback.format_exc())

            self.thread = Thread(
                target=run,
                daemon=True,
                name="OverlayServer"
            )

            self.thread.start()

            log("Thread démarré")

        except Exception:

            log("Exception au démarrage")
            log(traceback.format_exc())

    def stop(self):

        if self.server:

            log("Arrêt serveur")

            self.server.shutdown()

            self.server.server_close()

            self.server = None