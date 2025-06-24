def solve_heavy_light_composition():
    print("=== Heavy-Light Composition Problem Solver ===")
    print("A letter is 'heavy' if it appears more than once in the string, 'light' otherwise.")
    print("Determine if letters alternate between heavy and light in each string.\n")
    
    T, N = map(int, input("Enter T (number of strings) and N (length of each string): ").split())
    
    print(f"\nEnter {T} strings of length {N}:")
    
    results = []
    
    for i in range(T):
        string = input(f"String {i+1}: ").strip()
        
        char_count = {}
        for char in string:
            char_count[char] = char_count.get(char, 0) + 1
        
        char_types = []
        for char in string:
            if char_count[char] > 1:
                char_types.append("heavy")
            else:
                char_types.append("light")
        
        is_alternating = True
        if len(char_types) > 1:
            for j in range(1, len(char_types)):
                if char_types[j] == char_types[j-1]:
                    is_alternating = False
                    break
        
        print(f"\nAnalysis for '{string}':")
        print("Character frequencies:", char_count)
        print("Pattern:", " → ".join(char_types))
        
        if is_alternating:
            print("Result: T (alternating)")
            results.append("T")
        else:
            print("Result: F (not alternating)")
            results.append("F")
        
        print("-" * 40)
    
    print("\n=== FINAL RESULTS ===")
    for i, result in enumerate(results):
        print(f"String {i+1}: {result}")
    
    return results

def run_example():
    print("=== RUNNING EXAMPLE ===")
    print("Input:")
    print("T = 3, N = 4")
    print("Strings: ['abcb', 'bcbb', 'babc']")
    print("Expected output: ['T', 'F', 'T']")
    print("\nDetailed analysis:")
    
    strings = ["abcb", "bcbb", "babc"]
    
    for i, string in enumerate(strings):
        print(f"\nString {i+1}: '{string}'")
        
        char_count = {}
        for char in string:
            char_count[char] = char_count.get(char, 0) + 1
        
        print(f"Character frequencies: {char_count}")
        
        pattern = []
        for char in string:
            if char_count[char] > 1:
                pattern.append("heavy")
            else:
                pattern.append("light")
        
        print(f"Pattern: {' → '.join(pattern)}")
        
        is_alternating = True
        if len(pattern) > 1:
            for j in range(1, len(pattern)):
                if pattern[j] == pattern[j-1]:
                    is_alternating = False
                    break
        
        result = "T" if is_alternating else "F"
        print(f"Result: {result}")
        print("-" * 30)

def solve_with_input(strings):
    results = []
    
    for i, string in enumerate(strings):
        print(f"String {i+1}: '{string}'")
        char_count = {}
        for char in string:
            char_count[char] = char_count.get(char, 0) + 1
        
        char_types = []
        for char in string:
            if char_count[char] > 1:
                char_types.append("heavy")
            else:
                char_types.append("light")
        
        is_alternating = True
        if len(char_types) > 1:
            for j in range(1, len(char_types)):
                if char_types[j] == char_types[j-1]:
                    is_alternating = False
                    break
        
        result = "T" if is_alternating else "F"
        
        print(f"  Frequencies: {char_count}")
        print(f"  Pattern: {' → '.join(char_types)}")
        print(f"  Result: {result}")
        
        results.append(result)
    
    return results

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Solve your own Heavy-Light Composition problem")
    print("2. View and run the provided example")
    print("3. Quick test with example strings")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == "1":
        solve_heavy_light_composition()
    elif choice == "2":
        run_example()
    elif choice == "3":
        print("Quick test:")
        test_strings = ["abcb", "bcbb", "babc"]
        results = solve_with_input(test_strings)
        print(f"\nFinal results: {results}")
    else:
        print("Invalid choice. Running the solver...")
        solve_heavy_light_composition()
