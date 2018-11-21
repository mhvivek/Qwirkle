from shape import Shape
from color import Color
from tile import Tile

class Board:
    def __init__(self):
        self.tiles_on_board = {}

    def add_to_board(self, tiles_to_play):
        for key, value in tiles_to_play.items():
            self.tiles_on_board[key] = value
        print(self.tiles_on_board)

    def find_legal_plays(self):
        possible_plays = set()
        for coordinates in self.tiles_on_board:
            x, y = coordinates.split(" ")
            possible_plays.add((int(x) + 1, int(y)))
            possible_plays.add((int(x) - 1, int(y)))
            possible_plays.add((int(x), int(y) + 1))
            possible_plays.add((int(x), int(y) - 1))
        print(possible_plays)
        for coordinates in self.tiles_on_board:
            x, y = coordinates.split(" ")
            possible_plays.remove((int(x), int(y)))
        print(possible_plays)
        return possible_plays

    def find_similar_tiles(self, tile):
        similar_tiles = []
        tile_color = tile.color
        tile_shape = tile.shape
        for shape in Shape:
            if shape != tile_shape:
                tile1 = Tile(shape, tile_color)
                similar_tiles.append(tile1)

        for color in Color:
            if color != tile_color:
                tile1 = Tile(tile_shape, color)
                similar_tiles.append(tile1)
        print(*similar_tiles, sep='\n')
        return similar_tiles




