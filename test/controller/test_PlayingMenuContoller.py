import unittest
from src.controller.PlayingMenuController import PlayingMenuController as PMC


class MyTestCase(unittest.TestCase):
    def test_handle_difficulty(self):
        self.assertFalse(PMC.handle_difficulty(self, "string"), "Invalid parameter type")
        self.assertFalse(PMC.handle_difficulty(self, 10.0), "Invalid parameter type")
        self.assertFalse(PMC.handle_difficulty(self, 2.0), "Invalid parameter type")
        self.assertFalse(PMC.handle_difficulty(self, 0), "Invalid parameter value, less than 1")
        self.assertFalse(PMC.handle_difficulty(self, 4), "Invalid parameter value, bigger than 3")
        self.assertTrue(PMC.handle_difficulty(self, 1), "Valid parameter")
        self.assertTrue(PMC.handle_difficulty(self, 2), "Valid parameter")
        self.assertTrue(PMC.handle_difficulty(self, 3), "Valid parameter")


if __name__ == '__main__':
    unittest.main()
