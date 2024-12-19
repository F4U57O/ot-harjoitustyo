class GameStats:
    """Luokka edustaa pelitilastoja
    """

    def __init__(self, id, user_id, stats):
        """
        Pelitilasto instanssi.

        Args:
            id (int): id tunniste
            user_id (int): Käyttäjän id
            stats (dict): Sisältää seuraavat:
                opponent (str): Vastustaja joukkueen nimi
                date (date): Päivämäärä
                goals (int): Maalien määrä
                assists (int): Syöttöjen määrä
                play_time (int): Peliaika
                rating (int): Arvosana
                feedback (str): Palaute tekstinä
        """
        self.id = id
        self.user_id = user_id
        self.stats = stats

    @property
    def opponent(self):
        return self.stats.get("opponent")

    @property
    def date(self):
        return self.stats.get("date")

    @property
    def goals(self):
        return self.stats.get("goals")

    @property
    def assists(self):
        return self.stats.get("assists")

    @property
    def play_time(self):
        return self.stats.get("play_time")

    @property
    def rating(self):
        return self.stats.get("rating")

    @property
    def feedback(self):
        return self.stats.get("feedback")
