from color import Color
from shape import Shape

class Hand:
    hand = []
    reds = []
    yellows = []
    greens = []
    purples = []
    oranges = []
    blues = []
    circles = []
    squares = []
    diamonds = []
    clovers = []
    stars = []
    suns = []

    def add_tiles(self, tiles):
        hand = self.hand.extend(tiles)
        return hand
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






