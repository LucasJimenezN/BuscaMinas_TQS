from src.view.BoardView import BoardView
from src.model.boardData import Board
from src.model.userData import User


class BoardController:
    def __init__(self, difficulty):
        self.board = Board(difficulty)
        self.view = BoardView(self)
        self.score = 0

    def start_game(self):
        self.view.display_board()
        self.play_game()

    def play_game(self):
        while self.board.is_game_won() == False and self.board.is_game_lost == False:
            letter_tile = input("Which colum do you want to pick: ")
            number_tile = input("Which row do you want to pick: ")
            while not (letter_tile.isalpha() and len(letter_tile) == 1 and number_tile.isdigit() and
                       letter_tile.isupper()):
                print("Wrong input, please try again: ")
                letter_tile = input("Which colum do you want to pick: ")
                number_tile = input("Which row do you want to pick: ")
            letter_tile = ord(letter_tile) - 65
            number_tile = int(number_tile) - 1
            if 0 <= letter_tile < self.board.size and 0 <= number_tile < self.board.size:
                self.reveal_tile(letter_tile, number_tile)
            else:
                print("Invalid tile. Please try again.")

    def check_tile(self, letter, number):
        if letter < 0 or letter > self.board.size:
            return False
        if number < 0 or number > self.board.size:
            return False
        return True

    def reveal_tile(self, x, y):
        tile = self.board.get_tile(x, y)
        if(tile.is_revealed == True):
            self.view.display_already_revealed()
        tile.reveal()

        if tile.is_bomb:
            self.view.display_board()
            self.view.display_loss_message()
            User.add_user(self, self.score)
            self.board.is_game_lost = True;
        elif self.board.is_game_won():
            self.view.display_board()
            self.view.display_win_message()
            User.add_user(self, self.score)
        else:
            self.score = self.score + 10
            self.view.display_board()
