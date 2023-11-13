from ..view.BoardView import BoardView
from ..model.boardData import Board
from ..model.boardData import Board

class BoardController:
    def __init__(self, board):
        self.board = board
        self.view = BoardView(self)

    def start_game(self):
        self.view.display_board()

    def reveal_tile(self, x, y):
        tile = self.board.get_tile(x, y)
        tile.reveal()

        if tile.is_mine:
            self.view.display_loss_message()
        elif self.board.is_game_won():
            self.view.display_win_message()
        else:
            self.view.display_board()