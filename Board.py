from shape import Shape
from color import Color
from tile import Tile

class Board:
    def __init__(self):
        self.tiles_on_board = {}

    def add_to_board(self, tiles_to_play):
        for key, value in tiles_to_play.items():
            self.tiles_on_board[key] = value
        print(self.tiles_on_board)

    def find_spots(self):
        return self.find_spots_any_board(self.tiles_on_board)

    def find_spots_any_board(self, board):
        possible_plays = set()
        for coordinates in board:
            x = coordinates[0]
            y = coordinates[1]
            possible_plays.add((x + 1, y))
            possible_plays.add((x - 1, y))
            possible_plays.add((x, y + 1))
            possible_plays.add((x, y - 1))
        #print(possible_plays)
        for coordinates in board:
            x = coordinates[0]
            y = coordinates[1]
            if ((x, y)) in possible_plays:
                possible_plays.remove((x, y))
        print(possible_plays)
        return possible_plays

    def find_similar_tiles(self, tile):
        similar_tiles = []
        tile_color = tile.color
        tile_shape = tile.shape
        for shape in Shape:
            if shape != tile_shape:
                tile1 = Tile(shape, tile_color)
                similar_tiles.append(tile1)

        for color in Color:
            if color != tile_color:
                tile1 = Tile(tile_shape, color)
                similar_tiles.append(tile1)
        #print(*similar_tiles, sep='\n')
        return similar_tiles

    def find_legal_plays(self):
        return self.find_legal_plays_any_board(self.tiles_on_board)

    def find_legal_plays_any_board(self, board):
        spots = self.find_spots_any_board(board)
        plays_dict = {}
        for spot in spots:
            x = spot[0]
            y = spot[1]
            num = 1
            plays_shortlist = set()
            if_statement_execution = False
            print("I'm at " + str(x) + ' ' + str(y))
            if (x, y + 1) in board:
                num = 1
                tile = board[(x, y + 1)]
                if if_statement_execution == False:
                    possible_tiles = self.find_similar_tiles(board[(x, y + 1)])

                while (x, y + num) in board:
                    plays_shortlist = set()
                    print("Possible Tiles1: " + str(possible_tiles))
                    print("Num " + str(num))
                    tile1 = board[(x, y + num)]
                    print(board[(x, y + num)])
                    if board[(x, y + num)].color == tile.color:
                        for tiles in possible_tiles:
                            if tiles.color == tile.color and tiles.shape != board[(x, y + num)].shape:
                                plays_shortlist.add(tiles)
                                #print(tiles)


                    if board[(x, y + num)].shape == tile.shape:
                        for tiles in possible_tiles:
                            if tiles.shape == tile.shape and tiles.color != board[(x, y + num)].color:
                                plays_shortlist.add(tiles)
                                #print(tiles)
                    possible_tiles = plays_shortlist
                    num += 1

                print("\n")
                print(*plays_shortlist, sep='\n')
                if_statement_execution = True

            if (x + 1, y) in board:
                num = 1
                tile = board[(x + 1, y)]
                if if_statement_execution == False:
                    possible_tiles = self.find_similar_tiles(board[(x + 1, y)])

                while (x + num, y) in board:
                    print("Possible Tiles2: " + str(possible_tiles))
                    print("Num " + str(num))
                    plays_shortlist = set()
                    if board[(x + num, y)].color == tile.color:
                        for tiles in possible_tiles:
                            if tiles.color == tile.color and tiles.shape != board[(x + num, y)].shape:
                                plays_shortlist.add(tiles)
                                #print(tiles)

                    if board[(x + num, y)].shape == tile.shape:
                        for tiles in possible_tiles:
                            if tiles.shape == tile.shape and tiles.color != board[(x + num, y)].color:
                                plays_shortlist.add(tiles)
                                #print(tiles)
                    possible_tiles = plays_shortlist
                    num += 1
                print("\n")
                print(*plays_shortlist, sep='\n')
                if_statement_execution = True

            if (x, y - 1) in board:
                num = 1
                tile = board[(x, y - 1)]
                if not if_statement_execution:
                    possible_tiles = self.find_similar_tiles(board[(x, y - 1)])

                while (x, y - num) in board:
                    print("Possible Tiles3: " + str(possible_tiles))
                    print("Num " + str(num))
                    plays_shortlist = set()
                    if board[(x, y - num)].color == tile.color:
                        for tiles in possible_tiles:
                            if tiles.color == tile.color and tiles.shape != board[(x, y - num)].shape:
                                plays_shortlist.add(tiles)
                                #print(tiles)

                    if board[(x, y - num)].shape == tile.shape:
                        for tiles in possible_tiles:
                            if tiles.shape == tile.shape and tiles.color != board[(x, y - num)].color:
                                plays_shortlist.add(tiles)
                                #print(tiles)
                    possible_tiles = plays_shortlist
                    num += 1
                print("\n")
                print(*plays_shortlist, sep='\n')
                if_statement_execution = True

            if (x - 1, y) in board:
                num = 1
                tile = board[(x - 1, y)]
                if if_statement_execution == False:
                    possible_tiles = self.find_similar_tiles(board[(x - 1, y)])

                while (x - num, y) in board:
                    print("Possible Tiles4: " + str(possible_tiles))
                    print("Num " + str(num))
                    plays_shortlist = set()
                    if board[(x - num, y)].color == tile.color:
                        for tiles in possible_tiles:
                            if tiles.color == tile.color and tiles.shape != board[(x - num, y)].shape:
                                plays_shortlist.add(tiles)
                                #print(tiles)

                    if board[(x - num, y)].shape == tile.shape:
                        for tiles in possible_tiles:
                            if tiles.shape == tile.shape and tiles.color != board[(x - num, y)].color:
                                plays_shortlist.add(tiles)
                                #print(tiles)
                    possible_tiles = plays_shortlist
                    num += 1
                print("\n")
                print(*plays_shortlist, sep='\n')
                if_statement_execution = True

            plays_dict[spot] = plays_shortlist
            print(plays_dict)
        return plays_dict

    def find_plays_from_hand(self, all_plays, in_hand):
        plays_from_hand = {}
        for coordinates, legal_tiles in all_plays.items():
            if set.intersection(legal_tiles, in_hand):
                plays_from_hand[coordinates] = set.intersection(legal_tiles, in_hand)

        print(plays_from_hand)
        return plays_from_hand

    def multiple_tile_plays(self, plays_using_hand, tiles_on_board, in_hand):
        list_of_play_dictionaries = []
        num = 0
        for coordinates, tiles in plays_using_hand.items():
            print(coordinates)
            print(tiles)
            x = coordinates[0]
            y = coordinates[1]

            for tile in tiles:
                mock_board = tiles_on_board.copy()
                mock_board[coordinates] = tile
                list_of_play_dictionaries.append({coordinates: tile})
                num = 0
                executed = True
                while (x, y + num) in mock_board:
                    legal_plays = self.find_legal_plays_any_board(mock_board)
                    plays_dictionary = self.find_plays_from_hand(legal_plays, in_hand)

                    if (x, y + num + 1) not in mock_board:

                        if (x, y + num + 1) in plays_dictionary:
                            tiles_for_place = plays_dictionary[(x, y + num + 1)]

                            for tile1 in tiles_for_place:
                                mock_board[(x, y + num + 1)] = tile1

                                if executed == True:
                                    dict1 = {coordinates: tile, (x, y + 1 + num): tile1}
                                    list_of_play_dictionaries.append({coordinates: tile, (x, y + 1 + num): tile1})
                                    executed = False
                                else:
                                    dict2 = dict1.copy()
                                    dict2[(x, y + num + 1)] = tile1
                                    list_of_play_dictionaries.append(dict2)
                                    dict1 = dict2.copy()

                    num += 1
                #del mock_board[(x, y + num - 1)]
                num = 0

                mock_board = tiles_on_board.copy()
                mock_board[coordinates] = tile
                executed = True
                while (x + num, y) in mock_board:
                    legal_plays = self.find_legal_plays_any_board(mock_board)
                    plays_dictionary = self.find_plays_from_hand(legal_plays, in_hand)

                    if (x + num + 1) not in mock_board:

                        if (x + num + 1, y) in plays_dictionary:
                            tiles_in_dict = plays_dictionary[(x + num + 1, y)]
                            for tile1 in tiles_in_dict:
                                mock_board[(x + num + 1, y)] = tile1

                                if executed == True:
                                    dict1 = {coordinates:tile, (x + num + 1, y): tile1}
                                    list_of_play_dictionaries.append(dict1)
                                    executed = False

                                else:
                                    dict2 = dict1.copy()
                                    dict2[(x + num + 1, y)] = tile1
                                    list_of_play_dictionaries.append(dict2)
                                    dict1 = dict2.copy()

                    num += 1
                #del mock_board[(x + num - 1, y)]
                num = 0

                mock_board = tiles_on_board.copy()
                mock_board[coordinates] = tile
                executed = True
                while (x, y - num) in mock_board:
                    legal_plays = self.find_legal_plays_any_board(mock_board)
                    plays_dictionary = self.find_plays_from_hand(legal_plays, in_hand)

                    if (x, y - num - 1) not in mock_board:

                        if (x, y - num - 1) in plays_dictionary:
                            tiles_in_dict = plays_dictionary[(x, y - num - 1)]
                            for tile1 in tiles_in_dict:
                                mock_board[(x, y - num - 1)] = tile1

                                if executed == True:
                                    dict1 = {coordinates:tile, (x, y - 1 - num):tile1}
                                    list_of_play_dictionaries.append(dict1)
                                    executed = False

                                else:
                                    dict2 = dict1.copy()
                                    dict2[(x, y - num - 1)] = tile1
                                    list_of_play_dictionaries.append(dict2)
                                    dict1 = dict2.copy()

                    num +=1
                #del mock_board[(x, y - num + 1)]
                num = 0

                mock_board = tiles_on_board.copy()
                mock_board[coordinates] = tile
                executed = True
                while (x - num, y) in mock_board:
                    legal_plays = self.find_legal_plays_any_board(mock_board)
                    plays_dictionary = self.find_plays_from_hand(legal_plays, in_hand)

                    if (x - num - 1, y) not in mock_board:

                        if (x - num - 1, y) in plays_dictionary:
                            tiles_in_dict = plays_dictionary[(x - num - 1, y)]
                            for tile1 in tiles_in_dict:
                                mock_board[(x - num - 1, y)] = tile1

                                if executed == True:
                                    dict1 = {coordinates:tile, (x - 1 - num, y):tile1}
                                    list_of_play_dictionaries.append(dict1)
                                    executed = False

                                else:
                                    dict2 = dict1.copy()
                                    dict2[(x - num - 1, y)] = tile1
                                    list_of_play_dictionaries.append(dict2)
                                    dict1 = dict2.copy()

                    num += 1
                #del mock_board[(x - num + 1, y)]
            print('\n')
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(list_of_play_dictionaries)
