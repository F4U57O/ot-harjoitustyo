class GoalService:
    def __init__(self, goal_repo):
        """
        Alustaa GoalService-luokan käyttäen annettua GoalRepositorya

        Args:
            goal_repo: Instanssi GoalRepository-luokasta, jota käytetään tietokantatoimintoihin.
        """
        self.goal_repo = goal_repo

    def add_goal(self, user_id, goal):
        """
        Lisää uuden tavoitteen käyttäjälle.

        Args:
            user_id: Käyttäjän id, jolle tavoite lisätään
            goal: Tavoitteen kuvaus.

        Returns:
            Tuplen, joka sisältää:
            Boolean-arvo, joka kertoo tavoitteen luonnin onnistumisesta.
            String, joka kuvaa operaation tuloksen.
        """
        if not goal or len(goal) < 3:
            return False, "Tavoitteen tulee olla vähintään 3 merkkiä."
        self.goal_repo.add_goal(user_id, goal)
        return True, "Tavoite lisätty!"

    def update_goal_status(self, goal_id, status):
        """
        Päivittää olemassa olevan tavoitteen tilan.

        Args:
            goal_id: Tavoitteen id, jonka tila päivitetään.
            status: Päivitetty tila tavoitteelle.

        Returns:
            Tuplen, joka sisältää:
            Boolean-arvo, joka kertoo päivittämisen onnistumisesta.
            String, joka kuvaa operaation tuloksen
        """
        if status not in ["käynnissä", "suoritettu", "ei suoritettu"]:
            return False, "Virheellinen tila!"
        self.goal_repo.update_goal_status(goal_id, status)
        return True, "Tavoitteen tila päivitetty!"

    def get_user_goals(self, user_id):
        """
        Hakee kaikki käyttäjän tavoitteet.

        Args:
            user_id: Käyttäjän id, jonka tavoitteet haetaan.

        Returns:
            Listan käyttäjän tavoitteista.
        """
        return self.goal_repo.get_goals(user_id)
