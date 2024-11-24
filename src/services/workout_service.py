class WorkoutService:
    def __init__(self, workout_repo):
        self.workout_repo = workout_repo

    def add_workout(self, user_id, date, activity, duration):
        if len(activity) < 0:
            return False, "Harjoitus puuttuu"
        self.workout_repo.add_workout(user_id, date, activity, duration)
        return True, "Harjoitus lisätty"

    def get_workouts(self, user_id):
        return self.workout_repo.get_workouts(user_id)
