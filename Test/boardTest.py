
from Board import *
from shape import *
from color import *
from tile import *
from hand import *

#
# def test_play():
#     board1 = Board()
#     tile = Tile(Shape.CLOVER, Color.BLUE)
#     coordinates = (1, 2)
#     removed_from_hand = {coordinates: tile}
#     board1.add_to_board(removed_from_hand)
#     assert len(board1.tiles_on_board) == 1
#
#
# def test_coordinate_retrieval():
#     board2 = Board()
#     tile = Tile(Shape.CLOVER, Color.BLUE)
#     board2.add_to_board({(3, 8): tile, (3, 7): tile})
#     possible_plays = board2.find_spots()
#     assert possible_plays == {(2, 7), (4, 7), (4, 8), (2, 8), (3, 9), (3, 6)}
#
#
# def test_coordinate_retrieval_one_tile():
#     board2 = Board()
#     tile = Tile(Shape.CLOVER, Color.BLUE)
#     board2.add_to_board({(3, 8): tile})
#     possible_plays = board2.find_spots()
#     assert possible_plays == {(4, 8), (2, 8), (3, 9), (3, 7)}
#
#
# def test_find_similar_tiles():
#     board1 = Board()
#     tile = Tile(Shape.STAR, Color.YELLOW)
#     similar_tiles_test = board1.find_similar_tiles(tile)
#     assert len(similar_tiles_test) == 10
#
#
# def test_find_legal_plays():
#     board1 = Board()
#     tile1 = Tile(Shape.SUN, Color.BLUE)
#     tile2 = Tile(Shape.SUN, Color.ORANGE)
#     tile3 = Tile(Shape.SQUARE, Color.BLUE)
#     tile4 = Tile(Shape.SQUARE, Color.ORANGE)
#     tiles = {(0, 0): tile1, (0, 1): tile3, (1, 0): tile2, (1, -1): tile4}
#     board1.add_to_board(tiles)
#     plays = board1.find_legal_plays()
#     assert plays[(1, 1)] == set()
#     assert plays[(1, -2)] == {Tile(Shape.DIAMOND, Color.ORANGE), Tile(Shape.STAR, Color.ORANGE),
#                               Tile(Shape.CIRCLE, Color.ORANGE), Tile(Shape.CLOVER, Color.ORANGE)}
#     assert plays[(2, -1)] == {Tile(Shape.CLOVER, Color.ORANGE), Tile(Shape.CIRCLE, Color.ORANGE),
#                               Tile(Shape.STAR, Color.ORANGE), Tile(Shape.DIAMOND, Color.ORANGE),
#                               Tile(Shape.SUN, Color.ORANGE), Tile(Shape.SQUARE, Color.BLUE),
#                               Tile(Shape.SQUARE, Color.GREEN), Tile(Shape.SQUARE, Color.PURPLE),
#                               Tile(Shape.SQUARE, Color.YELLOW), Tile(Shape.SQUARE, Color.RED)}
#     assert plays[(-1, 0)] == {Tile(Shape.SUN, Color.RED), Tile(Shape.SUN, Color.YELLOW), Tile(Shape.SUN, Color.PURPLE),
#                               Tile(Shape.SUN, Color.GREEN)}
#
#
# def test_find_plays_from_hand():
#     board1 = Board()
#     tile1 = Tile(Shape.CLOVER, Color.BLUE)
#     tile2 = Tile(Shape.CLOVER, Color.ORANGE)
#     tile3 = Tile(Shape.SQUARE, Color.BLUE)
#     tile4 = Tile(Shape.CLOVER, Color.BLUE)
#     tiles_in_hand = {Tile(Shape.DIAMOND, Color.BLUE),  Tile(Shape.CLOVER, Color.ORANGE)}
#
#     tiles = {(0, 0): tile1, (0, 1): tile3, (1, 0): tile2, (1, -1): tile4}
#     hand1 = Hand()
#     hand1.add_tiles(tiles_in_hand)
#     hand = hand1.convert_hand_to_set()
#     board1.add_to_board(tiles)
#     plays = board1.find_legal_plays()
#     plays_hand = board1.find_plays_from_hand(plays, hand)
#     assert plays_hand[(2, -1)] == {Tile(Shape.CLOVER, Color.ORANGE), Tile(Shape.DIAMOND, Color.BLUE)}
#     assert plays_hand[(-1, 1)] == {Tile(Shape.DIAMOND, Color.BLUE)}
#     assert plays_hand[(0, 2)] == {Tile(Shape.DIAMOND, Color.BLUE)}
#     assert plays_hand[(0, -1)] == {Tile(Shape.DIAMOND, Color.BLUE)}

def test_multiple_tile_play():
    print("$$$$$$$$$$$$$$\n")
    board1 = Board()
    tile1 = Tile(Shape.CLOVER, Color.BLUE)
    tile2 = Tile(Shape.CIRCLE, Color.BLUE)
    tiles_in_hand = {Tile(Shape.DIAMOND, Color.BLUE),  Tile(Shape.STAR, Color.BLUE)}
    tiles = {(0, 0): tile1, (0, 1): tile2}
    hand = Hand()
    hand.add_tiles(tiles_in_hand)
    hand = hand.convert_hand_to_set()
    board1.add_to_board(tiles)
    plays = board1.find_legal_plays()
    plays_hand = board1.find_plays_from_hand(plays, hand)
    board1.multiple_tile_plays(plays_hand, tiles, hand)
    print("**********")
