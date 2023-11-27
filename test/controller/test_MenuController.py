import unittest
from unittest.mock import patch
from src.controller.MenuController import MenuController


class TestMenuController(unittest.TestCase):
    def setUp(self):
        self.menu_controller = MenuController()

    # In this test we just need to know if the input is alright
    def test_handle_principal_input(self):
        self.assertFalse(self.menu_controller.handle_principal_input("not an int"))
        self.assertFalse(self.menu_controller.handle_principal_input(0))
        self.assertFalse(self.menu_controller.handle_principal_input(-1))
        self.assertFalse(self.menu_controller.handle_principal_input(4))


if __name__ == '__main__':
    unittest.main()
