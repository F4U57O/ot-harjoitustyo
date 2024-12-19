from database_connection import get_database_connection


class UserRepository:
    """
    Luokka käyttäjien hallintaan tietokannassa.
    """
    def __init__(self, connection=None):
        """
        Alustaa UserRepository-instanssin.

        Args:
            connection (sqlite3.Connection, optional): Tietokantayhteys.
        """
        self.connection = connection or get_database_connection()

    def create_user(self, username, password):
        """
        Luo uuden käyttäjän tietokantaan.

        Args:
            username (str): Uusi käyttäjänimi.
            password (str): Uusi salasana.

        Returns:
            bool: Totuusarvo käyttäjän luomisen onnistumisesta.
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
            )
            self.connection.commit()
        except Exception as exception:
            print(f"Virhe käyttäjän luomisessa: {exception}")
            return False
        return True

    def find_user_by_username(self, username):
        """
        Hakee käyttäjän tietokannasta.

        Args:
            username (str): Etsitty käyttäjänimi.

        Returns:
            dict: Sisältää käyttäjän tiedot.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()

    def get_all_users(self):
        """
        Hakee käyttäjät tietokannasta.

        Returns:
            list[dict]: Sisältää käyttäjien tiedot.
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")

    def remove_user(self, username):
        """
        Poistaa käyttäjän tietokannasta.

        Args:
            username (str): Käyttäjänimi, jonka käyttäjätunnukset poistetaan.

        Returns:
            bool: Totuusarvo käyttäjän poistamisen onnistumisesta.
        """
        cursor = self.connection.cursor()
        user = self.find_user_by_username(username)
        if user:
            cursor.execute("DELETE FROM users WHERE username = ?", (username,))
            self.connection.commit()
            return True
        return False

    def delete_all(self):
        """
        Poistaa kaikki käyttäjät tietokannasta.

        Returns:
            None
        """
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users")
        self.connection.commit()
