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

    def find_spots(self):
        possible_plays = set()
        for coordinates in self.tiles_on_board:
            x, y = coordinates.split(" ")
            possible_plays.add((int(x) + 1, int(y)))
            possible_plays.add((int(x) - 1, int(y)))
            possible_plays.add((int(x), int(y) + 1))
            possible_plays.add((int(x), int(y) - 1))
        #print(possible_plays)
        for coordinates in self.tiles_on_board:
            x, y = coordinates.split(" ")
            if ((int(x), int(y))) in possible_plays:
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
        #print(*similar_tiles, sep='\n')
        return similar_tiles

    def find_legal_plays(self):
        spots = self.find_spots()
        for spot in spots:
            x = spot[0]
            y = spot[1]
            num = 2
            plays_shortlist = []
            if str(x) + " " + str(y + 1) in self.tiles_on_board:
                tile = self.tiles_on_board[str(x) + " " + str(y + 1)]
                possible_tiles = self.find_similar_tiles(self.tiles_on_board[str(x) + " " + str(y + 1)])
                #print(*possible_tiles, sep='\n')
                while str(x) + " " + str(y + num) in self.tiles_on_board:

                    if self.tiles_on_board[str(x) + " " + str(y + num)].color == tile.color:
                        for tiles in possible_tiles:
                            if tiles.color == tile.color and tiles.shape != self.tiles_on_board[str(x) + " " + str(y + num)].shape:
                                plays_shortlist.append(tiles)
                                print(tiles)


                    if self.tiles_on_board[str(x) + " " + str(y + num)].shape == tile.shape:
                        for tiles in possible_tiles:
                            if tiles.shape == tile.shape and tiles.color != self.tiles_on_board[str(x) + " " + str(y + num)].color:
                                plays_shortlist.append(tiles)
                                print(tiles)



                    num += 1
                print("\n")
                print(*plays_shortlist, sep='\n')

            # if str(x + 1) + " " + str(y) in self.tiles_on_board:
            #     self.find_similar_tiles(self.tiles_on_board[str(x + 1) + " " + str(y)])
            # if str(x) + " " + str(y - 1) in self.tiles_on_board:
            #     self.find_similar_tiles(self.tiles_on_board[str(x) + " " + str(y - 1)])
            # if str(x - 1) + " " + str(y) in self.tiles_on_board:
            #     self.find_similar_tiles(self.tiles_on_board[str(x - 1) + " " + str(y)])










