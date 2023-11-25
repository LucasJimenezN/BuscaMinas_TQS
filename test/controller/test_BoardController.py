import unittest
from unittest.mock import Mock, patch, MagicMock, call
from src.controller.BoardController import BoardController
from src.model.boardData import Board


class TestBoardController(unittest.TestCase):
    def setUp(self):
        self.board = Board(1)

    # Pairwise testing
    def test_pairwise(self):
        self.board = Board(2)
        self.assertEqual(len(self.board.tiles), 8)
        self.assertEqual(len(self.board.tiles[0]), 8)

    # Statement coverage
    def test_statement_coverage(self):
        self.board = Board(3)
        self.assertEqual(len(self.board.tiles), 10)
        self.assertEqual(len(self.board.tiles[0]), 10)

    # Decision coverage
    def test_decision_coverage(self):
        with self.assertRaises(ValueError):
            self.board = Board(4)

    # Condition coverage
    def test_condition_coverage(self):
        self.board = Board(1)
        self.board.tiles[0][0].is_bomb = True
        self.assertFalse(self.board.checkTile(0, 0))

    # Path coverage
    def test_path_coverage(self):
        self.board = Board(1)
        self.board.tiles[0][0].is_bomb = True
        self.board.tiles[0][0].is_revealed = True
        self.assertFalse(self.board.checkHidden(0, 0))

    # Loop testing
    def test_loop_testing(self):
        self.board = Board(1)
        for i in range(self.board.size):
            for j in range(self.board.size):
                self.board.tiles[i][j].is_bomb = True
        self.assertTrue(self.board.is_game_won())

if __name__ == '__main__':
    unittest.main()
