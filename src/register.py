from repositories.user_repository import UserRepository

class Register:
  def __init__(self, user_repo):
    self.user_repo = user_repo


  def register_user(self, username, password):
    if len(username) < 3:
      return False, "Käyttäjätunnuksen tulee olla vähintään 3 merkkiä"
    if len(password) < 8:
      return False, "Salasanan tulee olla vähintään 8 merkkiä"
    if self.user_repo.find_user_by_username(username):
      return False,"Käyttäjätunnus on jo käytössä"
    if self.user_repo.create_user(username, password):
      return True, "Rekisteröinti onnistui!"
    else: 
      return False, "Käyttäjän rekisteröinti epäonnistui"



