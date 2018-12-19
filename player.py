from hand import *
import random

class Player:

    def __init__(self, strategy):
        self.strategy = strategy
        self.hand = Hand()
        self.total_points = 0

    def find_where_to_play(self, board):
        if len(board.tiles_on_board) > 0:
            plays = board.find_legal_plays()
            plays_hand = board.find_plays_from_hand(plays, self.hand.hand)
            list_plays = board.multiple_tile_plays(plays_hand, board.tiles_on_board, self.hand.hand)
            if len(list_plays) > 0:
                return random.choice(list_plays)
            else:
                return {}
        else:
            return {(0, 0): self.hand.hand[0]}
