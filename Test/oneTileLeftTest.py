from hand import*
from tile import *

def test_one_tile_left():

    hand = Hand()
    hand.add_tiles({Tile(Shape.CLOVER, Color.GREEN)})
    hand.remove_from_hand({(-1, 6): Tile(Shape.CLOVER, Color.GREEN)})
    assert len(hand.hand) == 0
