import pytest
from bag import *
from hand import *

def test_draw():
    bag3 = Bag()
    bag3.createTiles()
    bag3.shuffleTiles()
    new_tiles = bag3.drawFromBag(6)
    hand1 = Hand()
    hand1.add_tiles(new_tiles)
    print(*hand1.hand, sep='\n')
    assert len(hand1.hand) == 6
    hand1.find_combinations()



