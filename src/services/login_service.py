
class LoginService:
    def __init__(self, user_repo):
        """
        Alustaa LoginService-luokan käyttäen annettua UserRepositorya

        Args:
            user_repo: Instanssi UserRepository-luokasta, jota käytetään tietokantatoimintoihin.
        """
        self.user_repo = user_repo

    def login_user(self, username, password):
        """
        Kirjaa käyttäjän sisään tarkistamalla käyttäjätunnuksen ja salasanan.

        Args:
            username: Käyttäjän nimimerkki, jolla kirjaudutaan sisään.
            password: Käyttäjän salasana, joka vaaditaan kirjautumiseen.

        Returns:
            Tuplen, joka sisältää:
            Boolean-arvo, kirjautumisen onnistumisesta.
            String, joka kuvaa operaation tuloksen.
        """
        user = self.user_repo.find_user_by_username(username)
        if user and user["password"] == password:
            return True, "Kirjautuminen onnistui!"

        return False, "Väärä käyttäjätunnus tai salasana!"

    def log_out(self):
        """
        Kirjaa käyttäjän ulos.
        """
        self.user = None
