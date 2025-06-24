def simulate_canvas():
    print("=" * 50)
    print("MODERN ART CANVAS SIMULATOR")
    print("=" * 50)
    print()
    print("INSTRUCTIONS:")
    print("1. Enter canvas dimensions (M rows, N columns)")
    print("2. Enter number of artist choices (K)")
    print("3. For each choice, enter either:")
    print("   - 'R [row_number]' to brush along a row")
    print("   - 'C [column_number]' to brush along a column")
    print("4. The program will count final gold cells")
    print()
    print("Example input:")
    print("M=3, N=3, K=2")
    print("Choice 1: R 1  (brush row 1)")
    print("Choice 2: C 1  (brush column 1)")
    print()
    
    try:
        print("Enter canvas dimensions:")
        M = int(input("Number of rows (M): "))
        N = int(input("Number of columns (N): "))
        
        if M <= 0 or N <= 0:
            print("Error: Canvas dimensions must be positive!")
            return
        
        K = int(input("Number of artist choices (K): "))
        
        if K < 0:
            print("Error: Number of choices cannot be negative!")
            return
        
        canvas = [[False for _ in range(N)] for _ in range(M)]
        
        print(f"\nStarting with {M}x{N} canvas (all black)")
        print("\nEnter artist choices:")
        
        for i in range(K):
            while True:
                try:
                    choice = input(f"Choice {i+1} (R [row] or C [col]): ").strip().split()
                    
                    if len(choice) != 2:
                        print("Error: Please enter exactly 2 values (e.g., 'R 1' or 'C 2')")
                        continue
                    
                    action = choice[0].upper()
                    position = int(choice[1])
                    
                    if action == 'R':
                        if position < 1 or position > M:
                            print(f"Error: Row must be between 1 and {M}")
                            continue
                        
                        row = position - 1
                        for col in range(N):
                            canvas[row][col] = not canvas[row][col]
                        
                        print(f"  Brushed row {position}")
                        break
                        
                    elif action == 'C':
                        if position < 1 or position > N:
                            print(f"Error: Column must be between 1 and {N}")
                            continue
                        
                        col = position - 1
                        for row in range(M):
                            canvas[row][col] = not canvas[row][col]
                        
                        print(f"  Brushed column {position}")
                        break
                        
                    else:
                        print("Error: Action must be 'R' for row or 'C' for column")
                        continue
                        
                except ValueError:
                    print("Error: Position must be a valid number")
                    continue
        
        gold_count = 0
        for row in range(M):
            for col in range(N):
                if canvas[row][col]:
                    gold_count += 1
        
        print("\n" + "=" * 30)
        print("FINAL CANVAS:")
        print("=" * 30)
        
        for row in range(M):
            row_str = ""
            for col in range(N):
                if canvas[row][col]:
                    row_str += "G" 
                else:
                    row_str += "B" 
            print(row_str)
        
        print(f"\nTotal gold cells: {gold_count}")
        print("=" * 30)
        
    except ValueError:
        print("Error: Please enter valid numbers for dimensions and choices")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def run_sample_tests():
    """Run the provided sample test cases"""
    print("RUNNING SAMPLE TESTS:")
    print("=" * 40)
    
    print("\nSample 1:")
    print("Canvas: 3x3")
    print("Choices: R 1, C 1")
    
    canvas = [[False, False, False],
              [False, False, False],
              [False, False, False]]
    
    for col in range(3):
        canvas[0][col] = not canvas[0][col]
    
    print("After R 1:")
    for row in canvas:
        print(''.join('G' if cell else 'B' for cell in row))
    
    for row in range(3):
        canvas[row][0] = not canvas[row][0]
    
    print("After C 1:")
    for row in canvas:
        print(''.join('G' if cell else 'B' for cell in row))
    
    gold_count = sum(sum(row) for row in canvas)
    print(f"Gold cells: {gold_count}")
    
    print("\nSample 2:")
    print("Canvas: 4x5")
    print("Choices: R 3, C 1, C 2, R 2, R 2, C 1, R 4")
    
    canvas = [[False for _ in range(5)] for _ in range(4)]
    choices = [('R', 3), ('C', 1), ('C', 2), ('R', 2), ('R', 2), ('C', 1), ('R', 4)]
    
    for action, pos in choices:
        if action == 'R':
            row = pos - 1
            for col in range(5):
                canvas[row][col] = not canvas[row][col]
        else:  
            col = pos - 1
            for row in range(4):
                canvas[row][col] = not canvas[row][col]
    
    print("Final canvas:")
    for row in canvas:
        print(''.join('G' if cell else 'B' for cell in row))
    
    gold_count = sum(sum(row) for row in canvas)
    print(f"Gold cells: {gold_count}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Run interactive simulator")
    print("2. Run sample tests")
    print("3. Both")
    
    try:
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            simulate_canvas()
        elif choice == "2":
            run_sample_tests()
        elif choice == "3":
            run_sample_tests()
            print("\n" + "=" * 60)
            simulate_canvas()
        else:
            print("Invalid choice. Running interactive simulator...")
            simulate_canvas()
            
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"Error: {e}")
        print("Running interactive simulator...")
        simulate_canvas()
