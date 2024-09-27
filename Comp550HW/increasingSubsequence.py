def longest_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return [], []  # If the array is empty, return empty lists

    # Initialize the DP array with 1s (each element is a subsequence of length 1)
    dp = [1] * n
    prev = [-1] * n  # To store the previous element index in the LIS

    # Fill the DP array according to the LIS recurrence relation
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j  # Store the previous index for reconstruction

    # Find the index of the maximum value in the dp array (first occurrence)
    max_value = max(dp)
    max_index = dp.index(max_value)

    # Reconstruct the LIS by tracing back the prev array
    lis = []
    current_index = max_index
    while current_index != -1:
        lis.append(arr[current_index])
        current_index = prev[current_index]

    # The LIS is constructed in reverse, so we reverse it at the end
    lis.reverse()

    # Extract the last 3 elements of both dp and LIS
    last_three_dp = dp[-3:]  # Last 3 elements of the dp array
    last_three_lis = lis[-3:]  # Last 3 elements of the LIS

    return last_three_dp, last_three_lis


# Example usage:
A = [6, 7, 8, 1, 2, 3]
last_three_dp, last_three_lis = longest_increasing_subsequence(A)

print("Last three elements in dp:", last_three_dp)
print("Last three elements in LIS:", last_three_lis)
