from .database import get_connection


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            played_at TEXT NOT NULL,

            result TEXT NOT NULL,

            sr_before INTEGER NOT NULL,

            sr_change INTEGER NOT NULL,

            sr_after INTEGER NOT NULL

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (

            id INTEGER PRIMARY KEY CHECK(id = 1),

            activision_name TEXT,

            current_sr INTEGER NOT NULL,

            goal_sr INTEGER NOT NULL,

            created_at TEXT,

            updated_at TEXT

        )
    """)

    # ----------------------------------------
    # Migrations Settings
    # ----------------------------------------

    columns = [
        ("current_rank", "TEXT DEFAULT 'Bronze I'"),
        ("peak_rank", "TEXT DEFAULT 'Bronze I'"),
        ("peak_sr", "INTEGER DEFAULT 0"),
        ("goal_rank", "TEXT DEFAULT 'Top 250'"),
    ]

    cursor.execute("PRAGMA table_info(settings)")
    existing = [row[1] for row in cursor.fetchall()]

    for column, sql_type in columns:
        if column not in existing:
            cursor.execute(
                f"ALTER TABLE settings ADD COLUMN {column} {sql_type}"
            )

    cursor.execute("""
        INSERT OR IGNORE INTO settings (
            id,
            activision_name,
            current_sr,
            goal_sr,
            current_rank,
            peak_rank,
            peak_sr,
            goal_rank,
            created_at,
            updated_at
        )
        VALUES (
            1,
            '',
            0,
            10000,
            'Bronze I',
            'Bronze I',
            0,
            'Top 250',
            datetime('now'),
            datetime('now')
        )
    """)

    conn.commit()

    conn.close()