
class RegisterService:
    """
    Luokka Käyttäjien rekisteröintiin
    """

    def __init__(self, user_repo):
        """
        Alustaa RegisterService-luokan

        Args:
            user_repo (UserRepository): Hallinnoi käyttäjätunnusten tallentamista ja hakemista.
        """
        self.user_repo = user_repo

    def register_user(self, username, password):
        """
        Alustaa RegisterService-luokan

        Args:
            username (str): Uusi käyttäjätunnus
            password (str): Uusi salasana

        Returns:
            Tuple, jossa totuusarvo ja viesti merkkijonona.
        """
        if len(username) < 3:
            return False, "Käyttäjätunnuksen tulee olla vähintään 3 merkkiä"
        if len(password) < 8:
            return False, "Salasanan tulee olla vähintään 8 merkkiä"
        if self.user_repo.find_user_by_username(username):
            return False, "Käyttäjätunnus on jo käytössä"
        if self.user_repo.create_user(username, password):
            return True, "Rekisteröinti onnistui!"
        return False, "Käyttäjän rekisteröinti epäonnistui"
