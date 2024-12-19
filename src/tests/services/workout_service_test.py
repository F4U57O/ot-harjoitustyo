import unittest
from database_connection import get_database_connection
from initialize_database import initialize_database
from services.workout_service import WorkoutService
from repositories.workout_repository import WorkoutRepository


class TestWorkout(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection(test=True)
        initialize_database(self.connection)
        self.repo = WorkoutRepository(self.connection)
        self.workout = WorkoutService(self.repo)

    def tearDown(self):
        self.connection.close()

    def test_add_workout(self):
        user_id = 1
        date = "2024-12-13"
        activity = "Juoksu"
        duration = 30

        success, message = self.workout.add_workout(
            user_id, date, activity, duration
        )
        self.assertTrue(success)
        self.assertEqual(message, "Harjoitus lisätty")

        workouts = self.repo.get_workouts(user_id)
        self.assertEqual(len(workouts), 1)

    def test_add_workout_fail(self):
        user_id = 1
        date = "2024-12-13"
        activity = ""
        duration = 30

        fail, message = self.workout.add_workout(
            user_id, date, activity, duration
        )
        self.assertFalse(fail)
        self.assertEqual(message, "Harjoitus puuttuu")
