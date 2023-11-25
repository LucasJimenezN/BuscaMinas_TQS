import unittest
from unittest.mock import patch
from src.controller.MenuController import MenuController  # replace 'your_module' with the actual module name


class TestMenuController(unittest.TestCase):
    def setUp(self):
        self.menu_controller = MenuController()

    # Testing handle_principal_input method
    def test_handle_principal_input(self):
        self.assertFalse(self.menu_controller.handle_principal_input("not an int"))
        self.assertFalse(self.menu_controller.handle_principal_input(0))
        self.assertFalse(self.menu_controller.handle_principal_input(4))

    # Mocking the PM.show_playing_menu method
    @patch('src.view.PlayingMenuView.PlayingMenu.show_playing_menu')
    def test_handle_principal_input_option_1(self, mock_show_playing_menu):
        self.assertTrue(self.menu_controller.handle_principal_input(1))
        mock_show_playing_menu.assert_called()

    # Mocking the RankingController.get_ranking method
    @patch('src.controller.RankingController.RankingController.get_ranking')
    def test_handle_principal_input_option_2(self, mock_get_ranking):
        self.assertTrue(self.menu_controller.handle_principal_input(2))
        mock_get_ranking.assert_called()


if __name__ == '__main__':
    unittest.main()
