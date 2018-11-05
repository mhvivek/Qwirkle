import pytest
from tile import Tile
from shape import Shape
from color import Color

def test_tile():
    tile1 = Tile("circle", "purple")
    assert tile1.shape == "circle"
    assert tile1.color == "purple"

