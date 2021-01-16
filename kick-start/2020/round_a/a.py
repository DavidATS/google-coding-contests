def knapsack(N, B, house_prices):
    """
    :param N: number of houses
    :param B: budget
    :param house_prices: prices
    :return: max number of houses you can buy
    """
    matrix = [[0 for i in range(B + 1)] for j in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, B + 1):
            price = house_prices[i - 1]
            if price <= j:
                matrix[i][j] = max(
                    1 + matrix[i - 1][j - price], matrix[i - 1][j]
                )
            else:
                matrix[i][j] = matrix[i - 1][j]
    return matrix[i][j]


def greedy(N, B, house_prices):
    result = 0
    house_prices.sort()
    for house in house_prices:
        if house <= B:
            result += 1
            B -= house
        else:
            break
    return result


"""
This is how you read input from the platform
"""
# input() reads a string with a line of input,
# stripping the ' ' (newline) at the end.
# This is all you need for most problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N, B = [
        int(s) for s in input().split(" ")
    ]  # read a list of integers, 2 in this case
    houses = [int(s) for s in input().split(" ")]

    print("Case #{}: {}".format(i, greedy(N, B, houses)))
    # check out .format's specification for more formatting options
