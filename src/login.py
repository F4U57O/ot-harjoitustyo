from repositories.user_repository import UserRepository

class Login:
  def __init__(self, user_repo):
      self.user_repo = user_repo

  def login_user(self, username, password):
    user = self.user_repo.find_user_by_username(username)
    if user and user["password"] == password:
      return True, "Kirjautuminen onnistui!"
    
    else:
      return False, "Väärä käyttäjätunnus tai salasana!"



  