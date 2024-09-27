def longest_increasing_subsequence(arr):
    n = len(arr)
    if n == 0:
        return [], [], [], []  # If the array is empty, return empty lists

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

    # Extract the first 3 elements of the LIS (if available)
    first_three_lis = lis[:3]

    return last_three_dp, last_three_lis, first_three_lis, lis


# Example usage:
A = [14, 84, 76, 26, 50, 45, 65, 79, 10, 3, 83, 43, 76, 1, 45, 72, 23, 94, 90, 4, 3, 54, 93, 38, 22, 42, 3, 22, 44, 50, 24, 23, 22, 46, 29, 3, 83, 56, 64, 19, 99, 86, 12, 33, 72, 71, 93, 42, 83, 67, 31, 59, 88, 84, 51, 59, 4, 25, 79, 42, 18, 55, 70, 67, 38, 44, 51, 78, 52, 39, 49, 3, 5, 70, 98, 59, 39, 17, 50, 98, 77, 54, 86, 23, 51, 95, 58, 46, 27, 55, 95, 1, 78, 82, 88, 74, 81, 52, 56, 43]
last_three_dp, last_three_lis, first_three_lis, full_lis = longest_increasing_subsequence(A)

print("Last three elements in dp:", last_three_dp)
print("Last three elements in LIS:", last_three_lis)
print("First three elements in LIS:", first_three_lis)
print("Full LIS found by the algorithm:", full_lis)

