def solve_harvest_waterloo():
    print("=== Harvest Waterloo Solver ===")
    print("Enter the patch dimensions and layout:")
    
    R = int(input("Number of rows (R): "))
    C = int(input("Number of columns (C): "))
    
    print(f"\nNow enter {R} rows of the patch layout:")
    print("Use: S (small pumpkin), M (medium pumpkin), L (large pumpkin), * (hay bale)")
    
    grid = []
    for i in range(R):
        row = input(f"Row {i+1}: ").strip()
        grid.append(row)
    
    print("\nEnter the farmer's starting position:")
    A = int(input("Starting row (0-indexed): "))
    B = int(input("Starting column (0-indexed): "))
    
    pumpkin_values = {
        'S': 1,
        'M': 5, 
        'L': 10 
    }
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visited = [[False for _ in range(C)] for _ in range(R)]
    
    def dfs(row, col):
        if row < 0 or row >= R or col < 0 or col >= C:
            return 0
        
        if visited[row][col]:
            return 0
        
        if grid[row][col] == '*':
            return 0
        
        visited[row][col] = True
        
        current_value = 0
        if grid[row][col] in pumpkin_values:
            current_value = pumpkin_values[grid[row][col]]
        
        total_value = current_value
        for dr, dc in directions:
            total_value += dfs(row + dr, col + dc)
        
        return total_value
    
    print(f"\nCalculating harvest starting from position ({A}, {B})...")
    total_harvest_value = dfs(A, B)
    
    print(f"\n=== RESULT ===")
    print(f"Total value of harvested pumpkins: ${total_harvest_value}")
    
    return total_harvest_value

def run_example_1():
    print("=== RUNNING EXAMPLE 1 ===")
    print("This will simulate the first example from the problem.")
    print("Expected output: $37")
    print("\nExample input:")
    print("Rows: 6, Columns: 6")
    print("Grid:")
    example_grid = [
        "**LMLS",
        "S*LMMS",
        "S*SMSM",
        "******",
        "LLM*MS",
        "SSL*SS"
    ]
    for i, row in enumerate(example_grid):
        print(f"Row {i+1}: {row}")
    print("Starting position: Row 5 (0-indexed), Column 1")
    print("\nTo run this example, input the values above when prompted.\n")

def run_example_2():
    print("=== RUNNING EXAMPLE 2 ===")
    print("This will simulate the second example from the problem.")
    print("Expected output: $88")
    print("\nExample input:")
    print("Rows: 6, Columns: 6")
    print("Grid:")
    example_grid = [
        "**LMLS",
        "S*LMMS",
        "S*SMSM",
        "***SLL",
        "LLM*MS",
        "SSL*SS"
    ]
    for i, row in enumerate(example_grid):
        print(f"Row {i+1}: {row}")
    print("Starting position: Row 2 (0-indexed), Column 4")
    print("\nTo run this example, input the values above when prompted.\n")

def solve_harvest_waterloo_bfs():
    from collections import deque
    
    R = int(input())
    C = int(input())
    
    grid = []
    for i in range(R):
        row = input().strip()
        grid.append(row)
    
    A = int(input())
    B = int(input())
    
    pumpkin_values = {
        'S': 1, 
        'M': 5, 
        'L': 10  
    }
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([(A, B)])
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[A][B] = True
    
    total_value = 0
    
    while queue:
        row, col = queue.popleft()
        
        if grid[row][col] in pumpkin_values:
            total_value += pumpkin_values[grid[row][col]]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < R and 0 <= new_col < C:
                if not visited[new_row][new_col] and grid[new_row][new_col] != '*':
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
    
    return total_value

if __name__ == "__main__":
    result = solve_harvest_waterloo()
    print(result)
