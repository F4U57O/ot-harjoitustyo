class Workout:
    """
    Luokka edustaa yksittäistä harjoitusta.
    """

    def __init__(self, user_id, date, activity, duration):
        """
        Luo uuden harjoitusinstanssin.

        Args:
            user_id (int): Käyttäjän tunniste
            date (date): Harjoituksen päivämäärä
            activity (str): Harjoituksen tyyppi
            duration (int): Harjoituksen kesto minuutteina.
        """
        self.user_id = user_id
        self.date = date
        self.activity = activity
        self.duration = duration
