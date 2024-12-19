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
        game_id = 1
        user_id = 1
        stats = {
            "opponent": "Testi joukkue",
            "date": "01-12-2024",
            "goals": 2,
            "assists": 1,
            "play_time": 50,
            "rating": 9,
            "feedback": "Hyvä peli!"
        }

        success, message = self.game_stats.add_game_stats( 
            game_id=game_id,
            user_id=user_id, 
            game_stats=stats
        )
        self.assertTrue(success)
        self.assertEqual(message, "Pelitilasto lisätty!")

        game_stat = self.repo.get_game_stats(user_id)
        self.assertEqual(len(game_stat), 1)
        self.assertEqual(game_stat[0].opponent, "Testi joukkue")
        self.assertEqual(game_stat[0].goals, 2)
        self.assertEqual(game_stat[0].assists, 1)
        self.assertEqual(game_stat[0].play_time, 50)
        self.assertEqual(game_stat[0].rating, 9)
        self.assertEqual(game_stat[0].feedback, "Hyvä peli!")
        self.assertEqual(game_stat[0].date, "01-12-2024")
