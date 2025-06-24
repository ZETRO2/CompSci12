def solve_trianglane():
    print("=== Trianglane Problem Solver ===")
    print("Instructions:")
    print("1. Enter the number of columns (C)")
    print("2. Enter the first row: C integers separated by spaces (1=wet/black, 0=dry/white)")
    print("3. Enter the second row: C integers separated by spaces (1=wet/black, 0=dry/white)")
    print()
    
    C = int(input("Number of columns: "))
    print("First row (upward triangles):")
    row1 = list(map(int, input().split()))
    print("Second row (downward triangles):")
    row2 = list(map(int, input().split()))
    
    def get_neighbors(row, col):
        neighbors = []
        
        if row == 0:
            if col > 0:
                neighbors.append((0, col - 1))
            if col < C - 1:
                neighbors.append((0, col + 1))
  
            if col < C:
                neighbors.append((1, col))
        
        else: 
            if col > 0:
                neighbors.append((1, col - 1))
            if col < C - 1:
                neighbors.append((1, col + 1))
            neighbors.append((0, col))
        
        return [(r, c) for r, c in neighbors if 0 <= r <= 1 and 0 <= c < C]
    
    wet_tiles = set()
    for col in range(C):
        if row1[col] == 1:
            wet_tiles.add((0, col))
        if row2[col] == 1:
            wet_tiles.add((1, col))
    
    total_perimeter = 0
    
    for row, col in wet_tiles:
        neighbors = get_neighbors(row, col)
        
        wet_neighbor_count = 0
        for nr, nc in neighbors:
            if (nr, nc) in wet_tiles:
                wet_neighbor_count += 1
        
        contribution = 3 - wet_neighbor_count
        total_perimeter += contribution
    
    return total_perimeter

print("Running Trianglane Solution...")
result = solve_trianglane()
print(f"\nAnswer: {result} metres of warning tape needed")
print("\nExplanation: Each wet tile contributes its unshared edges to the perimeter.")
print("Each triangular tile has 3 edges of 1 metre each.")
