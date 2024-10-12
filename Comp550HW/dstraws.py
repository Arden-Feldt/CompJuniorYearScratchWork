import heapq

def dijkstra(G, s, n):
    # Step 1: Initialize distances from the source node to all other nodes as infinity
    inf = float('inf')
    d = [inf] * n
    d[s] = 0  # Distance to the source is 0
    
    # Step 2: Use a priority queue to always expand the node with the smallest distance
    pq = [(0, s)]  # (distance, node)
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # If we pop a node with a distance larger than the current known distance, skip it
        if current_dist > d[u]:
            continue
        
        # Step 3: Relax all edges outgoing from u
        for v, weight in G[u]:
            v -= 1  # Adjust for 0-based indexing
            distance_through_u = d[u] + weight
            if distance_through_u < d[v]:
                d[v] = distance_through_u
                heapq.heappush(pq, (d[v], v))
    
    return d

# Input graph G and source s
G =  [[[2, 58], [27, 96]], [[3, 64], [7, 51], [9, 91], [16, 82], [17, 77], [19, 62]], [[4, 93], [23, 85], [26, 86], [28, 92], [30, 50]], [[3, 97], [5, 82]], [[6, 50], [15, 92]], [[7, 95], [11, 90], [22, 53], [26, 97]], [[4, 79], [8, 99], [27, 58]], [[2, 72], [3, 93], [9, 52], [12, 63], [20, 99], [21, 81]], [[10, 86]], [[1, 84], [2, 68], [11, 68]], [[8, 52], [12, 87]], [[5, 61], [13, 88], [17, 52], [23, 94]], [[12, 86], [14, 51]], [[8, 91], [15, 73], [28, 86]], [[2, 96], [12, 66], [16, 55], [17, 58], [18, 89], [23, 74], [24, 77], [26, 78], [28, 63]], [[17, 67]], [[2, 51], [6, 98], [18, 95]], [[4, 79], [7, 95], [8, 69], [16, 71], [19, 87], [20, 94]], [[1, 67], [20, 72]], [[5, 92], [21, 71], [30, 98]], [[8, 59], [22, 56], [25, 61]], [[14, 65], [23, 63], [24, 52]], [[19, 99], [24, 90]], [[11, 72], [16, 54], [22, 59], [25, 63]], [[3, 52], [26, 65], [29, 82]], [[1, 87], [11, 68], [27, 83]], [[1, 70], [21, 91], [28, 51]], [[2, 61], [4, 89], [29, 77]], [[2, 62], [6, 66], [18, 50], [27, 84], [30, 85]], [[3, 83], [11, 60]]]                # Node 3 has no outgoing edges

# Source node (index starts from 0 in Python, so s = 0 corresponds to node 1)
s = 0

# Number of nodes (3 in this case)
n = 30

# Run Dijkstra's algorithm
distances = dijkstra(G, s, n)

# Output the distance from the source node to node 2 (d[2])
i = 0
for x in distances:
    i = i + 1
    print("Final value of d[", str(i), "]:", x)

