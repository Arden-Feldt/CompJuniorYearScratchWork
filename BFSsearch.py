from collections import deque

def bfs_distance(graph, start_vertex):
    # Initialize distances to -1 (unvisited)
    num_vertices = len(graph)
    distances = [-1] * num_vertices
    # Distance to the start_vertex is 0
    distances[start_vertex] = 0
    
    # Create a queue for BFS and enqueue the start_vertex
    queue = deque([start_vertex])
    
    while queue:
        # Dequeue a vertex from the queue
        current_vertex = queue.popleft()
        
        # Visit all the neighbors of the current_vertex
        for neighbor in graph[current_vertex]:
            if 0 <= neighbor < num_vertices:  # Ensure neighbor is within bounds
                if distances[neighbor] == -1:  # If neighbor hasn't been visited
                    # Set the distance and enqueue the neighbor
                    distances[neighbor] = distances[current_vertex] + 1
                    queue.append(neighbor)
    
    return distances

# Example graph
G = [[41], [16, 21, 27, 32], [42, 53], [7, 11, 30, 41, 56], [29, 38, 47, 54, 55, 59], [10, 45], [11], [8, 23, 28, 36, 44], [9, 22, 24, 49, 54], [], [9, 23, 51], [12, 49], [11, 22, 50, 55], [25, 29, 37, 46], [27, 49, 56], [4, 7, 36, 46, 50, 55], [1, 6, 35, 45, 48], [2, 49], [], [16, 41, 58], [17, 27, 52], [4, 11, 32, 35, 40], [34, 55], [26, 46, 54], [6, 9, 32], [0, 8, 27, 46, 55, 57], [2, 31, 39], [25, 30, 33, 55], [22, 32], [21], [24, 28, 42], [32, 45], [3, 25, 58], [0, 9, 10, 13, 25, 31, 52], [23, 54], [29, 47, 54, 58], [0, 44], [34], [15, 17, 39, 48, 49, 56], [4, 56], [6, 16], [13, 18, 46, 50], [28, 43, 57], [44], [8, 22, 55], [26, 33, 46], [6, 24], [0, 1, 4, 6, 50], [24, 42, 53], [0, 31], [3, 40], [19, 40], [32], [2, 8, 21], [2, 20], [47], [16, 18, 19, 41, 44], [28, 32, 52, 53, 56], [10, 26, 47, 52, 57], [3, 24, 25, 33, 56]]
# Perform BFS and get distances from vertex 0
distances = bfs_distance(G, 0)

# Output distances
print("Distances from vertex 0:", distances)
