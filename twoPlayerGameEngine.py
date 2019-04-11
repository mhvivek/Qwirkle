from Board import *
from shape import *
from color import *
from tile import *
from hand import *
from bag import Bag
from player import *
import csv

class twoPlayerGameEngine:

    def __init__(self):
        self.bag = Bag()
        self.bag.createTiles()
        self.bag.shuffleTiles()
        self.board = Board()
        self.player_list = []
        self.strategy_to_player = {}
        for strategy_num in range(1, 3):
             self.player_list.append(Player(strategy_num))

    def playGame(self, strategy_list, order):
        first_player = strategy_list[0]
        second_player = strategy_list[1]
        for player in self.player_list:
            first_tiles = self.bag.drawFromBag(6)
            player.hand.add_tiles(first_tiles)

        self.player_list[0].strategy = strategy_list[0]
        self.player_list[1].strategy = strategy_list[1]
        #self.player_list[2].strategy = strategy_list[2]
        #self.player_list[3].strategy = strategy_list[3]
        self.strategy_to_player[strategy_list[0]] = self.player_list[0]
        self.strategy_to_player[strategy_list[1]] = self.player_list[1]
        #self.strategy_to_player[strategy_list[2]] = self.player_list[2]
        #self.strategy_to_player[strategy_list[3]] = self.player_list[3]

        rounds_played = 0
        game_over = False
        first_turn = True
        while not game_over:
            for player in self.player_list:
                for tile in player.hand.hand:
                    print(tile.color, tile.shape)
                if not game_over:
                    if first_turn:
                        play_dict = player.hand.find_first_play()
                        first_turn = False
                        print("Tiles in hand: " + str(len(player.hand.hand)))
                        player.hand.remove_from_hand(play_dict)
                        print("Tiles in hand: " + str(len(player.hand.hand)))
                        self.board.add_to_board(play_dict)
                        print("Play: " + str(play_dict))
                        for place, tile in play_dict.items():
                            print(tile.color, tile.shape)
                        points_this_turn = len(play_dict)
                        player.total_points += points_this_turn
                        tiles_to_replenish_hand = self.bag.drawFromBag(len(play_dict))
                        player.hand.add_tiles(tiles_to_replenish_hand)
                        print("Tiles in hand: " + str(len(player.hand.hand)))
                    else:
                        play_dict = player.find_where_to_play(self.board, self.bag.tile_list)
                        if len(play_dict) > 0:
                            print("Tiles in hand: " + str(len(player.hand.hand)))
                            player.hand.remove_from_hand(play_dict)
                            print("Tiles in hand: " + str(len(player.hand.hand)))
                            self.board.add_to_board(play_dict)
                            print("Play: " + str(play_dict))
                            for place, tile in play_dict.items():
                                print(tile.color, tile.shape)
                            points_this_turn = self.board.score_play(play_dict, False)
                            player.total_points += points_this_turn
                            tiles_to_replenish_hand = self.bag.drawFromBag(len(play_dict))
                            player.hand.add_tiles(tiles_to_replenish_hand)
                            print("Tiles in hand: " + str(len(player.hand.hand)))
                        else:
                            if len(self.bag.tile_list) > 5:
                                print("Trade-in ")
                                num = 0
                                tiles_to_remove = {}
                                points_this_turn = 0
                                for tile in player.hand.hand:
                                    tiles_to_remove[(0, num)] = tile
                                    self.bag.tile_list.append(tile)
                                    num += 1
                                player.hand.remove_from_hand(tiles_to_remove)
                                self.bag.shuffleTiles()
                                tiles_to_replenish_hand = self.bag.drawFromBag(6)
                                player.hand.add_tiles(tiles_to_replenish_hand)
                            else:
                                points_this_turn = 0
                                player.total_points += 0

                    if len(player.hand.hand) == 0:
                        player.total_points += 6
                        game_over = True
                    if rounds_played > 50:
                        game_over = True
                    print(player.strategy, points_this_turn)


            print("Round: " + str(rounds_played))
            rounds_played += 1

        print(rounds_played)
        for player in self.player_list:
            print("Strategy: " + str(player.strategy) + " Points: " + str(player.total_points))

        winning_score = 0
        for strategy, player in self.strategy_to_player.items():
            if player.total_points > winning_score:
                    winning_score = player.total_points

        if order == 1:
            game_data = [rounds_played, self.strategy_to_player[first_player].total_points, self.strategy_to_player[second_player].total_points,
                         strategy_list.index(first_player) + 1, strategy_list.index(second_player) + 1,
                         int(self.strategy_to_player[first_player].total_points == winning_score), int(self.strategy_to_player[second_player].total_points == winning_score)]
        if order == 2:
            game_data = [rounds_played, self.strategy_to_player[second_player].total_points,
                         self.strategy_to_player[first_player].total_points,
                         strategy_list.index(second_player) + 1, strategy_list.index(first_player) + 1,
                         int(self.strategy_to_player[second_player].total_points == winning_score),
                         int(self.strategy_to_player[first_player].total_points == winning_score)]
        # game_data = [rounds_played, self.strategy_to_player[0].total_points, self.strategy_to_player[1].total_points,
        #              self.strategy_to_player[2].total_points, self.strategy_to_player[3].total_points,
        #              strategy_list.index(0) + 1, strategy_list.index(1) + 1, strategy_list.index(2) + 1,
        #              strategy_list.index(3) + 1,
        #              int(self.strategy_to_player[0].total_points == winning_score),
        #              int(self.strategy_to_player[1].total_points == winning_score),
        #              int(self.strategy_to_player[2].total_points == winning_score),
        #              int(self.strategy_to_player[3].total_points == winning_score)]

        return game_data







