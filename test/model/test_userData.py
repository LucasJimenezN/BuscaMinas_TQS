import unittest
from src.model.userData import User


class MyTestCase(unittest.TestCase):
    def test_get_set_name(self):
        user = User()
        self.assertEqual(user.get_name(), None, "Return is not the same")
        user.set_name("Lucas")
        self.assertEqual(user.get_name(), "Lucas", "Set name not working")
        user.set_name("Saul")
        self.assertEqual(user.get_name(), "Saul", "Set name not working")

    def test_get_set_score(self):
        pass



if __name__ == '__main__':
    unittest.main()
