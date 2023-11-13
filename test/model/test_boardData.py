import unittest
from ...src.model.boardData import Board
from ...src.model.boardData import Tile


class TestMinesweeper(unittest.TestCase):
    def test_tile(self):
        tile = Tile()
        self.assertEqual(tile.is_bomb, False)

    def test_board(self):
        board1 = Board(1)
        self.assertEqual(len(board1.board), 6)
        self.assertEqual(sum(tile.is_bomb for row in board1.board for tile in row), 8)

        board2 = Board(2)
        self.assertEqual(len(board2.board), 8)
        self.assertEqual(sum(tile.is_bomb for row in board2.board for tile in row), 16)

        board3 = Board(3)
        self.assertEqual(len(board3.board), 10)
        self.assertEqual(sum(tile.is_bomb for row in board3.board for tile in row), 32)

        with self.assertRaises(ValueError):
            Board(4)

    def test_checkTile(self):
        board = Board(1)
        for i in range(6):
            for j in range(6):
                if board.board[i][j].is_bomb:
                    self.assertEqual(board.checkTile(i, j), False)
                else:
                    num_bombs = board.checkTile(i, j)
                    self.assertTrue(0 <= num_bombs <= 8)


if __name__ == '__main__':
    unittest.main()
