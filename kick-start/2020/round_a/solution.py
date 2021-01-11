def knapsack(N, B, houses):
    """
    :param N: number of houses
    :param B: budget
    :param houses: prices
    :return: max number of houses you can buy
    """
    matrix = [[0 for i in range(B + 1)] for j in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, B + 1):
            matrix[i][j] = max(1 + matrix[i - 1][j - 1], matrix[i][j - 1])
    print(matrix)
    return 2


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(
                    val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w]
                )
            else:
                K[i][w] = K[i - 1][w]
    print(K)
    return K[n][W]


if __name__ == "__main__":

    # Driver code
    val = [1, 1, 1]
    wt = [10, 20, 30]  # houses
    W = 60  # B
    n = len(val)  # N
    print(knapSack(W, wt, val, n))

    print(knapsack((n, W,)))

# """
# This is how you read input from the platform
# """
# # input() reads a string with a line of input,
# stripping the ' ' (newline) at the end.
# # This is all you need for most problems.
# t = int(input())  # read a line with a single integer
# for i in range(1, t + 1):
#     N, B = [
#         int(s) for s in input().split(" ")
#     ]  # read a list of integers, 2 in this case
#     houses = [int(s) for s in input().split(" ")]
#
#     print("Case #{}: {}".format(i, knapsack(N, B, houses)))
#     # check out .format's specification for more formatting options
