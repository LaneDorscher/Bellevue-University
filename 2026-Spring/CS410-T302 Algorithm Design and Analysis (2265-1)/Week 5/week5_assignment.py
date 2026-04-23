def fractional_knapsack(values, weights, capacity):
    """
    Solve the fractional knapsack problem and return the maximum value that can be obtained.
    """
    # pair the item with the v to w ratio
    items = []
    for v,w in zip(values, weights):
        ratio = v / w
        items.append((ratio, v, w))
    
    # Sort items by ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])

    totalValue = 0.0

    for ratio, value, weight in items:
        if capacity == 0: break

        if weight <= capacity:
            totalValue += value
            capacity -= weight
        else:
            f = capacity / weight
            totalValue += (value * f)
            capacity = 0
    
    return totalValue

def coin_change_greedy(coins, amount):
    """
    Using a greedy approach, determine the minimum number of coins needed to make the given amount.
    If it's not possible to make the amount using the given coin denominations, return -1.
    """
    # coins = [1,5,10,25]
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        num = amount // coin ## get the quantifyable amount of coins that could fit into the amount
        amount -= (num * coin) ## subtract the amount the coins equal
        count += num    #increase the coin count by the num of coins used

    if amount is 0:
        return count
    return -1 ## no need for explicit else as both statements exit out

def activity_selection(activities):
    """
    Given a list of 'activities' where each activity is represented as a tuple (start_time, end_time),
    determine the maximum number of activities that can be scheduled without any conflicts.
    Return the list of selected activities.
    """
    # sort the activities by the end time
    activities.sort(key=lambda x: x[1])
    list = []
    list.append(activities[0])

    for activity in activities:
        if activity[0] >= list[len(list) - 1][1]:
            list.append(activity)

    return list
2