from src.view.BoardView import BoardView
from src.model.boardData import Board


class BoardController:
    def __init__(self, difficulty):
        self.board = Board(difficulty)
        self.view = BoardView(self)

    def start_game(self):
        self.view.display_board()
        self.play_game()

    def play_game(self):
        while self.board.is_game_won() == False and self.board.is_game_lost == False:
            letter_tile = ord(input("Which colum do you want to pick: "))
            number_tile = int(input("Which row do you want to pick: "))
            number_tile = number_tile - 1
            while not self.check_tile(letter_tile, number_tile):
                print("Wrong input, please try again: ")
                letter_tile = ord(input("Which colum do you want to pick: "))
                number_tile = int(input("Which row do you want to pick: "))
                number_tile = number_tile - 1

            letter_tile = letter_tile - 65

    def check_tile(self, letter, number):
        if letter < 0 or letter > self.board.size:
            return False
        if number < 0 or number > self.board.size:
            return False
        return True

    def reveal_tile(self, x, y):
        tile = self.board.get_tile(x, y)
        tile.reveal()

        if tile.is_bomb:
            self.view.display_loss_message()
        elif self.board.is_game_won():
            self.view.display_win_message()
        else:
            self.view.display_board()
