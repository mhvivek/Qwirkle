import pytest
from tile import Tile
from shape import Shape
from color import Color

def test_tile():
    tile1 = Tile("circle", "purple")
    assert tile1.shape == "circle"
    assert tile1.color == "purple"

def test_tile_equality():
    tile1 = Tile(Shape.CLOVER, Color.ORANGE)
    tile2 = Tile(Shape.CLOVER, Color.ORANGE)
    print(hash(tile1))
    print(hash(tile2))
    assert tile1 == tile2
