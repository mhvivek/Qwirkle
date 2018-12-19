from hand import  *
from tile import *

def test_remove_from_hand():
    hand = Hand()
    tiles_hand = [Tile(Shape.STAR, Color.GREEN), Tile(Shape.STAR, Color.GREEN), Tile(Shape.SQUARE, Color.GREEN), Tile(Shape.STAR, Color.ORANGE)]
    hand.add_tiles(tiles_hand)
    tiles_to_remove = {(0, 0): Tile(Shape.STAR, Color.GREEN)}
    hand.remove_from_hand(tiles_to_remove)
    assert len(hand.hand) == 3

def test_remove_from_hand2():
    hand = Hand()
    tiles_hand = [Tile(Shape.STAR, Color.GREEN), Tile(Shape.STAR, Color.GREEN), Tile(Shape.SQUARE, Color.GREEN), Tile(Shape.STAR, Color.ORANGE)]
    hand.add_tiles(tiles_hand)
    tiles_to_remove = {(0, 0): Tile(Shape.STAR, Color.GREEN), (1, 0): Tile(Shape.SQUARE, Color.GREEN)}
    hand.remove_from_hand(tiles_to_remove)
    assert len(hand.hand) == 2