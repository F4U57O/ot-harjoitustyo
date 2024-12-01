import sqlite3
from database_connection import get_database_connection
from entities.game_stats import GameStats



class GameStatsRepository:
    def __init__(self, connection=None):
        self.connection = connection or get_database_connection()

    def add_game_stats(self, game_stats):
        query = """
        INSERT INTO game_stats (user_id, opponent, date, goals, assists, play_time, rating, feedback)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
      """
        self.connection.execute(
            query,
            [
                game_stats.user_id, game_stats.opponent, game_stats.date,
                game_stats.goals, game_stats.assists, game_stats.play_time,
                game_stats.rating, game_stats.feedback
            ]
        )
        game_stats.id = self.connection.cursor().lastrowid
        self.connection.commit()

    def get_game_stats(self, user_id):
        query = "SELECT * FROM game_stats WHERE user_id=?"
        rows = self.connection.execute(query, [user_id]).fetchall()
        return [
            GameStats(row["id"], row["user_id"], row["opponent"], row["date"],
                      row["goals"], row["assists"], row["play_time"],
                      row["rating"], row["feedback"]) for row in rows
        ]

    def delete_game_stat(self, stat_id):
        try:
            query = "DELETE FROM game_stats WHERE id = ?"
            self.connection.execute(query, [stat_id])
            self.connection.commit()
        except sqlite3.Error as error:
            print(f"Database error: {error}")
