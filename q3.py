def knapsack(weights, values, capacity):
    n = len(weights)

    # creating 2D array to store the maximum value for each wieght limit and item consideration

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # build the dp array from bottom up
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][capacity]
#assigning values
weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6

#printing result
print(knapsack(weights, values, capacity))
