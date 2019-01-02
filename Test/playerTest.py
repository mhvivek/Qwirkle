from player import *
from tile import *
from Board import *
from bag import *


def test_player():
    player = Player(0)
    board = Board()
    player.hand.add_tiles([Tile(Shape.STAR, Color.GREEN), Tile(Shape.CLOVER, Color.GREEN)])
    board.add_to_board({(0, 0): Tile(Shape.SUN, Color.GREEN)})
    play = player.find_where_to_play(board, [])
    print(play)
def test_player_2():
    player = Player(2)
    board = Board()
    player.hand.add_tiles([Tile(Shape.CIRCLE, Color.PURPLE),
                           Tile(Shape.SUN, Color.ORANGE),
                           Tile(Shape.SUN, Color.GREEN),
                           Tile(Shape.STAR, Color.RED),
                           Tile(Shape.STAR, Color.ORANGE),
                           Tile(Shape.SQUARE, Color.BLUE)])

    board.add_to_board({(0, 0): Tile(Shape.SQUARE, Color.ORANGE),
                        (0, -1): Tile(Shape.SQUARE, Color.RED),
                        (-1, 0): Tile(Shape.CLOVER, Color.ORANGE),
                        (-1, -1): Tile(Shape.SQUARE, Color.ORANGE),
                        (-2, -1): Tile(Shape.SQUARE, Color.GREEN),
                        (1, 0): Tile(Shape.SUN, Color.ORANGE),
                        (1, 1): Tile(Shape.SUN, Color.PURPLE),
                        (1, 2): Tile(Shape.SUN, Color.YELLOW)})
    play = player.find_where_to_play(board, [])
    # print(play[(2, 0)].shape, play[(2, 0)].color)
    # print(play[(2, 1)].shape, play[(2, 1)].color)
    assert play == {(2, 0): Tile(Shape.STAR, Color.ORANGE), (2, 1): Tile(Shape.SUN, Color.ORANGE)} or play == {(2, 0): Tile(Shape.SUN, Color.ORANGE), (2, 1): Tile(Shape.STAR, Color.ORANGE)}

def test_cant_play():
    player = Player(3)
    board = Board()
    bag = Bag()
    player.hand.add_tiles(
        [Tile(Shape.CIRCLE, Color.PURPLE), Tile(Shape.SUN, Color.ORANGE), Tile(Shape.SUN, Color.GREEN),
         Tile(Shape.STAR, Color.PURPLE), Tile(Shape.STAR, Color.ORANGE), Tile(Shape.SQUARE, Color.BLUE)])
    board.add_to_board({(0, 0): Tile(Shape.DIAMOND, Color.RED)})
    play1 = player.find_where_to_play(board, [])
    assert play1 == {}
