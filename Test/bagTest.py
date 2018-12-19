import pytest
from bag import *

def test_creat_tiles():
    bag1 = Bag()
    assert len(bag1.tile_list) == 0
    bag1.createTiles()
    assert len(bag1.tile_list) == 108

#def test_shuffle():

    #bag2 = Bag()
    #bag2.createTiles()
    #bag2.shuffleTiles()

def test_draw():
    bag3 = Bag()
    bag3.createTiles()
    bag3.shuffleTiles()
    bag3.drawFromBag(3)
    assert len(bag3.tile_list) == 105

def test_end_game_draw():
    bag1 = Bag()
    drawn_tiles = bag1.drawFromBag(2)
    assert len(drawn_tiles) == 0


