import unittest
from initialize_database import initialize_database
from database_connection import get_database_connection
from services.register_service import RegisterService
from repositories.user_repository import UserRepository


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection(test=True)
        initialize_database(self.connection)
        self.repo = UserRepository(self.connection)
        self.register = RegisterService(self.repo)

    def tearDown(self):
        self.connection.close()

    def test_registering_works_with_right_credentials(self):
        success, message = self.register.register_user("test_user", "password")
        self.assertTrue(success)
        self.assertEqual(message, "Rekisteröinti onnistui!")

    def test_registering_fails_with_too_short_username(self):
        fail, message = self.register.register_user("aa", "password")
        self.assertFalse(fail)
        self.assertEqual(
            message, "Käyttäjätunnuksen tulee olla vähintään 3 merkkiä")

    def test_registering_fails_with_too_short_password(self):
        fail, message = self.register.register_user("test_user", "passwor")
        self.assertFalse(fail)
        self.assertEqual(message, "Salasanan tulee olla vähintään 8 merkkiä")

    def test_registering_fails_if_username_is_not_unique(self):
        self.register.register_user("same_user", "password")
        fail, message = self.register.register_user("same_user", "password")
        self.assertFalse(fail)
        self.assertEqual(message, "Käyttäjätunnus on jo käytössä")
