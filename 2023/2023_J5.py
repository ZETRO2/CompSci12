def solve_word_hunt():
    print("=== Word Hunt Solver ===")
    print("This program finds words in a grid that can appear in:")
    print("- Straight lines (horizontal, vertical, diagonal)")
    print("- L-shapes (two perpendicular segments sharing one letter)")
    print()
    
    print("Enter the word to search for:")
    word = input().strip().upper()
    
    print(f"\nEnter the number of rows in the grid:")
    R = int(input())
    
    print(f"Enter the number of columns in the grid:")
    C = int(input())
    
    print(f"\nEnter {R} rows of the grid.")
    print(f"Each row should contain {C} letters separated by spaces.")
    print("Example: A B C D E")
    print()
    
    grid = []
    for i in range(R):
        print(f"Row {i+1}:")
        row = input().strip().split()
        row = [letter.upper() for letter in row]
        grid.append(row)
    
    print(f"\nSearching for '{word}' in the grid...")
    print()
    
    print("Grid:")
    for i, row in enumerate(grid):
        print(f"  {' '.join(row)}")
    print()
    
    found_patterns = set()
    
    for r in range(R):
        for c in range(C):
            straight_patterns = find_straight_patterns(grid, word, r, c, R, C)
            for pattern in straight_patterns:
                found_patterns.add(pattern)
            
            l_patterns = find_l_patterns(grid, word, r, c, R, C)
            for pattern in l_patterns:
                found_patterns.add(pattern)
    
    count = len(found_patterns)
    print(f"Result: The word '{word}' appears {count} times in the grid.")
    
    if count > 0:
        print(f"\nFound patterns:")
        for i, pattern in enumerate(sorted(found_patterns), 1):
            pattern_type = pattern[0]
            if pattern_type == 'straight':
                path = pattern[1]
                print(f"{i}. Straight line: {path}")
            else: 
                path = pattern[1]
                print(f"{i}. L-shape: {path}")

def find_straight_patterns(grid, word, start_r, start_c, R, C):
    patterns = []
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for dr, dc in directions:
        if check_word_in_direction(grid, word, start_r, start_c, dr, dc, R, C):
            path = []
            for i in range(len(word)):
                r = start_r + i * dr
                c = start_c + i * dc
                path.append((r, c))
            
            pattern = ('straight', tuple(path))
            patterns.append(pattern)
    
    return patterns

def find_l_patterns(grid, word, start_r, start_c, R, C):
    patterns = []
    
    for split in range(1, len(word)):
        part1 = word[:split]
        part2 = word[split-1:] 
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for dr1, dc1 in directions:
            if not check_word_in_direction(grid, part1, start_r, start_c, dr1, dc1, R, C):
                continue
            
            bend_r = start_r + (len(part1) - 1) * dr1
            bend_c = start_c + (len(part1) - 1) * dc1
            
            for dr2, dc2 in directions:
                if dr1 * dr2 + dc1 * dc2 != 0:
                    continue
                
                if check_word_in_direction(grid, part2, bend_r, bend_c, dr2, dc2, R, C):
                    path = []
                    
                    for k in range(len(part1)):
                        r = start_r + k * dr1
                        c = start_c + k * dc1
                        path.append((r, c))
                    
                    for k in range(1, len(part2)):
                        r = bend_r + k * dr2
                        c = bend_c + k * dc2
                        path.append((r, c))
                    
                    if is_straight_line(path):
                        continue
                    
                    pattern_key = ('L', tuple(sorted(path)), split, tuple(sorted([(dr1, dc1), (dr2, dc2)])))
                    patterns.append(pattern_key)
    
    return patterns

def is_straight_line(path):
    if len(path) < 3:
        return True
    
    dr = path[1][0] - path[0][0]
    dc = path[1][1] - path[0][1]
    
    for i in range(2, len(path)):
        expected_r = path[0][0] + i * dr
        expected_c = path[0][1] + i * dc
        if path[i] != (expected_r, expected_c):
            return False
    
    return True

def check_word_in_direction(grid, word, start_r, start_c, dr, dc, R, C):
    for i in range(len(word)):
        r = start_r + i * dr
        c = start_c + i * dc
        
        if r < 0 or r >= R or c < 0 or c >= C:
            return False
        
        if grid[r][c] != word[i]:
            return False
    
    return True

if __name__ == "__main__":
    solve_word_hunt()
