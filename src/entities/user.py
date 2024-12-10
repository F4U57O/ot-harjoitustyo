class User:
    """Luokka edustaa käyttäjää sovelluksessa.
    """

    def __init__(self, username, password):
        """
        Luo uuden User-instanssin.

        Args:
            username (str): Käyttäjän valitsema tunnus
            password (str): Käyttäjän valitsema salasana
        """
        self.username = username
        self.password = password
