from color import Color
from shape import Shape

class Hand:
    def __init__(self):
        self.hand = []
        self.reds = set()
        self.yellows = set()
        self.greens = set()
        self.purples = set()
        self.oranges = set()
        self.blues = set()
        self.circles = set()
        self.squares = set()
        self.diamonds = set()
        self.clovers = set()
        self.stars = set()
        self.suns = set()
        self.list_possible_combinations = []


    def add_tiles(self, tiles):
        hand = self.hand.extend(tiles)
        return hand

    def convert_hand_to_set(self):
        return set(self.hand)

    def find_first_play(self):
        biggest_play = []
        for tile in self.hand:
            if tile.color == Color.RED:
                self.reds.add(tile)
            if tile.color == Color.YELLOW:
                self.yellows.add(tile)
            if tile.color == Color.GREEN:
                self.greens.add(tile)
            if tile.color == Color.PURPLE:
                self.purples.add(tile)
            if tile.color == Color.ORANGE:
                self.oranges.add(tile)
            if tile.color == Color.BLUE:
                self.blues.add(tile)
            if tile.shape == Shape.CLOVER:
                self.clovers.add(tile)
            if tile.shape == Shape.CIRCLE:
                self.circles.add(tile)
            if tile.shape == Shape.SQUARE:
                self.squares.add(tile)
            if tile.shape == Shape.DIAMOND:
                self.diamonds.add(tile)
            if tile.shape == Shape.STAR:
                self.stars.add(tile)
            if tile.shape == Shape.SUN:
                self.suns.add(tile)
        self.list_possible_combinations = [self.reds, self.yellows, self.blues, self.greens, self.purples, self.oranges,
                                           self.clovers, self.squares, self.circles, self.diamonds, self.stars, self.suns]
        for possibility in self.list_possible_combinations:
            if len(possibility) > len(biggest_play):
                biggest_play = possibility

        first_play = {}
        num = 0
        for tile in biggest_play:
            first_play[(num, 0)] = tile
            num += 1
        return first_play


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









