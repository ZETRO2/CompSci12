def solve_square_pool():
    print("Square Pool Solver")
    print("=" * 18)
    
    try:
        n = int(input("Enter grid size (N): "))
        if n < 2:
            print("Grid size must be at least 2")
            return None
        
        t = int(input("Enter number of trees (T): "))
        if t >= n * n:
            print("Too many trees for the grid")
            return None
        
        trees = set()
        print(f"\nEnter {t} tree positions (row col, 1-indexed):")
        for i in range(t):
            try:
                line = input(f"Tree {i+1}: ").strip()
                r, c = map(int, line.split())
                if 1 <= r <= n and 1 <= c <= n:
                    trees.add((r-1, c-1)) 
                else:
                    print(f"Invalid position ({r}, {c}). Must be between 1 and {n}")
                    return None
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")
                return None
        
        max_square_size = find_largest_square(n, trees)
        
        print(f"\nLargest square pool size: {max_square_size}")
        
        show_viz = input("\nShow grid visualization? (y/n): ").strip().lower()
        if show_viz in ['y', 'yes']:
            visualize_grid(n, trees, max_square_size)
        
        return max_square_size
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None
    except KeyboardInterrupt:
        print("\n\nExiting...")
        return None

def find_largest_square(n, trees):
    for size in range(n, 0, -1):
        for top_row in range(n - size + 1):
            for left_col in range(n - size + 1):
                contains_tree = False
                for r in range(top_row, top_row + size):
                    for c in range(left_col, left_col + size):
                        if (r, c) in trees:
                            contains_tree = True
                            break
                    if contains_tree:
                        break
                
                if not contains_tree:
                    return size
    
    return 0 

def visualize_grid(n, trees, max_size):
    print(f"\nGrid visualization ({n}x{n}):")
    print("T = Tree, . = Empty, # = Possible pool area")
    
    grid = [['.' for _ in range(n)] for _ in range(n)]
    
    for r, c in trees:
        grid[r][c] = 'T'
    
    square_found = False
    for top_row in range(n - max_size + 1):
        for left_col in range(n - max_size + 1):
            contains_tree = False
            for r in range(top_row, top_row + max_size):
                for c in range(left_col, left_col + max_size):
                    if (r, c) in trees:
                        contains_tree = True
                        break
                if contains_tree:
                    break
            
            if not contains_tree:
                for r in range(top_row, top_row + max_size):
                    for c in range(left_col, left_col + max_size):
                        if grid[r][c] == '.':
                            grid[r][c] = '#'
                square_found = True
                break
        if square_found:
            break
    
    print("\n   ", end="")
    for c in range(n):
        print(f"{c+1:2}", end="")
    print()
    
    for r in range(n):
        print(f"{r+1:2} ", end="")
        for c in range(n):
            print(f"{grid[r][c]:2}", end="")
        print()

def main():
    while True:
        result = solve_square_pool()
        
        if result is not None:
            print(f"\nFinal Answer: {result}")
        
        print("\n" + "="*50)
        again = input("Solve another problem? (y/n): ").strip().lower()
        if again not in ['y', 'yes']:
            print("Goodbye!")
            break
        print()

if __name__ == "__main__":
    main()
