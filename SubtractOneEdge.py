G = [[[2, 3], [3, 3]], [[1, 2], [3, 4], [4, 1]], [[1, 3], [2, 4], [4, 5]], [[2, 1], [3, 5]]]

# Subtract 1 from each value
G_subtracted = [[[v - 1, w - 1] for v, w in sublist] for sublist in G]

print(G_subtracted)