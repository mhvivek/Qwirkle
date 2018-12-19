from color import Color
from shape import Shape

class Hand:
    def __init__(self):
        self.hand = []
        self.reds = []
        self.yellows = []
        self.greens = []
        self.purples = []
        self.oranges = []
        self.blues = []
        self.circles = []
        self.squares = []
        self.diamonds = []
        self.clovers = []
        self.stars = []
        self.suns = []


    def add_tiles(self, tiles):
        hand = self.hand.extend(tiles)
        return hand

    def convert_hand_to_set(self):
        return set(self.hand)

    def find_combinations(self):
        for tile in self.hand:
            if tile.color == Color.RED:
                self.reds.append(tile)
            if tile.color == Color.YELLOW:
                self.yellows.append(tile)
            if tile.color == Color.GREEN:
                self.greens.append(tile)
            if tile.color == Color.PURPLE:
                self.purples.append(tile)
            if tile.color == Color.ORANGE:
                self.oranges.append(tile)
            if tile.color == Color.BLUE:
                self.blues.append(tile)
            if tile.shape == Shape.CLOVER:
                self.clovers.append(tile)
            if tile.shape == Shape.CIRCLE:
                self.circles.append(tile)
            if tile.shape == Shape.SQUARE:
                self.squares.append(tile)
            if tile.shape == Shape.DIAMOND:
                self.diamonds.append(tile)
            if tile.shape == Shape.STAR:
                self.stars.append(tile)
            if tile.shape == Shape.SUN:
                self.suns.append(tile)
        print(self.reds)
        print(self.yellows)
        print(self.oranges)
        print(self.blues)
        print(self.greens)
        print(self.purples)
        print(self.diamonds)
        print(self.suns)
        print(self.stars)
        print(self.squares)
        print(self.circles)
        print(self.clovers)

    def remove_from_hand(self, tiles_to_remove_dict):
        tiles_to_remove_list = []
        for coordinate, tile in tiles_to_remove_dict.items():
            tiles_to_remove_list.append(tile)
        # for tile in self.hand:
        #         #     if tile in tiles_to_remove_list:
        #         #         self.hand.remove(tile)
        #         #         tiles_to_remove_list.remove(tile)
        for tile in tiles_to_remove_list:
            if tile in self.hand:
                self.hand.remove(tile)









