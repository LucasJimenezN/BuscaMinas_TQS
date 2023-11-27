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

    def check_while_play_game(self):
        return self.board.is_game_won() == False and self.board.is_game_lost == False

    def check_while_playing_game_user_input(self, letter, number):
        return letter.isalpha() and len(letter) == 1 and number.isdigit() and letter.isupper()

    def check_if_tile_is_valid(self, letter, number):
        return 0 <= letter < self.board.size and 0 <= number < self.board.size

    def play_game(self):
        while self.check_while_play_game():
            letter_tile = input("Which colum do you want to pick: ")
            number_tile = input("Which row do you want to pick: ")
            while not self.check_while_playing_game_user_input(letter_tile, number_tile):
                print("Wrong input, please try again: ")
                letter_tile = input("Which colum do you want to pick: ")
                number_tile = input("Which row do you want to pick: ")
            letter_tile = ord(letter_tile) - 65
            number_tile = int(number_tile) - 1
            if self.check_if_tile_is_valid(letter_tile, number_tile):
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
        if (tile.is_revealed == True):
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
