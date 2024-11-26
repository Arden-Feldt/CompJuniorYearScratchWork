from itertools import combinations, product

def calculate_3sat_independent_set(A):
    # 1. Initialize sets for vertices and edges
    vertices = set()
    edges = set()
    
    # Track each clause and add vertices for each literal in the clause
    for clause in A:
        clause_vertices = []
        for literal in clause:
            # Use tuples to represent each vertex as (clause_index, literal)
            vertex = (A.index(clause), literal)
            clause_vertices.append(vertex)
            vertices.add(vertex)
        
        # Add edges to form a triangle within each clause (3 edges per clause)
        for v1, v2 in combinations(clause_vertices, 2):
            edges.add((v1, v2))
    
    # 2. Add conflict edges between complementary literals across different clauses
    literals = set(abs(literal) for clause in A for literal in clause)
    for literal in literals:
        pos_vertices = [v for v in vertices if v[1] == literal]      # x_i vertices
        neg_vertices = [v for v in vertices if v[1] == -literal]     # ¬x_i vertices
        for pos_v, neg_v in product(pos_vertices, neg_vertices):
            edges.add((pos_v, neg_v))

    # 3. Calculate number of vertices and edges
    num_vertices = len(vertices)
    num_edges = len(edges)
    k = len(A)  # Number of clauses is the value of k

    return num_vertices, num_edges, k

# Example usage
A =  [[9, 37, -49], [-31, 42, 25], [-25, 28, 39], [-47, -15, 38], [2, -42, -35], [-28, -47, -2], [36, 15, 23], [-19, -2, -27], [-12, 41, 47], [-47, 46, -33], [43, -13, 20], [-33, 26, -38], [26, -27, -43], [44, -48, 24], [11, -34, 26], [-20, 46, 40], [-33, -15, -1], [15, -26, 33], [-18, -43, 36], [-48, -33, 9], [-4, 31, -24], [32, -23, -27], [-40, -22, -30], [-36, -38, -12], [17, -3, 44], [49, -18, 16], [19, -5, 11], [18, -42, 46], [8, 2, 20], [-7, 17, -47], [2, -15, 26], [46, -33, -44], [41, -45, 34], [-44, 37, -21], [9, -14, 4], [20, 48, 11], [-3, -38, 14], [46, 40, 33], [-37, 44, -28], [25, 19, -33]]
vertices, edges, k = calculate_3sat_independent_set(A)
print(f"Number of vertices: {vertices}")
print(f"Number of edges: {edges}")
print(f"Value of k: {k}")

