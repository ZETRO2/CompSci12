def solve_hat_circle():
    print("=== Hat Circle Problem Solver ===")
    print("People sit around a circular table and look at the person directly across from them.")
    print("Count how many people see someone with the same hat number as their own.\n")
    
    N = int(input("Enter the number of people (must be even): "))
    
    if N % 2 != 0:
        print("Error: Number of people must be even!")
        return
    
    print(f"\nEnter the hat numbers for each person (seats 1 to {N}):")
    
    hat_numbers = []
    for i in range(N):
        hat_num = int(input(f"Hat number for person in seat {i+1}: "))
        hat_numbers.append(hat_num)
    
    matches = 0
    
    print(f"\nAnalyzing who sees whom:")
    
    for i in range(N):
        opposite_seat = (i + N // 2) % N
        
        person_seat = i + 1  
        opposite_person_seat = opposite_seat + 1 
        
        person_hat = hat_numbers[i]
        opposite_hat = hat_numbers[opposite_seat]
        
        print(f"Person in seat {person_seat} (hat {person_hat}) looks at person in seat {opposite_person_seat} (hat {opposite_hat})", end="")
        
        if person_hat == opposite_hat:
            matches += 1
            print(" -> MATCH! ✓")
        else:
            print(" -> No match")
    
    print(f"\n=== RESULT ===")
    print(f"Number of people who see someone with the same hat number: {matches}")
    
    return matches

def run_example_1():
    print("=== EXAMPLE 1 ===")
    print("Input:")
    print("N = 4")
    print("Hat numbers: [0, 1, 0, 1]")
    print("Expected output: 4")
    print("\nExplanation:")
    print("- Person 1 (hat 0) looks at person 3 (hat 0) -> Match")
    print("- Person 2 (hat 1) looks at person 4 (hat 1) -> Match") 
    print("- Person 3 (hat 0) looks at person 1 (hat 0) -> Match")
    print("- Person 4 (hat 1) looks at person 2 (hat 1) -> Match")
    print("Total matches: 4\n")

def run_example_2():
    print("=== EXAMPLE 2 ===")
    print("Input:")
    print("N = 4") 
    print("Hat numbers: [1, 1, 0, 0]")
    print("Expected output: 0")
    print("\nExplanation:")
    print("- Person 1 (hat 1) looks at person 3 (hat 0) -> No match")
    print("- Person 2 (hat 1) looks at person 4 (hat 0) -> No match")
    print("- Person 3 (hat 0) looks at person 1 (hat 1) -> No match") 
    print("- Person 4 (hat 0) looks at person 2 (hat 1) -> No match")
    print("Total matches: 0\n")

def solve_with_input(N, hat_numbers):
    """Helper function to solve with given input (for testing examples)"""
    matches = 0
    
    print(f"Solving for N={N}, hat numbers={hat_numbers}")
    print("Analysis:")
    
    for i in range(N):
        opposite_seat = (i + N // 2) % N
        person_seat = i + 1
        opposite_person_seat = opposite_seat + 1
        person_hat = hat_numbers[i]
        opposite_hat = hat_numbers[opposite_seat]
        
        print(f"Person {person_seat} (hat {person_hat}) looks at person {opposite_person_seat} (hat {opposite_hat})", end="")
        
        if person_hat == opposite_hat:
            matches += 1
            print(" -> MATCH!")
        else:
            print(" -> No match")
    
    print(f"Result: {matches} matches\n")
    return matches

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Solve your own Hat Circle problem")
    print("2. View and run Example 1")
    print("3. View and run Example 2") 
    print("4. Run both examples")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        solve_hat_circle()
    elif choice == "2":
        run_example_1()
        print("Running Example 1:")
        solve_with_input(4, [0, 1, 0, 1])
    elif choice == "3":
        run_example_2()
        print("Running Example 2:")
        solve_with_input(4, [1, 1, 0, 0])
    elif choice == "4":
        run_example_1()
        solve_with_input(4, [0, 1, 0, 1])
        run_example_2()
        solve_with_input(4, [1, 1, 0, 0])
    else:
        print("Invalid choice. Running the solver...")
        solve_hat_circle()
