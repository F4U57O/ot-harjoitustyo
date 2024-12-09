from datetime import datetime
from database_connection import get_database_connection


class GoalRepository:
    def __init__(self, connection=None):
        self.connection = connection or get_database_connection()

    def add_goal(self, user_id, goal, status="käynnissä"):
        created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        query = """
        INSERT INTO goals (user_id, goal, status, created_at)
        VALUES (?, ?, ?, ?)
        """
        self.connection.execute(query, [user_id, goal, status, created_at])
        self.connection.commit()

    def update_goal_status(self, goal_id, status):
        status_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        query = """
        UPDATE goals SET status = ?, status_updated_at = ? WHERE id = ?
        """
        self.connection.execute(query, [status, status_updated_at, goal_id])
        self.connection.commit()

    def get_goals(self, user_id):
        query = """
        SELECT * FROM goals WHERE user_id = ?
        """
        rows = self.connection.execute(query, [user_id]).fetchall()
        return [
            {"id": row["id"], "goal": row["goal"], "status": row["status"],
                "created_at": row["created_at"], "status_updated_at": row["status_updated_at"]}
            for row in rows
        ]
