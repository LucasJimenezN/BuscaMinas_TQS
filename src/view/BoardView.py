import string
from ..view.BoardView import BoardView
from ..model.boardData import Board
from ..model.boardData import Tile

class BoardView:
    def __init__(self, controller):
        self.controller = controller

    def display_board(self):
        print(' ', end=' ')
        for i in range(self.controller.board.size):
            print(string.ascii_uppercase[i], end=' ')
        print()

        for i, row in enumerate(self.controller.board.tiles):
            print(i+1, end=' ')
            for tile in row:
                print(tile, end=' ')
            print()

    def display_loss_message(self):
        print("You hit a mine! Game over.")

    def display_win_message(self):
        print("Congratulations, you cleared the board!")