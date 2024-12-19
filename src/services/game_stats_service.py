from entities.game_stats import GameStats


class GameStatsService:
    """
    Luokka pelitilastojen hallintaan.

    Mahdollistaa pelitilastojen lisäämisen, hakemisen ja poistamisen.
    """

    def __init__(self, game_stats_repo):
        """
        Alustaa GameStatsService-luokan.

        Args:
            game_stats_repo (_type_): Hallinnoi pelitilastoihin liittyviä tietokantatoimintoja.
        """
        self.game_stats_repo = game_stats_repo

    def add_game_stats(
            self, game_id, user_id, game_stats):
        """_summary_

        Args:
            game_id (int): Yksilöllinen tunniste tilastolle
            user_id (int): Käyttäjän tunniste
            opponent (str): Vastustajan nimi
            game_stats (dict): Sisältää seuraavat:
                date (date): Pelin päivämäärä
                goals (int): Maalien lukumäärä
                assists (int): Syöttöpisteiden määrä
                play_time (int): Peliaika minuutteina
                rating (int): Pelin arvosana
                feedback (str): Palaute tekstinä

        Returns:
            Tuplen, jossa totuusarvo, sekä viesti merkkijonona.
        """
        game_stat = GameStats(game_id, user_id, game_stats)
        self.game_stats_repo.add_game_stats(game_stat)
        return True, "Pelitilasto lisätty!"

    def get_game_stats(self, user_id):
        """
        Hakee käyttäjän kaikki pelitilastot

        Args:
            user_id (int): Käyttäjän tunniste

        Returns:
            Lista käyttäjän pelitilastoista.
        """
        return self.game_stats_repo.get_game_stats(user_id)

    def delete_game_stat(self, stat_id):
        """
        Poistaa yksittäisen pelitilaston

        Args:
            stat_id (int): Poistettavan pelitilaston tunniste
        """
        self.game_stats_repo.delete_game_stat(stat_id)
