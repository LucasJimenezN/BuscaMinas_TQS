import random

class Tile:
    def __init__(self):
        self.is_bomb = False
        self.is_revealed = False
    
    def reveal(self):
        self.is_revealed = True

class Board:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = self.initialise()

    def initialise(self):
        if self.difficulty == 1:
            size = 6
            num_bombs = 8
        elif self.difficulty == 2:
            size = 8
            num_bombs = 16
        elif self.difficulty == 3:
            size = 10
            num_bombs = 32
        else:
            raise ValueError("Invalid difficulty level. Choose between 1, 2, or 3.")

        board = [[Tile() for _ in range(size)] for _ in range(size)]

        bomb_positions = random.sample(range(size*size), num_bombs)
        for pos in bomb_positions:
            row = pos // size
            col = pos % size
            board[row][col].is_bomb = True

        return board
    
    def checkHidden(self, x, y):
        if self.board[x][y].is_revealed:
            return True
        else:
            return False


    def checkTile(self, x, y):
        if self.board[x][y].is_bomb:
            return False

        num_bombs = 0
        for i in range(max(0, x-1), min(len(self.board), x+2)):
            for j in range(max(0, y-1), min(len(self.board[0]), y+2)):
                if self.board[i][j].is_bomb:
                    num_bombs += 1

        return num_bombs
    
    def get_tile(self, x, y):
        return self.board[y][x]

    def is_game_won(self):
        for row in self.board:
            for tile in row:
                if not tile.is_bomb and not tile.is_revealed:
                    return False
        return True
