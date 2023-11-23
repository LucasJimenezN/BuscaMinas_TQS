import random


class Tile:
    def __init__(self):
        self.is_bomb = False
        self.is_revealed = False

    def reveal(self):
        self.is_revealed = True

    def print(self):
        if self.is_revealed and self.is_bomb:
            return "X"
        elif self.is_revealed and self.is_bomb == False:
            return "O"
        else:
            return " "


class Board:
    def __init__(self, difficulty):
        self.size = 0
        self.difficulty = difficulty
        self.tiles = self.initialise()
        self.is_game_lost = False

    def initialise(self):
        if self.difficulty == 1:
            self.size = 6
            num_bombs = 8
        elif self.difficulty == 2:
            self.size = 8
            num_bombs = 16
        elif self.difficulty == 3:
            self.size = 10
            num_bombs = 32
        else:
            raise ValueError("Invalid difficulty level. Choose between 1, 2, or 3.")

        Tiles = [[Tile() for _ in range(self.size)] for _ in range(self.size)]

        bomb_positions = random.sample(range(self.size * self.size), num_bombs)
        for pos in bomb_positions:
            row = pos // self.size
            col = pos % self.size
            Tiles[row][col].is_bomb = True

        self.tiles = Tiles
        return Tiles

    def checkHidden(self, x, y):
        if self.tiles[x][y].is_revealed:
            return False
        else:
            return True

    def checkTile(self, x, y):
        if self.tiles[x][y].is_bomb:
            self.is_game_lost = True
            return False

        num_bombs = 0
        for i in range(max(0, x - 1), min(len(self.tiles), x + 2)):
            for j in range(max(0, y - 1), min(len(self.tiles[0]), y + 2)):
                if self.tiles[i][j].is_bomb:
                    num_bombs += 1

        return num_bombs

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def is_game_won(self):
        for row in self.tiles:
            for tile in row:
                if not tile.is_bomb and not tile.is_revealed:
                    return False
        return True
