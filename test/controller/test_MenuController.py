import unittest
from ...src.controller.MenuController import MenuController as MC


class MyTestCase(unittest.TestCase):
    # Not necessari
    def test_handlePrincipalInput(self):
        self.assertFalse(MC.handle_principal_input(self, "string"))
        self.assertFalse(MC.handle_principal_input(self, 10.0))
        self.assertFalse(MC.handle_principal_input(self, 0))
        self.assertFalse(MC.handle_principal_input(self, 4))
        self.assertFalse(MC.handle_principal_input(self, 10))
        self.assertTrue(MC.handle_principal_input(self, 1))
        self.assertTrue(MC.handle_principal_input(self, 2))
        self.assertTrue(MC.handle_principal_input(self, 3))


if __name__ == '__main__':
    unittest.main()
