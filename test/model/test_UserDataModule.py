import unittest
from unittest.mock import patch
from src.model.userData import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_initialization(self):
        self.assertIsNone(self.user.get_id())
        self.assertIsNone(self.user.get_name())
        self.assertIsNone(self.user.get_score())

    def test_set_id(self):
        self.user.set_id(1)
        self.assertEqual(self.user.get_id(), 1)

    def test_set_invalid_id(self):
        self.user.set_id("string")
        self.assertIsNone(self.user.get_id())

    def test_set_name(self):
        self.user.set_name("John")
        self.assertEqual(self.user.get_name(), "John")

    def test_set_invalid_name(self):
        self.user.set_name(123)
        self.assertIsNone(self.user.get_name())

    def test_set_score(self):
        self.user.set_score(100)
        self.assertEqual(self.user.get_score(), 100)

    def test_set_invalid_score(self):
        self.user.set_score("string")
        self.assertIsNone(self.user.get_score())

    @patch('builtins.input', return_value='John')
    def test_add_user(self, mock_input):
        self.user.add_user(100)
        self.assertEqual(self.user.get_name(), 'John')


if __name__ == '__main__':
    unittest.main()
