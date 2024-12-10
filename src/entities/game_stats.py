class GameStats:
    """Luokka edustaa pelitilastoja
    """

    def __init__(self, id, user_id, opponent, date, goals, assists, play_time, rating, feedback):
        """
        Pelitilasto instanssi.

        Args:
            id (int): id tunniste
            user_id (int): Käyttäjän id
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
        self.opponent = opponent
        self.date = date
        self.goals = goals
        self.assists = assists
        self.play_time = play_time
        self.rating = rating
        self.feedback = feedback
