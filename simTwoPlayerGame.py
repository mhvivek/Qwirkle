from twoPlayerGameEngine import *
import csv
import time
start = time.time()

for strat_list in [[1, 2], [1, 3], [2, 3]]:
    with open('two_player_data_' + str(strat_list[0]) + '_' + str(strat_list[1]) + '.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for order in [1, 2]:
            for sim in range(1, 1801):

                game = twoPlayerGameEngine()
                game_data = game.playGame(strat_list, order)
                writer.writerow(game_data)
                print(game_data)

            strat_list = [strat_list[1], strat_list[0]]

    csvfile.close()
end = time.time()
print(end - start)