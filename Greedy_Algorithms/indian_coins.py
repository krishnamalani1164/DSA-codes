def indian_coins_greedy(amount):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = []

    for coin in denominations:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result

amount = 2753
coins_used = indian_coins_greedy(amount)
print("Coins used:", coins_used)
print("Total coins:", len(coins_used))
