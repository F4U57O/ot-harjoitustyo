import unittest
from register import Register
from repositories.user_repository import UserRepository


class TestRegister(unittest.TestCase):
    def setUp(self):
      self.repo = UserRepository()
      self.repo.delete_all()
      self.register = Register(self.repo)
      self.repo.create_user("same_user", "password")

    def test_registering_works_with_right_credentials(self):
      success, message = self.register.register_user("test_user", "password")
      self.assertTrue(success)
      self.assertEqual(message, "Rekisteröinti onnistui!")

    def test_registering_fails_with_too_short_username(self):
      fail, message = self.register.register_user("aa", "password")
      self.assertFalse(fail)
      self.assertEqual(message, "Käyttäjätunnuksen tulee olla vähintään 3 merkkiä")

    def test_registering_fails_with_too_short_password(self):
      fail, message = self.register.register_user("test_user", "passwor")
      self.assertFalse(fail)
      self.assertEqual(message, "Salasanan tulee olla vähintään 8 merkkiä") 

    def test_registering_fails_if_username_is_not_unique(self):
      fail, message = self.register.register_user("same_user", "password")
      self.assertFalse(fail)
      self.assertEqual(message, "Käyttäjätunnus on jo käytössä")
       

