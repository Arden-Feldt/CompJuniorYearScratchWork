def fractional_knapsack(v, w, B):
    n = len(v)
    
    # Compute value-to-weight ratios and store them along with index
    items = [(v[i] / w[i], v[i], w[i], i) for i in range(n)]
    
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)

    total_value = 0
    remaining_capacity = B
    fractions = [0] * n  # To track fractions of items selected

    # Greedily pick items
    for ratio, value, weight, i in items:
        if remaining_capacity >= weight:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
            fractions[i] = 1
        else:
            # Take fraction of the item
            fraction = remaining_capacity / weight
            total_value += fraction * value
            fractions[i] = fraction
            break  # Since the knapsack is now full

    return total_value, fractions

# Example instance
v = [64, 111, 58, 168, 98, 192, 142, 129, 214, 205, 240, 243, 127, 190, 150, 216, 221, 242, 242, 123, 215, 237, 113, 93, 202, 187, 71]
w = [1, 2, 2, 23, 10, 38, 16, 24, 8, 18, 31, 59, 14, 27, 46, 21, 64, 49, 35, 40, 37, 11, 3, 10, 14, 44, 5]
B = 31

# Run the fractional knapsack algorithm
optimal_value, fractions = fractional_knapsack(v, w, B)

# Print the results
print(f"Optimal value: {optimal_value:.2f}")
print("Fractions of items taken:", fractions)
