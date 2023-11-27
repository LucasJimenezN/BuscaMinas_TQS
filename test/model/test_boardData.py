import unittest
from src.model.boardData import Tile, Board


class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = Tile()

    def test_tile_initialization(self):
        self.assertFalse(self.tile.is_bomb)
        self.assertFalse(self.tile.is_revealed)
        self.assertEqual(self.tile.bombs, 0)

    def test_reveal_tile(self):
        self.tile.reveal()
        self.assertTrue(self.tile.is_revealed)

    def test_print_tile_unrevealed(self):
        result = self.tile.print()
        self.assertEqual(result, " ")
        aux_tile = Tile()
        aux_tile.is_revealed = True
        result = aux_tile.print()
        self.assertEqual(result, aux_tile.bombs)
        aux_tile.is_bomb = True
        result = aux_tile.print()
        self.assertEqual(result, "X")

    def test_print_tile_revealed_not_bomb(self):
        self.tile.reveal()
        result = self.tile.print()
        self.assertEqual(result, 0)

    def test_print_tile_revealed_bomb(self):
        self.tile.reveal()
        self.tile.is_bomb = True
        result = self.tile.print()
        self.assertEqual(result, "X")


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(1)

    def test_board_initialization(self):
        self.assertEqual(self.board.size, 6)
        self.assertFalse(self.board.is_game_lost)
        self.assertEqual(len(self.board.tiles), 6)
        self.assertEqual(len(self.board.tiles[0]), 6)

    def test_check_hidden_tile(self):
        result = self.board.checkHidden(0, 0)
        self.assertTrue(result)

    def test_check_tile_bomb(self):
        self.board.tiles[0][0].is_bomb = True
        result = self.board.checkTile(0, 0)
        self.assertFalse(result)

    def test_check_tile_no_bomb(self):
        result = self.board.checkTile(0, 0)
        self.assertEqual(result, 0)

    def test_get_tile(self):
        tile = self.board.get_tile(0, 0)
        self.assertIsInstance(tile, Tile)

    def test_is_game_won_not_finished(self):
        result = self.board.is_game_won()
        self.assertFalse(result)

    def test_is_game_won_finished(self):
        for row in self.board.tiles:
            for tile in row:
                tile.is_revealed = True
        result = self.board.is_game_won()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
