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

    def test_get_data_from_id_invalid_id(self):
        user = User()
        result = user.get_data_from_id("invalid_id")
        self.assertFalse(result)
        self.assertIsNone(user.get_name())
        self.assertIsNone(user.get_score())

if __name__ == '__main__':
    unittest.main()
