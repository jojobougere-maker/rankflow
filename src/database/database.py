import sqlite3

from src.core.paths import database_path, data_dir


DB_PATH = database_path()


def get_connection():

    data_dir().mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn