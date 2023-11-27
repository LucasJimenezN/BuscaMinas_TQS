import unittest
from src.controller.PlayingMenuController import PlayingMenuController

class TestPlayingMenuController(unittest.TestCase):

    def test_handle_difficulty_valid(self):
        playing_menu_controller = PlayingMenuController()

        # Valid inputs
        valid_inputs = [1, 2, 3]
        for option in valid_inputs:
            with self.subTest(option=option):
                result = playing_menu_controller.handle_difficulty(option)
                self.assertTrue(result)
                self.assertEqual(playing_menu_controller.difficulty, option)

    def test_handle_difficulty_invalid(self):
        playing_menu_controller = PlayingMenuController()

        # Invalid inputs excluding None
        invalid_inputs = [0, 4, 5, "a", 1.5, True, False]
        for option in invalid_inputs:
            with self.subTest(option=option):
                result = playing_menu_controller.handle_difficulty(option)
                self.assertFalse(result)
                self.assertIsNone(playing_menu_controller.difficulty)

if __name__ == '__main__':
    unittest.main()
