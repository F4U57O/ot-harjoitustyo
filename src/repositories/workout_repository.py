from database_connection import get_database_connection


class WorkoutRepository:
    def __init__(self):
        self.connection = get_database_connection()

    def add_workout(self, user_id, date, activity, duration):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO workouts (user_id, date, activity, duration) VALUES (?, ?, ?, ?)",
            (user_id, date, activity, duration),
        )
        self.connection.commit()

    def get_workouts(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT date, activity, duration FROM workouts WHERE user_id = ?",
                       (user_id,))
        return cursor.fetchall()
