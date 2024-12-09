import unittest
from database_connection import get_database_connection
from initialize_database import initialize_database
from services.goal_service import GoalService
from repositories.goal_repository import GoalRepository


class TestGoal(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection(test=True)
        initialize_database(self.connection)
        self.repo = GoalRepository(self.connection)
        self.goal = GoalService(self.repo)

    def tearDown(self):
        self.connection.close()

    def test_add_goal(self):
        user_id = 1
        goal = "Tavoite"

        success, message = self.goal.add_goal(
            user_id, goal
        )
        self.assertTrue(success)
        self.assertEqual(message, "Tavoite lisätty!")

        goals = self.repo.get_goals(user_id)
        self.assertEqual(len(goals), 1)

    def test_add_goal_fail(self):
        user_id = 1
        goal = "aa"

        fail, message = self.goal.add_goal(
            user_id, goal 
        )
        self.assertFalse(fail)
        self.assertEqual(message, "Tavoitteen tulee olla vähintään 3 merkkiä.")

    