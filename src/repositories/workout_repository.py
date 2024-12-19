from database_connection import get_database_connection


class WorkoutRepository:
    """
    Luokka harjoituspäiväkirjan hallintaan tietokannassa.
    """
    def __init__(self, connection=None):
        """
        Alustaa WorkoutRepository-instanssin.

        Args:
            connection (sqlite3.Connection, optional): Tietokantayhteys.
        """
        self.connection = connection or get_database_connection()

    def add_workout(self, user_id, date, activity, duration):
        """
        Lisää merkinnän harjoituspäiväkirjaan tietokannassa.

        Args:
            user_id (int): Tunniste käyttäjälle, jolle merkintä tallennetaan.
            date (str): Harjoituksen päivämäärä.
            activity (str): Harjoituksen tyyppi.
            duration (int): Harjoituksen kerto minuutteina.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO workouts (user_id, date, activity, duration) VALUES (?, ?, ?, ?)",
            (user_id, date, activity, duration),
        )
        self.connection.commit()

    def get_workouts(self, user_id):
        """
        Hakee käyttäjän harjoitukset.

        Args:
            user_id (int): Tunniste käyttäjälle, jonka harjoitukset haetaan.

        Returns:
            list[tuple]: Sisältää harjoitusten tiedot.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT date, activity, duration FROM workouts WHERE user_id = ?",
                       (user_id,))
        return cursor.fetchall()
