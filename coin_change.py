import sys

if __name__ == '__main__':

    coins = [2, 5, 3, 6]
    target_money = 10
    coin_count = len(coins)

    combinations = [1] + [0] * target_money

    for coin_index in range(coin_count):

        print("coin_index", coin_index)

        # print("Combinations before processing coin {}: {}".format(coins[coin_index], combinations))

        for money in range(coins[coin_index], target_money + 1):

            print(
                "money: ", money,
                ", coin: ", coins[coin_index],
                ", money - coins[coin_index]: ", money - coins[coin_index],
                ", combinations[money - coins[coin_index]]", combinations[money - coins[coin_index]])

            if (combinations[money - coins[coin_index]]) > 0:

                # print("Combinations for {} added to combinations for {} : {} += {}".format(money - coins[coin_index], money, combinations[money], combinations[money - coins[coin_index]]))

                combinations[money] += combinations[money - coins[coin_index]]

        # print("Combinations after processing coin {}: {}".format(coins[coin_index], combinations))

    # print("Combinations for {} : {}".format(target_money, combinations[target_money]))

    print(combinations[target_money])