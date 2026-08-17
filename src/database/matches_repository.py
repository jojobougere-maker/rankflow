from src.database.database import get_connection


class MatchesRepository:

    def add_match(
        self,
        result: str,
        sr_before: int,
        sr_after: int,
    ):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO matches(
                result,
                sr_before,
                sr_after,
                sr_change
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                result,
                sr_before,
                sr_after,
                sr_after - sr_before,
            ),
        )

        conn.commit()
        conn.close()

    def get_all_matches(self):

        conn = get_connection()

        rows = conn.execute(
            """
            SELECT *
            FROM matches
            ORDER BY id ASC
            """
        ).fetchall()

        conn.close()

        return rows

    def get_last_match(self):

        conn = get_connection()

        row = conn.execute(
            """
            SELECT *
            FROM matches
            ORDER BY id DESC
            LIMIT 1
            """
        ).fetchone()

        conn.close()

        return row

    def clear_matches(self):

        conn = get_connection()

        conn.execute(
            """
            DELETE FROM matches
            """
        )

        conn.commit()
        conn.close()