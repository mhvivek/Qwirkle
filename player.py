from hand import *
import random
import copy
from Board import *

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

    def find_where_to_play(self, board, bag_tiles):
        scored_mock_plays = {}
        high_score = 0
        multiple_times = False
        trade_in = False
        if len(board.tiles_on_board) > 0:
            plays = board.find_legal_plays()
            plays_hand = board.find_plays_from_hand(plays, self.hand.hand)
            list_plays = board.multiple_tile_plays(plays_hand, board.tiles_on_board, self.hand.hand)

            if self.strategy == 0:
                for play in list_plays:
                    mock_board = Board()
                    mock_board.tiles_on_board = board.tiles_on_board.copy()
                    mock_board.add_to_board(play)
                    mock_score = mock_board.score_play(play, False)
                    scored_mock_plays[mock_score] = play
                for score, may_play in scored_mock_plays.items():
                    if not multiple_times:
                        high_score = score
                        multiple_times = True
                    else:
                        if score > high_score:
                            high_score = score
                return scored_mock_plays[high_score]

            if self.strategy == 1:
                for play in list_plays:
                    mock_board = Board()
                    mock_board.tiles_on_board = board.tiles_on_board.copy()
                    mock_board.add_to_board(play)
                    mock_score = mock_board.score_play(play, False)
                    scored_mock_plays[mock_score] = play
                for score, may_play in scored_mock_plays.items():
                    if not multiple_times:
                        high_score = score
                        multiple_times = True
                    else:
                        if score > high_score:
                            high_score = score
                if high_score < 6 and len(bag_tiles) > 6:
                    scored_mock_plays[high_score] = {}
                return scored_mock_plays[high_score]

            if self.strategy == 2:
                most_tiles_to_play = 0
                to_play = {}
                num = 0
                high_score = 0
                for play in list_plays:
                    if not multiple_times:
                        most_tiles_to_play = len(play)
                        to_play[most_tiles_to_play] = play
                        multiple_times = True
                    else:
                        if len(play) > most_tiles_to_play:
                            to_play = {}
                            most_tiles_to_play = len(play)
                            to_play[most_tiles_to_play] = play
                        if len(play) == most_tiles_to_play:
                            to_play[most_tiles_to_play - num] = play
                    scored_mock_plays[high_score] = to_play
                    num += 1
                if len(to_play) > 1:
                    scored_mock_plays = {}
                    for number, play in to_play.items():
                        mock_board = Board()
                        mock_board.tiles_on_board = board.tiles_on_board.copy()
                        mock_board.add_to_board(play)
                        mock_score = mock_board.score_play(play, False)
                        scored_mock_plays[mock_score] = play
                    for score, may_play in scored_mock_plays.items():
                        if not multiple_times:
                            high_score = score
                            multiple_times = True
                        else:
                            if score > high_score:
                                high_score = score
                return scored_mock_plays[high_score]

            if self.strategy == 3:
                for play in list_plays:
                    mock_board = Board()
                    mock_board.tiles_on_board = board.tiles_on_board.copy()
                    mock_board.add_to_board(play)
                    mock_score = mock_board.score_play(play, True)
                    scored_mock_plays[mock_score] = play
                for score, may_play in scored_mock_plays.items():
                    if not multiple_times:
                        high_score = score
                        multiple_times = True
                    else:
                        if score > high_score:
                            high_score = score
                return scored_mock_plays[high_score]
            if self.strategy == 4:
                if len(list_plays) > 0:
                    return random.choice(list_plays)
                else:
                    return {}
        else:
            return {(0, 0): self.hand.hand[0]}
