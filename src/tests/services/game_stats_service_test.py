import unittest
from database_connection import get_database_connection
from initialize_database import initialize_database
from entities.game_stats import GameStats
from services.game_stats_service import GameStatsService
from repositories.game_stats_repository import GameStatsRepository


class TestGameStats(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection(test=True)
        initialize_database(self.connection)
        self.repo = GameStatsRepository(self.connection)
        self.game_stats = GameStatsService(self.repo)

    def tearDown(self):
        self.connection.close()

    def test_add_game_stats(self):
        user_id = 1
        opponent = "Testi joukkue"
        date = "01-12-2024"
        goals = 2
        assists = 1
        play_time = 50
        rating = 9
        feedback = "Hyvä peli!"

        success, message = self.game_stats.add_game_stats(
            id, user_id, opponent, date, goals, assists, play_time, rating, feedback
        )
        self.assertTrue(success)
        self.assertEqual(message, "Pelitilasto lisätty!")

        stats = self.repo.get_game_stats(user_id)
        self.assertEqual(len(stats), 1)
        self.assertEqual(stats[0].opponent, "Testi joukkue")
        self.assertEqual(stats[0].goals, 2)
