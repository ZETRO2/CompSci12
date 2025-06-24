def solve_bad_codes():
    
    print("=== BAD CODES PROBLEM SOLVER ===")
    print("This program checks if your binary code system has ambiguous sequences.")
    print("An ambiguous sequence can be decoded in multiple ways.\n")
    
    print("First, tell me about your code system:")
    try:
        n = int(input("How many different symbols do you have? (1-50): "))
        if n < 1 or n > 50:
            print("Error: Number of symbols must be between 1 and 50")
            return
        
        m = int(input("What's the maximum number of bits per symbol? (1-50): "))
        if m < 1 or m > 50:
            print("Error: Maximum bits must be between 1 and 50")
            return
            
    except ValueError:
        print("Error: Please enter valid numbers")
        return
    
    print(f"\nGreat! Now enter the binary code for each of your {n} symbols:")
    print("(Each code should only contain 0s and 1s, with at most {} bits)".format(m))
    
    codes = []
    for i in range(n):
        while True:
            try:
                print(f"Symbol {i+1}: ", end="")
                code = input().strip()
                
                if not code:
                    print("Error: Code cannot be empty. Try again.")
                    continue
                    
                if len(code) > m:
                    print(f"Error: Code is too long (max {m} bits). Try again.")
                    continue
                    
                if not all(c in '01' for c in code):
                    print("Error: Code must only contain 0s and 1s. Try again.")
                    continue
                    
                codes.append(code)
                break
                
            except KeyboardInterrupt:
                print("\nProgram interrupted by user.")
                return
    
    print(f"\nYour code system:")
    for i, code in enumerate(codes):
        print(f"  Symbol {i+1}: {code}")
    
    print("\nAnalyzing your code system...")
    
    def count_decodings(binary_seq, codes):
        """Count the number of ways to decode a binary sequence using the given codes"""
        memo = {}
        
        def dp(pos):
            if pos == len(binary_seq):
                return 1
            
            if pos in memo:
                return memo[pos]
            
            count = 0
            for code in codes:
                if pos + len(code) <= len(binary_seq):
                    if binary_seq[pos:pos + len(code)] == code:
                        count += dp(pos + len(code))
            
            memo[pos] = count
            return count
        
        return dp(0)
    
    max_reasonable_length = min(20, n * m)  
    
    print("Checking for ambiguous sequences...")
    
    for length in range(1, max_reasonable_length + 1):
        print(f"  Checking sequences of length {length}...", end="", flush=True)
        
        found_ambiguous = False
        ambiguous_example = ""
        example_decodings = []
        
        for i in range(2 ** length):
            binary_seq = format(i, f'0{length}b')
            
            ways = count_decodings(binary_seq, codes)
            
            if ways >= 2:
                found_ambiguous = True
                ambiguous_example = binary_seq
                
                def find_all_decodings(seq, pos=0, current_decoding=[]):
                    if pos == len(seq):
                        return [current_decoding[:]]
                    
                    all_decodings = []
                    for j, code in enumerate(codes):
                        if pos + len(code) <= len(seq):
                            if seq[pos:pos + len(code)] == code:
                                current_decoding.append(f"Symbol{j+1}({code})")
                                all_decodings.extend(find_all_decodings(seq, pos + len(code), current_decoding))
                                current_decoding.pop()
                    
                    return all_decodings
                
                example_decodings = find_all_decodings(binary_seq)[:5]  
                break
        
        if found_ambiguous:
            print(f" FOUND!")
            print(f"\n🚨 RESULT: Your code system IS ambiguous!")
            print(f"📏 Shortest ambiguous sequence length: {length}")
            print(f"📋 Example ambiguous sequence: '{ambiguous_example}'")
            print(f"🔍 This sequence can be decoded as:")
            for idx, decoding in enumerate(example_decodings[:3], 1):
                decoded_str = " + ".join(decoding)
                print(f"     {idx}. {decoded_str}")
            if len(example_decodings) > 3:
                print(f"     ... and {len(example_decodings) - 3} more ways")
            return length
        else:
            print(" OK")
    
    print(f"\n✅ RESULT: Your code system is NOT ambiguous! -1" )
    print("🎉 Every binary sequence can be decoded in only one way (or not at all).")
    print("Your code system is safe to use for secret messages!")
    return -1

def run_examples():
    """Show some examples of how the program works"""
    print("=== EXAMPLE DEMONSTRATIONS ===\n")
    
    def solve_example(name, n, m, codes, expected):
        print(f"Example {name}:")
        print(f"  Number of symbols: {n}")
        print(f"  Max bits per symbol: {m}")
        print("  Code system:")
        for i, code in enumerate(codes):
            print(f"    Symbol {i+1}: {code}")
        
        def count_decodings(binary_seq, codes):
            memo = {}
            def dp(pos):
                if pos == len(binary_seq):
                    return 1
                if pos in memo:
                    return memo[pos]
                count = 0
                for code in codes:
                    if pos + len(code) <= len(binary_seq):
                        if binary_seq[pos:pos + len(code)] == code:
                            count += dp(pos + len(code))
                memo[pos] = count
                return count
            return dp(0)
        
        max_reasonable_length = min(15, n * m)
        
        for length in range(1, max_reasonable_length + 1):
            for i in range(2 ** length):
                binary_seq = format(i, f'0{length}b')
                ways = count_decodings(binary_seq, codes)
                if ways >= 2:
                    print(f"  ❌ Result: AMBIGUOUS (shortest length: {length})")
                    print(f"  Example: '{binary_seq}' can be decoded multiple ways")
                    print(f"  Expected: {expected}\n")
                    return length
        
        print(f"  ✅ Result: NOT ambiguous")
        print(f"  Expected: {expected}\n")
        return -1
    
    solve_example("1 (Ambiguous)", 4, 3, ["101", "10", "1", "100"], 3)
    
    solve_example("2 (Not Ambiguous)", 4, 4, ["1011", "1000", "1111", "1001"], -1)

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Solve your own code system")
    print("2. See example demonstrations")
    print("3. Exit")
    
    try:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            result = solve_bad_codes()
        elif choice == "2":
            run_examples()
        elif choice == "3":
            print("Goodbye!")
        else:
            print("Invalid choice. Please run the program again.")
            
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try running the program again.")
