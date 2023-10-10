import unittest
from src.model.connection import DB


class MyTestCase(unittest.TestCase):

    def test_check_insert_data(self):
        self.assertTrue(DB.check_insert_data(self, "Lucas", 1000))
        self.assertFalse(DB.check_insert_data(self, "Lucas", "Hola"))
        self.assertFalse(DB.check_insert_data(self, 10, 1000))
        self.assertTrue(DB.check_insert_data(self, "",20))




if __name__ == '__main__':
    unittest.main()
