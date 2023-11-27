import unittest
from unittest.mock import patch
from src.controller.BoardController import BoardController
from allpairspy import AllPairs


class TestBoardController(unittest.TestCase):
    def setUp(self):
        self.controller = BoardController(1)

    def test_reveal_tile(self):
        self.controller.reveal_tile_test(0, 0)
        self.assertEqual(self.controller.board.checkHidden(0, 0), False)

    def test_reveal_mine(self):
        # First, place a mine at (0, 0)
        self.controller.board.get_tile(0, 0).is_bomb = True
        self.controller.reveal_tile_test(0, 0)
        self.assertEqual(self.controller.board.is_game_lost, True)

    def test_reveal_all_tiles(self):
        # Reveal all non-mine tiles
        for y in range(self.controller.board.size):
            for x in range(self.controller.board.size):
                if not self.controller.board.get_tile(x, y).is_bomb:
                    self.controller.reveal_tile_test(x, y)
        self.assertTrue(self.controller.board.is_game_won())

    def test_check_tile(self):
        self.assertTrue(self.controller.check_tile(0, 0))
        self.assertFalse(self.controller.check_tile(-1, 0))
        self.assertFalse(self.controller.check_tile(-1, -1))
        self.assertFalse(self.controller.check_tile(0, -1))
        self.assertTrue(self.controller.check_tile(0, self.controller.board.size - 1))

    def test_check_while_playing_game_user_input(self):
        self.assertTrue(self.controller.check_while_playing_game_user_input('A', "1"))
        self.assertTrue(self.controller.check_while_playing_game_user_input('B', "2"))
        self.assertTrue(self.controller.check_while_playing_game_user_input('C', "5"))
        self.assertFalse(self.controller.check_while_playing_game_user_input('A', "-1"))
        self.assertFalse(self.controller.check_while_playing_game_user_input('', None))
        self.assertFalse(self.controller.check_while_playing_game_user_input('a', "2"))
        self.assertFalse(self.controller.check_while_playing_game_user_input('a', "2"))

    def test_check_if_tile_is_valid(self):
        self.assertTrue(self.controller.check_while_playing_game_user_input('A', "1"))
        self.assertTrue(self.controller.check_while_playing_game_user_input('B', "2"))
        self.assertTrue(self.controller.check_while_playing_game_user_input('C', "3"))
        self.assertFalse(self.controller.check_while_playing_game_user_input('a', "-1"))
        self.assertFalse(self.controller.check_while_playing_game_user_input('z', "0"))
        self.assertFalse(self.controller.check_while_playing_game_user_input('6', "6"))


if __name__ == '__main__':
    unittest.main()
