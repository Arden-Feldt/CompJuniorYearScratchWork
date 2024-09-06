class DFSWithBackEdges:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.visited = [False] * self.n
        self.pre = [-1] * self.n
        self.post = [-1] * self.n
        self.clock = 1
        self.back_edges = 0

    def dfs(self, vertex):
        # Mark the vertex as visited and assign the pre-order number
        self.visited[vertex] = True
        self.pre[vertex] = self.clock
        self.clock += 1
        
        # Explore all neighbors of the vertex
        for neighbor in self.graph[vertex]:
            if not self.visited[neighbor]:
                self.dfs(neighbor)
            elif self.pre[neighbor] != -1 and self.post[neighbor] == -1:
                # Back edge found: neighbor has been visited, but its post-order number hasn't been assigned
                self.back_edges += 1
        
        # Assign the post-order number
        self.post[vertex] = self.clock
        self.clock += 1

    def run_dfs(self):
        # Run DFS for every vertex that hasn't been visited
        for vertex in range(self.n):
            if not self.visited[vertex]:
                self.dfs(vertex)
        return self.pre, self.post, self.back_edges

# Test with the second graph
G2 = [[18, 19, 23], [2, 8, 36], [1, 8, 13], [29], [3, 15, 20, 28, 32], [8, 12, 18, 23, 28, 38], [17, 19, 31, 38], [0, 1, 10, 16, 17, 18, 22, 32, 36], [2, 25, 28, 33, 35, 37], [0, 2, 14], [11, 12, 30, 31], [6, 10, 12, 19, 20, 27, 28], [13, 26, 28], [14, 19, 32], [2, 26], [14, 19, 28, 30], [17, 36, 37], [4, 9, 19, 35, 39], [17, 20, 28], [16, 22, 27], [7, 11, 13, 14, 15, 17, 18, 24, 29, 33, 39], [23, 26, 30, 34], [16, 24, 32, 35], [0, 1, 3, 4, 24, 34, 38], [3, 9, 13, 14, 33, 38], [3, 6, 13, 15, 16, 31], [13, 38], [18, 25], [0, 26], [6, 7, 16, 31, 32], [3, 8, 21, 27, 29, 37], [9, 22, 24, 29, 35, 36], [1, 2, 8, 22, 25, 30], [], [5, 26, 36], [0, 14, 17, 30, 31, 38], [6, 9, 14, 18, 21, 26, 28, 30], [4, 10, 26, 32], [1, 7, 19, 23, 39], [8, 10, 13, 15, 35]]
dfs2 = DFSWithBackEdges(G2)
pre2, post2, back_edges2 = dfs2.run_dfs()

print("Graph 2:")
print("Pre-order:", pre2)
print("Post-order:", post2)
print("Number of back edges:", back_edges2)
