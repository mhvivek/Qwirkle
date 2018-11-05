import pytest
from Board import *
from shape import *
from color import *
from tile import *

def test_play():
    board1 = Board()
    tile = Tile(Shape.CLOVER, Color.BLUE)
    coordinates = "1 2"
    removed_from_hand = {coordinates: tile}
    board1.add_to_board(removed_from_hand)
    assert len(board1.tiles_on_board) == 1

