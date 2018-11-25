class Tile:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return str(self.shape) + " " + str(self.color)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return (hash(self.shape) ^
                hash(self.color))
