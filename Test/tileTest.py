import pytest
from tile import Tile
from shape import Shape
from color import Color

def test_tile():
    tile1 = Tile("circle", "purple")
    assert tile1.shape == "circle"
    assert tile1.color == "purple"

def test_tileAttributes():
    tile_list = []
    for shape in Shape:
        for color in Color:
            tile2 = Tile(shape, color)
            tile_list.append(tile2)
            print(tile2)
    assert len(tile_list) == 36