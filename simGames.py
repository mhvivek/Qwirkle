from gameEngine import *
import time
start = time.time()

with open('qwirkle_sim_data8.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    game_number = 0

    for sim in range(1, 2):
        strategy_list = [0, 1, 2, 3]
        for strategy in strategy_list:
            reduced_strategy_list = strategy_list.copy()
            reduced_strategy_list.remove(strategy)
            for strategy1 in reduced_strategy_list:
                reduced_strategy_list1 = reduced_strategy_list.copy()
                reduced_strategy_list1.remove(strategy1)
                for strategy2 in reduced_strategy_list1:
                    reduced_strategy_list2 = reduced_strategy_list1.copy()
                    reduced_strategy_list2.remove(strategy2)
                    for strategy3 in reduced_strategy_list2:
                        strategy_order = []
                        strategy_order.append(strategy)
                        strategy_order.append(strategy1)
                        strategy_order.append(strategy2)
                        strategy_order.append(strategy3)

                        game = GameEngine()
                        game_number += 1
                        print('\n')
                        print("!!!!! Game: " + str(game_number))
                        print('\n')
                        simulation_data = game.playGame(strategy_order)

                        print(simulation_data)

                        writer.writerow(simulation_data)

csvfile.close()
end = time.time()
print(end - start)
