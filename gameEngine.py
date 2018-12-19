from Board import *
from shape import *
from color import *
from tile import *
from hand import *
from bag import Bag
from player import *

class GameEngine:

    def __init__(self):
        self.bag = Bag()
        self.bag.createTiles()
        self.bag.shuffleTiles()
        self.board = Board()
        self.player_list = []
        for strategy_num in range(1, 5):
            self.player_list.append(Player(strategy_num))

    def playGame(self):
        for player in self.player_list:
            first_tiles = self.bag.drawFromBag(6)
            player.hand.add_tiles(first_tiles)
            player.strategy = 0

        rounds_played = 0
        game_over = False
        while not game_over:
            for player in self.player_list:
                if not game_over:
                    play_dict = player.find_where_to_play(self.board)
                    print("Tiles in hand: " + str(len(player.hand.hand)))
                    player.hand.remove_from_hand(play_dict)
                    print("Tiles in hand: " + str(len(player.hand.hand)))
                    self.board.add_to_board(play_dict)
                    points_this_turn = self.board.score_play(play_dict)
                    player.total_points += points_this_turn
                    tiles_to_replenish_hand = self.bag.drawFromBag(len(play_dict))
                    player.hand.add_tiles(tiles_to_replenish_hand)
                    print("Tiles in hand: " + str(len(player.hand.hand)))
                    if len(player.hand.hand) == 0:
                        game_over = True
                    print(player.strategy, points_this_turn)

            print("Round: " + str(rounds_played))
            rounds_played += 1

        print(rounds_played)
        for player in self.player_list:
            print("Strategy: " + str(player.strategy) + " Points: " + str(player.total_points))





