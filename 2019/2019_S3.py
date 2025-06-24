def solve_arithmetic_square():
    print("Arithmetic Square Solver")
    print("========================")
    print("Enter a 3x3 grid where some values are known and others are 'X'")
    print("Each row and column must form an arithmetic sequence")
    print("Enter integers or 'X' for unknown values, separated by spaces")
    print("Example: '8 9 10' or '16 X 20'\n")
    
    grid = []
    for i in range(3):
        while True:
            try:
                print(f"Enter row {i+1} (3 values separated by spaces):")
                line = input().strip().split()
                if len(line) != 3:
                    print("Please enter exactly 3 values separated by spaces")
                    continue
                
                row = []
                for val in line:
                    if val.upper() == 'X':
                        row.append(None)
                    else:
                        num = int(val)
                        if abs(num) > 1000000:
                            print("Integer values must be between -1,000,000 and 1,000,000")
                            raise ValueError
                        row.append(num)
                grid.append(row)
                break
            except ValueError:
                print("Invalid input. Use integers or 'X' for unknown values")
                continue
    
    print("\nInput grid:")
    for i, row in enumerate(grid):
        display_row = []
        for val in row:
            if val is None:
                display_row.append('X')
            else:
                display_row.append(str(val))
        print(f"Row {i+1}: {' '.join(display_row)}")
    print()
    
    solution = [row[:] for row in grid]
    
    max_iterations = 20
    for iteration in range(max_iterations):
        changed = False
        

        for i in range(3):
            row = solution[i]
            none_count = sum(1 for x in row if x is None)
            
            if none_count == 1:
                if row[0] is None:
                    solution[i][0] = 2 * row[1] - row[2]
                    changed = True
                elif row[1] is None:
                    solution[i][1] = (row[0] + row[2]) // 2
                    changed = True
                elif row[2] is None:
                    solution[i][2] = 2 * row[1] - row[0]
                    changed = True
        
        for j in range(3):
            col = [solution[i][j] for i in range(3)]
            none_count = sum(1 for x in col if x is None)
            
            if none_count == 1:
                if col[0] is None:
                    solution[0][j] = 2 * col[1] - col[2]
                    changed = True
                elif col[1] is None:
                    solution[1][j] = (col[0] + col[2]) // 2
                    changed = True
                elif col[2] is None:
                    solution[2][j] = 2 * col[1] - col[0]
                    changed = True
        
        total_unknowns = sum(1 for i in range(3) for j in range(3) if solution[i][j] is None)
        
        if total_unknowns <= 3 and not changed:
            if solution[1][1] is None:
                known_positions = []
                for i in range(3):
                    for j in range(3):
                        if solution[i][j] is not None:
                            known_positions.append((i, j, solution[i][j]))
                
                if len(known_positions) >= 6:
                    corners = [(0,0), (0,2), (2,0), (2,2)]
                    known_corners = [(i,j) for i,j in corners if solution[i][j] is not None]
                    
                    if len(known_corners) >= 2:
                        if solution[1][0] is not None and solution[1][2] is not None:
                            solution[1][1] = (solution[1][0] + solution[1][2]) // 2
                            changed = True
                        elif solution[0][1] is not None and solution[2][1] is not None:
                            solution[1][1] = (solution[0][1] + solution[2][1]) // 2
                            changed = True
        
        if not changed:
            break
    
    remaining_unknowns = [(i,j) for i in range(3) for j in range(3) if solution[i][j] is None]
    
    if remaining_unknowns:

        if solution[1][1] is None:
            solution[1][1] = 0 
        
        for iteration in range(10):
            old_solution = [row[:] for row in solution]
            
            for i in range(3):
                row = solution[i]
                if row[1] is not None:
                    if row[0] is None and row[2] is not None:
                        solution[i][0] = 2 * row[1] - row[2]
                    elif row[2] is None and row[0] is not None:
                        solution[i][2] = 2 * row[1] - row[0]
            
            for j in range(3):
                col = [solution[i][j] for i in range(3)]
                if col[1] is not None:
                    if col[0] is None and col[2] is not None:
                        solution[0][j] = 2 * col[1] - col[2]
                    elif col[2] is None and col[0] is not None:
                        solution[2][j] = 2 * col[1] - col[0]
            
            if solution == old_solution:
                break
        
        for i, j in remaining_unknowns:
            if solution[i][j] is None:
                solution[i][j] = 0
    
    print("Solution:")
    print("=========")
    for i in range(3):
        print(f"Row {i+1}: {' '.join(map(str, solution[i]))}")
    
    print("\nVerification:")
    print("-------------")
    # Verify rows are arithmetic sequences
    for i in range(3):
        a, b, c = solution[i]
        diff1 = b - a
        diff2 = c - b
        if diff1 == diff2:
            print(f"Row {i+1}: {a}, {b}, {c} (difference: {diff1}) ✓")
        else:
            print(f"Row {i+1}: {a}, {b}, {c} - ERROR: not arithmetic!")
    
    # Verify columns are arithmetic sequences
    for j in range(3):
        a, b, c = solution[0][j], solution[1][j], solution[2][j]
        diff1 = b - a
        diff2 = c - b
        if diff1 == diff2:
            print(f"Col {j+1}: {a}, {b}, {c} (difference: {diff1}) ✓")
        else:
            print(f"Col {j+1}: {a}, {b}, {c} - ERROR: not arithmetic!")

if __name__ == "__main__":
    solve_arithmetic_square()
