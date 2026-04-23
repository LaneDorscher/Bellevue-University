## Author: Lane Dorscher
## Date: 04/10/2026

def longest_common_subsequence(s1, s2):
    """
    Find and return the longest common subsequence between 's1' and 's2'.
    """
    table = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Fill the table bottom-up
    for i in range(1, len(table)):
        for j in range(1, len(table[0])):

            # If characters match, extend the LCS
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                # Otherwise, take the best from top or left
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # Reconstruct the LCS by backtracking
    i = len(table) - 1
    j = len(table[0]) - 1
    lcs = []

    while i > 0 and j > 0:
        # If characters match, it is part of the LCS
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        # Move toward the larger of the two neighboring values
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse because we built the LCS backwards
    return "".join(reversed(lcs))

def knapsack(weights, values, W):
    """
    Solve the 0/1 knapsack problem and return the maximum total value that can be obtained with the given weights and values and a knapsack of capacity 'W'.
    """

    table = [[0] * (W + 1) for _ in range(len(values) + 1)]
    
    for i in range(1, len(table)):
        for w in range(1, len(table[0])):

            # If the current item is too heavy, exclude it
            if weights[i - 1] > w:
                table[i][w] = table[i - 1][w]
            else:
                # Choose the better option: exclude or include the item
                table[i][w] = max(
                    table[i - 1][w],  # Exclude item
                    table[i - 1][w - weights[i - 1]] + values[i - 1]  # Include item
                )

    # The final answer is in the bottom-right cell
    return table[len(table) - 1][W]


def coin_change(coins, amount):
    """
    Given different coin denominations in 'coins' and a total amount 'amount', find the minimum number of coins that make up that amount.
    Return -1 if that amount cannot be made up by any combination of the coins.
    """

    ##represents the "infinite" amount which is just greater than the possible coin count
    inf = amount + 1 

    ## initialize list for minimum coins
    minCoins = [inf] * inf
    minCoins[0] = 0
    
    for coin in coins:
        for amt in range(coin, inf):
            if (minCoins[amt - coin] + 1 < minCoins[amt]):
                minCoins[amt] = minCoins[amt - coin] + 1

    # If the target amount was never updated, it is not possible to receive exact change
    if (minCoins[amount] == inf):
        return -1
    return minCoins[amount]




