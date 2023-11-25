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

    @patch('src.model.data.DB')
    def test_get_data_from_id(self, mock_db):
        mock_db.read_value_from_id.return_value = [(1, "Test", 100)]
        self.assertTrue(self.user.get_data_from_id(1))
        self.assertEqual(self.user.get_id(), 1)
        self.assertEqual(self.user.get_name(), "Test")
        self.assertEqual(self.user.get_score(), 100)

    @patch('src.model.data.DB')  # replace 'your_module' with the actual module name
    @patch('builtins.input', return_value="Test")
    def test_add_user(self, input, mock_db):
        self.user.add_user(100)
        mock_db.create_values.assert_called_with("Test", 100)
if __name__ == '__main__':
    unittest.main()
