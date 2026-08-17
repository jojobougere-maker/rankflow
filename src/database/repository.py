from .database import get_connection
from .models import Match


def add_match(match: Match):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO matches (
            played_at,
            result,
            sr_change,
            sr_after
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            match.played_at,
            match.result,
            match.sr_change,
            match.sr_after,
        ),
    )

    conn.commit()
    conn.close()


def get_matches():

    conn = get_connection()
    conn.row_factory = lambda cursor, row: {
        cursor.description[i][0]: row[i]
        for i in range(len(cursor.description))
    }

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM matches
        ORDER BY played_at DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def clear_matches():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("DELETE FROM matches")

    connection.commit()

    connection.close()