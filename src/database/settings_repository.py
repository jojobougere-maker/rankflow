from .database import get_connection


class SettingsRepository:

    def get(self):

        conn = get_connection()

        row = conn.execute(
            "SELECT * FROM settings WHERE id = 1"
        ).fetchone()

        conn.close()

        return row

    def update_sr(self, sr: int):

        conn = get_connection()

        conn.execute(
            """
            UPDATE settings
            SET current_sr = ?,
                updated_at = datetime('now')
            WHERE id = 1
            """,
            (sr,),
        )

        conn.commit()
        conn.close()

    def update_goal(self, goal: int):

        conn = get_connection()

        conn.execute(
            """
            UPDATE settings
            SET goal_sr = ?,
                updated_at = datetime('now')
            WHERE id = 1
            """,
            (goal,),
        )

        conn.commit()
        conn.close()

    def update_name(self, name: str):

        conn = get_connection()

        conn.execute(
            """
            UPDATE settings
            SET activision_name = ?,
                updated_at = datetime('now')
            WHERE id = 1
            """,
            (name,),
        )

        conn.commit()
        conn.close()

    def update_current_rank(self, rank: str):

        conn = get_connection()

        conn.execute(
            """
            UPDATE settings
            SET current_rank = ?,
                updated_at = datetime('now')
            WHERE id = 1
            """,
            (rank,),
        )

        conn.commit()
        conn.close()

    def update_peak_rank(self, rank: str):

        conn = get_connection()

        conn.execute(
            """
            UPDATE settings
            SET peak_rank = ?,
                updated_at = datetime('now')
            WHERE id = 1
            """,
            (rank,),
        )

        conn.commit()
        conn.close()

    def update_peak_sr(self, sr: int):

        conn = get_connection()

        conn.execute(
            """
            UPDATE settings
            SET peak_sr = ?,
                updated_at = datetime('now')
            WHERE id = 1
            """,
            (sr,),
        )

        conn.commit()
        conn.close()

    def update_goal_rank(self, rank: str):

        conn = get_connection()

        conn.execute(
            """
            UPDATE settings
            SET goal_rank = ?,
                updated_at = datetime('now')
            WHERE id = 1
            """,
            (rank,),
        )

        conn.commit()
        conn.close()

