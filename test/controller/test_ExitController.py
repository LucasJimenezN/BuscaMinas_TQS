import unittest
from src.controller.ExitController import end_execution


class TestEndExecution(unittest.TestCase):
    def test_end_execution(self):
        with self.assertRaises(SystemExit):
            end_execution()


if __name__ == '__main__':
    unittest.main()
