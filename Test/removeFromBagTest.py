import pytest
from bag import *

def test_draw():
    bag3 = Bag()
    bag3.createTiles()
    bag3.shuffleTiles()
    new_tiles = bag3.drawFromBag(3)
    assert len(bag3.tile_list) == 105
    assert len(new_tiles) == 3
