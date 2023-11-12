import unittest
from ...src.model.connection import DB


class MyTestCase(unittest.TestCase):

    def test_check_insert_data(self):
        self.assertTrue(DB.check_insert_data(self, "Lucas", 1000))
        self.assertFalse(DB.check_insert_data(self, "Lucas", "Hola"))
        self.assertFalse(DB.check_insert_data(self, 10, 1000))
        self.assertTrue(DB.check_insert_data(self, "",20))

    def test_read_value_from_id(self):
        self.assertFalse(DB.read_value_from_id(self, "string"), "String passed as parameter")
        self.assertFalse(DB.read_value_from_id(self, 10.0), "Float passed as parameter")
        self.assertFalse(DB.read_value_from_id(self, 1000), "Id not found")
        self.assertEqual(DB.read_value_from_id(self, 1), [(1, "Lucas", 1000)], "Data not fetched")


if __name__ == '__main__':
    unittest.main()
