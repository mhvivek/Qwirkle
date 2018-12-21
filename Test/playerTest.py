from player import *
from tile import *
from Board import *


def test_player():
    player = Player(0)
    board = Board()
    player.hand.add_tiles([Tile(Shape.STAR, Color.GREEN), Tile(Shape.CLOVER, Color.GREEN)])
    board.add_to_board({(0, 0): Tile(Shape.SUN, Color.GREEN)})
    play = player.find_where_to_play(board)
    print(play)