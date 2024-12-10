class WorkoutService:
    """
    Luokka harjoituspäiväkirjan tietojen käsittelyyn
    """

    def __init__(self, workout_repo):
        """
        Alustaa WorkoutService-luokan

        Args:
            workout_repo (WorkoutRepository): Hallinnoi tietojen tallentamista ja hakemista.
        """
        self.workout_repo = workout_repo

    def add_workout(self, user_id, date, activity, duration):
        """
        Lisää uuden harjoituksen tietokantaan.

        Args:
            user_id (int): Käyttäjän tunniste
            date (str): Harjoituksen ajankohta
            activity (str): Harjoituksen tyyppi
            duration (int): Harjoituksen kesto

        Returns:
            Tuplen, jossa totuusarvo ja viesti merkkijonona.
        """
        if len(activity) < 0:
            return False, "Harjoitus puuttuu"
        self.workout_repo.add_workout(user_id, date, activity, duration)
        return True, "Harjoitus lisätty"

    def get_workouts(self, user_id):
        """
        Hakee käyttäjän kaikki harjoitukset

        Args:
            user_id (int): Käyttäjän tunniste

        Returns:
            Listan harjoitusten tiedoista.
        """
        return self.workout_repo.get_workouts(user_id)
