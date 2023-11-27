import unittest
from src.model.boardData import Board
from src.model.boardData import Tile


class TestBoard(unittest.TestCase):
    def test_tile(self):
        tile = Tile()
        self.assertEqual(tile.is_bomb, False)
        self.assertEqual(tile.is_revealed, False)

    def test_board(self):
        board1 = Board(1)
        self.assertEqual(len(board1.tiles), 6)
        self.assertEqual(sum(tile.is_bomb for row in board1.tiles for tile in row), 8)

        board2 = Board(2)
        self.assertEqual(len(board2.tiles), 8)
        self.assertEqual(sum(tile.is_bomb for row in board2.tiles for tile in row), 16)

        board3 = Board(3)
        self.assertEqual(len(board3.tiles), 10)
        self.assertEqual(sum(tile.is_bomb for row in board3.tiles for tile in row), 32)

        with self.assertRaises(ValueError):
            Board(4)

    def test_checkTile(self):
        board = Board(1)
        for i in range(6):
            for j in range(6):
                if board.tiles[i][j].is_bomb:
                    self.assertEqual(board.checkTile(i, j), False)
                else:
                    num_bombs = board.checkTile(i, j)
                    self.assertTrue(0 <= num_bombs <= 8)

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
