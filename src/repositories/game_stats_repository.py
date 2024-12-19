import sqlite3
from database_connection import get_database_connection
from entities.game_stats import GameStats


class GameStatsRepository:
    """
    Luokka vastaa pelitilastojen hallinnasta tietokannassa.

    Metodit pelitilastojen lisäämiseen, hakemiseen ja poistamiseen.
    """
    def __init__(self, connection=None):
        """
        Alustaa GameStatRepository-instanssin.

        Args:
            connection (sqlite3.Connection, optional): Tietokantayhteys.
        """
        self.connection = connection or get_database_connection()

    def add_game_stats(self, game_stats):
        """
        Lisää pelitilastomerkinnän tietokantaan.

        Args:
            game_stats (GameStats): Sisältää lisättävät pelitilastot.

        Returns:
            None
        """
        query = """
        INSERT INTO game_stats (user_id, opponent, date, goals, assists, play_time, rating, feedback)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
      """
        self.connection.execute(
            query,
            [
                game_stats.user_id, game_stats.stats["opponent"], game_stats.stats["date"],
                game_stats.stats["goals"], game_stats.stats["assists"],
                game_stats.stats["play_time"], game_stats.stats["rating"],
                game_stats.stats["feedback"]
            ]
        )
        game_stats.id = self.connection.cursor().lastrowid
        self.connection.commit()

    def get_game_stats(self, user_id):
        """
        Hakee käyttäjän pelitilastot.

        Args:
            user_id (int): Tunniste käyttäjälle, jonka pelitilastot haetaan.

        Returns:
            list[GameStats]: Käyttäjän pelitilastot
        """
        query = "SELECT * FROM game_stats WHERE user_id=?"
        rows = self.connection.execute(query, [user_id]).fetchall()
        return [
            GameStats(row["id"], row["user_id"],
                      {
                      "opponent": row["opponent"],
                      "date": row["date"],
                      "goals": row["goals"],
                      "assists": row["assists"],
                      "play_time": row["play_time"],
                      "rating": row["rating"],
                      "feedback": row["feedback"]
                      }
                      )
            for row in rows
        ]

    def delete_game_stat(self, stat_id):
        """
        Poistaa pelitilaston tietokannasta.

        Args:
            stat_id (int): Pelitilaston tunniste, joka poistetaan.
        """
        try:
            query = "DELETE FROM game_stats WHERE id = ?"
            self.connection.execute(query, [stat_id])
            self.connection.commit()
        except sqlite3.Error as error:
            print(f"Database error: {error}")
