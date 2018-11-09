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

def test_coordinate_retrieval():
    board2 = Board()
    tile = Tile(Shape.CLOVER, Color.BLUE)
    board2.add_to_board({"3 8": tile, "3 7": tile})
    board2.find_legal_plays()

