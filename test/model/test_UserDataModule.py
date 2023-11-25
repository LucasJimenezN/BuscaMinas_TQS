import unittest
from src.model.connection import DB
from src.model.userData import User
from mock import patch


class TestUser(unittest.TestCase):
    def setUp(self):
        self.db = DB()
        # Set up your test database or configure the connection as needed

    def tearDown(self):
        # Clean up or close any resources after each test if necessary
        pass

    def test_set_name(self):
        user = User()
        user.set_name("Alice")
        self.assertEqual(user.get_name(), "Alice")

    def test_set_score(self):
        user = User()
        user.set_score(90)
        self.assertEqual(user.get_score(), 90)

    def setUp(self):
        self.user = User()

        # Testing getters and setters
    def test_id(self):
        self.user.set_id(1)
        self.assertEqual(self.user.get_id(), 1)

    def test_name(self):
        self.user.set_name("Test")
        self.assertEqual(self.user.get_name(), "Test")

    def test_score(self):
        self.user.set_score(100)
        self.assertEqual(self.user.get_score(), 100)

        # Mocking the DB class


if __name__ == '__main__':
    unittest.main()
