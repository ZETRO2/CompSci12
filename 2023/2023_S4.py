def solve_minimum_cost_roads():
    print("=== Minimum Cost Roads Problem Solver ===")
    print("This program finds the minimum cost subset of roads that maintains")
    print("connectivity while respecting distance constraints between intersections.")
    print()
    
    print("Enter the number of intersections (N) and roads (M), separated by space:")
    print("Example: 5 7")
    line = input("N M: ").split()
    N, M = int(line[0]), int(line[1])
    
    print(f"\nNow enter {M} roads, each on a new line.")
    print("Format: u v length cost")
    print("Where:")
    print("  u, v = intersection numbers (1 to N)")
    print("  length = road length in meters") 
    print("  cost = maintenance cost per year")
    print()
    
    roads = []
    original_graph = {}
    
    for i in range(M):
        print(f"Road {i+1}/{M}:")
        line = input("u v length cost: ").split()
        u, v, length, cost = int(line[0]), int(line[1]), int(line[2]), int(line[3])
        roads.append((u, v, length, cost))
        
        if u not in original_graph:
            original_graph[u] = []
        if v not in original_graph:
            original_graph[v] = []
        original_graph[u].append((v, length))
        original_graph[v].append((u, length))
    
    print("\nProcessing... Finding shortest distances in original graph...")
    
    def get_all_shortest_distances():
        dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            dist[i][i] = 0
        
        for u, v, length, cost in roads:
            dist[u][v] = min(dist[u][v], length)
            dist[v][u] = min(dist[v][u], length)
        
        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        return dist
    
    original_distances = get_all_shortest_distances()
    
    print("Original shortest distances calculated.")
    print("Searching for optimal road subset...")
    
    def is_valid_subset(road_indices):
        if not road_indices:
            return False
            
        graph = {i: [] for i in range(1, N + 1)}
        for idx in road_indices:
            u, v, length, cost = roads[idx]
            graph[u].append((v, length))
            graph[v].append((u, length))
        
        dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            dist[i][i] = 0
            
        for idx in road_indices:
            u, v, length, cost = roads[idx]
            dist[u][v] = min(dist[u][v], length)
            dist[v][u] = min(dist[v][u], length)
        
        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                if original_distances[i][j] != float('inf'):
                    if dist[i][j] > original_distances[i][j]:
                        return False
        
        return True
    
    min_cost = float('inf')
    best_roads = []
    total_combinations = 1 << M
    
    print(f"Testing {total_combinations - 1} possible combinations...")
    
    for mask in range(1, total_combinations):
        road_indices = []
        total_cost = 0
        
        for i in range(M):
            if mask & (1 << i):
                road_indices.append(i)
                total_cost += roads[i][3] 
        
        if is_valid_subset(road_indices):
            if total_cost < min_cost:
                min_cost = total_cost
                best_roads = road_indices[:]
        
        if mask % max(1, total_combinations // 10) == 0:
            progress = (mask * 100) // total_combinations
            print(f"Progress: {progress}%")
    
    print("\n" + "="*50)
    print("RESULTS:")
    print("="*50)
    
    if min_cost == float('inf'):
        print("No valid solution found!")
        print("This means no subset of roads can maintain the required distance constraints.")
        return None
    
    print(f"Minimum cost: {min_cost}")
    print(f"Number of roads in optimal plan: {len(best_roads)}")
    print("\nOptimal road plan details:")
    print("-" * 40)
    
    for i, idx in enumerate(best_roads, 1):
        u, v, length, cost = roads[idx]
        print(f"{i}. Road {idx+1}: Intersection {u} ↔ {v}")
        print(f"   Length: {length} meters, Cost: {cost} per year")
    
    print("-" * 40)
    print(f"Total annual maintenance cost: {min_cost}")
    
    unselected = [i for i in range(M) if i not in best_roads]
    if unselected:
        print(f"\nRoads NOT included in optimal plan:")
        for idx in unselected:
            u, v, length, cost = roads[idx]
            print(f"  Road {idx+1}: {u}↔{v} (length={length}, cost={cost})")
    
    return min_cost

def run_sample_test():
    print("=== SAMPLE TEST MODE ===")
    print("Running with the provided sample input...")
    print()
    
    sample_roads = [
        (1, 2, 15, 1),
        (2, 4, 9, 9), 
        (5, 2, 5, 6),
        (4, 5, 4, 4),
        (4, 3, 3, 7),
        (1, 3, 2, 7),
        (1, 4, 2, 1)
    ]
    
    N, M = 5, 7
    
    dist = [[float('inf')] * 6 for _ in range(6)]
    for i in range(1, 6):
        dist[i][i] = 0
    
    for u, v, length, cost in sample_roads:
        dist[u][v] = min(dist[u][v], length)
        dist[v][u] = min(dist[v][u], length)
    
    for k in range(1, 6):
        for i in range(1, 6):
            for j in range(1, 6):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    def is_valid_subset(road_indices):
        if not road_indices:
            return False
            
        graph_dist = [[float('inf')] * 6 for _ in range(6)]
        for i in range(1, 6):
            graph_dist[i][i] = 0
            
        for idx in road_indices:
            u, v, length, cost = sample_roads[idx]
            graph_dist[u][v] = min(graph_dist[u][v], length)
            graph_dist[v][u] = min(graph_dist[v][u], length)
        
        for k in range(1, 6):
            for i in range(1, 6):
                for j in range(1, 6):
                    if graph_dist[i][k] + graph_dist[k][j] < graph_dist[i][j]:
                        graph_dist[i][j] = graph_dist[i][k] + graph_dist[k][j]
        
        for i in range(1, 6):
            for j in range(i + 1, 6):
                if dist[i][j] != float('inf'):
                    if graph_dist[i][j] > dist[i][j]:
                        return False
        return True
    
    min_cost = float('inf')
    best_roads = []
    
    for mask in range(1, 1 << 7):
        road_indices = []
        total_cost = 0
        
        for i in range(7):
            if mask & (1 << i):
                road_indices.append(i)
                total_cost += sample_roads[i][3]
        
        if is_valid_subset(road_indices):
            if total_cost < min_cost:
                min_cost = total_cost
                best_roads = road_indices
    
    print(f"Sample result: {min_cost} (expected: 25)")
    print("Sample test completed!\n")
    
    return min_cost == 25

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Solve with manual input")
    print("2. Run sample test")
    print("3. Both (test first, then manual input)")
    
    choice = input("Enter choice (1, 2, or 3): ").strip()
    
    if choice == "2":
        run_sample_test()
    elif choice == "3":
        if run_sample_test():
            print("✓ Sample test PASSED! Algorithm is working correctly.")
        else:
            print("✗ Sample test FAILED! There might be an issue with the algorithm.")
        print("\nNow proceeding to manual input mode...\n")
        solve_minimum_cost_roads()
    else:
        solve_minimum_cost_roads()
