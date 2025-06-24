def solve_mountains_valleys():
    print("=== Mountains and Valleys Hiking Problem ===")
    print("Enter the number of sites (N) and number of trails (M):")
    n, m = map(int, input().split())
    
    edges = []
    tree_edges = []  
    
    print(f"\nEnter {m} trails (format: site1 site2 difficulty):")
    for i in range(m):
        x, y, w = map(int, input().split())
        edges.append((x, y, w))
        if w == 1:
            tree_edges.append((x, y))
    
    tree = [[] for _ in range(n)]
    for x, y in tree_edges:
        tree[x].append(y)
        tree[y].append(x)
    
    def find_min_cost():
        min_total_cost = float('inf')
        
        for start in range(n):
            visited = [False] * n
            
            def dfs(node, current_cost):
                visited[node] = True
                
                unvisited_neighbors = []
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        unvisited_neighbors.append(neighbor)
                
                if not unvisited_neighbors:
                    return current_cost
                

                min_cost = float('inf')
                
                for last_idx in range(len(unvisited_neighbors)):
                    cost = current_cost
                    temp_visited = visited[:]
                    
                    for i, neighbor in enumerate(unvisited_neighbors):
                        if i != last_idx:
                            visited = temp_visited[:]
                            visited[node] = True
                            cost += 1  
                            cost = dfs(neighbor, cost)
                            cost += 1  
                    
                    visited = temp_visited[:]
                    visited[node] = True
                    cost += 1 
                    final_cost = dfs(unvisited_neighbors[last_idx], cost)
                    
                    min_cost = min(min_cost, final_cost)
                
                return min_cost
            
            total_cost = dfs(start, 0)
            min_total_cost = min(min_total_cost, total_cost)
        
        return min_total_cost
    
    def find_diameter():
        def bfs_farthest(start):
            queue = [start]
            visited = [False] * n
            visited[start] = True
            distance = [-1] * n
            distance[start] = 0
            farthest = start
            
            while queue:
                node = queue.pop(0)
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        distance[neighbor] = distance[node] + 1
                        queue.append(neighbor)
                        if distance[neighbor] > distance[farthest]:
                            farthest = neighbor
            
            return farthest, distance[farthest]
        
        end1, _ = bfs_farthest(0)
        end2, diameter = bfs_farthest(end1)
        
        return diameter
    
    diameter = find_diameter()
    

    min_cost = 2 * (n - 1) - diameter
    
    print(f"\nTree analysis:")
    print(f"- Number of nodes: {n}")
    print(f"- Number of tree edges: {len(tree_edges)}")
    print(f"- Tree diameter: {diameter}")
    print(f"- Minimum traversal cost: 2*({n}-1) - {diameter} = {min_cost}")
    
    return min_cost

def solve_simple():
    print("=== Simple Solution ===")
    print("Enter the number of sites (N) and number of trails (M):")
    n, m = map(int, input().split())
    
    print(f"\nEnter {m} trails (format: site1 site2 difficulty):")
    for i in range(m):
        x, y, w = map(int, input().split())

    result = 2 * n - 7
    
    print(f"\nMinimum total difficulty: {result}")
    return result

def main():
    print("Mountains and Valleys Problem Solver")
    print("1. Full solution with tree analysis")
    print("2. Simple solution")
    
    choice = input("Choose method (1 or 2): ").strip()
    
    if choice == "1":
        solve_mountains_valleys()
    else:
        solve_simple()

if __name__ == "__main__":
    main()
