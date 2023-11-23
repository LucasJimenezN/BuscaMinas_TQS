import unittest
from src.model.boardData import Board
from src.controller.BoardController import BoardController


class TestBoardController(unittest.TestCase):
    def setUp(self):
        self.board = Board(1)
        self.controller = BoardController(self.board)

    def test_start_game(self):
        self.controller.start_game()
        for y in range(self.board.size):
            for x in range(self.board.size):
                self.assertEqual(self.board.checkHidden(x, y), True)

    def test_reveal_tile(self):
        self.controller.reveal_tile(0, 0)
        self.assertEqual(self.board.checkHidden(0, 0), False)

    def test_reveal_mine(self):
        # First, place a mine at (0, 0)
        self.board.get_tile(0, 0).is_bomb = True

        self.controller.reveal_tile(0, 0)
        self.assertEqual(self.board.is_game_won(), False)

    def test_reveal_all_tiles(self):
        # Reveal all non-mine tiles
        for y in range(self.board.size):
            for x in range(self.board.size):
                if not self.board.get_tile(x, y).is_bomb:
                    self.controller.reveal_tile(x, y)

        self.assertEqual(self.board.is_game_won(), True)


if __name__ == '__main__':
    unittest.main()
