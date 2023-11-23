import unittest
import os
from src.model.connection import DB


class TestDB(unittest.TestCase):
    TEST_DB_NAME = "test_data.db"

    def setUp(self):
        self.db = DB()
        self.db.CONST_DATABASE_NAME = self.TEST_DB_NAME

    def tearDown(self):
        if os.path.exists(self.TEST_DB_NAME):
            os.remove(self.TEST_DB_NAME)

    def test_create_table(self):
        self.db.create_table()
        self.assertTrue(os.path.exists(self.TEST_DB_NAME))

    def test_create_values(self):
        self.db.create_table()
        self.assertTrue(self.db.create_values("Alice", 90))
        self.assertFalse(self.db.create_values(10,""))

    def test_read_all_values(self):
        self.db.create_table()
        self.db.create_values("Alice", 90)
        self.db.create_values("Bob", 80)
        result = self.db.read_all_values()
        self.assertTrue(result)

    def test_get_all_values(self):
        self.db.create_table()
        self.db.create_values("Alice", 90)
        self.db.create_values("Bob", 80)
        result = self.db.get_all_values()
        self.assertEqual(len(result), 2)

    def test_read_value_from_id(self):
        self.db.create_table()
        self.db.create_values("Alice", 90)
        result = self.db.read_value_from_id(1)
        self.assertTrue(result)

    def test_delete_value_from_id(self):
        self.db.create_table()
        self.db.create_values("Alice", 90)
        self.assertTrue(self.db.delete_value_from_id(1))
        self.assertTrue(self.db.delete_value_from_id(99999))

    def test_check_insert_data(self):
        self.assertTrue(self.db.check_insert_data("Alice", 90))

        self.assertFalse(self.db.check_insert_data(None, 90))
        self.assertFalse(self.db.check_insert_data("Alice", None))
        self.assertFalse(self.db.check_insert_data(None, None))
        self.assertFalse(self.db.check_insert_data(123, 90))
        self.assertFalse(self.db.check_insert_data("Alice", "90"))


if __name__ == '__main__':
    unittest.main()
