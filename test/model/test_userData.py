import unittest
from ...src.model.userData import User


class MyTestCase(unittest.TestCase):
    def test_get_set_name(self):
        user = User()
        self.assertEqual(user.get_name(), None, "Return is not the same")
        user.set_name("Lucas")
        self.assertEqual(user.get_name(), "Lucas", "Set name not working")
        user.set_name("Saul")
        self.assertEqual(user.get_name(), "Saul", "Set name not working")
        user.set_name(10)
        self.assertEqual(user.get_name(), "Saul", "Set name changed name for an integer")

    def test_get_set_score(self):
        user = User()
        self.assertEqual(user.get_score(), None, "Return is not the same")
        user.set_score(100)
        self.assertEqual(user.get_score(), 100, "Set score not working")
        user.set_score(1000)
        self.assertEqual(user.get_score(), 1000, "Set score not working")
        user.set_score("Name")
        self.assertEqual(user.get_score(), 1000, "Set score modified score for a string")

    def test_init(self):
        user = User()
        self.assertFalse(user.get_data_from_id(""), "Wrong parameter, str.")
        self.assertFalse(user.get_data_from_id(10000), "Id not found.")
        self.assertEqual(user.get_data_from_id(1), [(1, "Lucas", 1000)])
        self.assertEqual(user.get_data_from_id(2), [(2, "Saul", 100)])


if __name__ == '__main__':
    unittest.main()
