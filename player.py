from hand import *
import random

class Player:

    def __init__(self, strategy):
        self.strategy = strategy
        self.hand = Hand()
        self.total_points = 0

    # def find_where_to_play(self, board):
    #     if len(board.tiles_on_board) > 0:
    #         plays = board.find_legal_plays()
    #         plays_hand = board.find_plays_from_hand(plays, self.hand.hand)
    #         list_plays = board.multiple_tile_plays(plays_hand, board.tiles_on_board, self.hand.hand)
    #         if len(list_plays) > 0:
    #             return random.choice(list_plays)
    #         else:
    #             return {}
    #     else:
    #         return {(0, 0): self.hand.hand[0]}

    def find_where_to_play(self, board):
        scored_mock_plays = {}
        high_score = 0
        multiple_times = False
        if len(board.tiles_on_board) > 0:
            plays = board.find_legal_plays()
            plays_hand = board.find_plays_from_hand(plays, self.hand.hand)
            list_plays = board.multiple_tile_plays(plays_hand, board.tiles_on_board, self.hand.hand)
            if self.strategy == 0:
                for play in list_plays:
                    mock_score = board.score_play(play)
                    scored_mock_plays[mock_score] = play
                for score, may_play in scored_mock_plays.items():
                    if not multiple_times:
                        high_score = score
                        multiple_times = True
                    else:
                        if score > high_score:
                            high_score = score
                return scored_mock_plays[high_score]
        else:
            return {(0, 0): self.hand.hand[0]}
