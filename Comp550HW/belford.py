# Bellman-Ford algorithm implementation
def bellman_ford(G, s, n):
    # Step 1: Initialize distances from source to all other vertices as infinity
    inf = float('inf')
    d = [inf] * n
    d[s] = 0  # Distance to the source is 0

    # Step 2: Relax all edges |V| - 1 times
    for _ in range(n - 1):
        for u in range(n):
            for v, weight in G[u]:
                if d[u] != inf and d[u] + weight < d[v - 1]:  # Adjust v to be 0-based
                    d[v - 1] = d[u] + weight

    # Return the distance array after relaxation
    return d

# Input graph G and source s
G = [[[2, 53], [6, -66], [14, -84], [15, -52], [16, 70], [17, 83], [27, 76], [29, -87]], [[3, 78], [10, -72], [13, 96], [14, -81], [16, -60], [17, -99], [18, 95], [19, -82], [25, -54], [29, -56]], [[4, 91], [8, -58], [9, 63], [10, 95], [19, 58], [20, 61], [26, 89]], [[5, 69], [9, -89], [17, 87], [21, 66]], [[6, 90], [8, -52], [9, 78]], [[7, 84], [10, -96], [11, 51], [18, 83], [19, 73], [21, 51], [22, 56], [24, -51], [25, 90]], [[8, 73], [18, 57], [20, -63]], [[9, 83], [10, -96], [11, -93], [18, -86], [21, 76], [22, -93], [23, -58], [24, 95]], [[10, 98], [17, 72], [24, 82]], [[11, 73], [12, 97], [13, 96], [18, -50], [21, 61], [22, 63], [25, -56], [28, 87]], [[12, 89], [20, 50], [21, -92]], [[13, 98], [16, -66], [19, 60], [21, -59], [24, 84], [25, -63], [26, 91]], [[14, 66], [15, 91], [16, 91], [18, 90], [21, 82], [28, 74], [29, 72]], [[15, 79], [18, 58], [19, 90], [23, 98], [29, -75], [30, -67]], [[16, 96], [17, -94], [24, -84], [30, 80]], [[17, 55], [18, 74], [23, -98], [27, -84]], [[18, 70], [21, -71]], [[19, 99], [21, 54], [26, 99], [28, 53]], [[20, 89], [21, -89], [25, -94]], [[21, 87], [23, -61]], [[22, 59], [24, 91], [26, 54]], [[23, 53], [27, 83], [28, 81]], [[24, 65]], [[25, 75], [26, -82], [30, 63]], [[26, 61]], [[27, 75]], [[28, 56]], [[29, 98]], [[30, 67]], []]               # Node 4 has no outgoing edges

# Source node (index starts from 0 in Python, so s = 0 corresponds to node 1)
s = 0

# Number of nodes (4 in this case)
n = 30

# Run Bellman-Ford algorithm
distances = bellman_ford(G, s, n)

# Output the distances from the source node
print("Distances from source node 1:", distances)

