class Tile:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return str(self.color) + " " + str(self.shape)