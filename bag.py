from tile import Tile
from shape import Shape
from color import Color
from random import shuffle

class Bag:

    def __init__(self):
        self.tile_list = []

    def createTiles(self):
        for copy_tiles in range(1, 4):
            for shape in Shape:
                for color in Color:
                    tile2 = Tile(shape, color)
                    self.tile_list.append(tile2)
                    #print(tile2)
        #print("\n")

    def shuffleTiles(self):
        shuffle(self.tile_list)
        #print(*self.tile_list, sep='\n')
        #print("\n")

    def drawFromBag(self, number_to_remove):
        drawn_tiles = self.tile_list[0:number_to_remove]
        del self.tile_list[0:number_to_remove]
        #print(*self.tile_list, sep='\n')
        #print(*drawn_tiles, sep=",")
        return drawn_tiles
