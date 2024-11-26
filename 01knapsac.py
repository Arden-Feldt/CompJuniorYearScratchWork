def knapsack(values, weights, capacity):
    n = len(values)  # Number of items
    # DP table where dp[i][b] represents the maximum value for first i items with capacity b
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):  # Loop over each item
        for b in range(capacity + 1):  # Loop over each capacity from 0 to B
            if weights[i - 1] <= b:  # If the item can fit in the knapsack
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - weights[i - 1]] + values[i - 1])
            else:
                dp[i][b] = dp[i - 1][b]  # Can't take the item, keep the previous value
    
    return dp[n][capacity]

# Example usage:
v = [3, 17, 15, 5, 10, 9, 13, 15, 2, 1, 16, 9, 15, 1, 9, 14, 5, 18, 18, 1, 1, 11, 18, 8, 5, 9, 1, 5, 9, 10, 5, 5, 5, 9, 6, 1, 16, 11, 13, 4, 19, 17, 3, 7, 14, 14, 18, 9, 16, 13]
w = [6, 12, 17, 17, 10, 12, 1, 5, 16, 8, 4, 11, 14, 13, 8, 9, 10, 15, 10, 8, 10, 1, 1, 14, 19, 12, 8, 4, 10, 19, 15, 11, 17, 5, 10, 19, 11, 9, 6, 11, 19, 1, 15, 16, 17, 15, 16, 10, 11, 9]
B = 40

# Run the knapsack algorithm
max_value = knapsack(v, w, B)
print("Maximum value:", max_value)
