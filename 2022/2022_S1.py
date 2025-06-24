def count_ways(n):

    count = 0
    
    for num_fours in range(n // 4 + 1):
        remaining = n - 4 * num_fours
        
        if remaining % 5 == 0:
            num_fives = remaining // 5
            count += 1

    
    return count

def main():
    try:
        print("Good Fours and Good Fives Calculator")
        print("Enter a number to find how many ways it can be expressed as a sum of 4s and 5s")
        print("Enter 'q' to quit")
        print()
        
        while True:
            user_input = input("Enter a number: ").strip()
            
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
            
            try:
                n = int(user_input)
                if n < 0:
                    print("Please enter a non-negative number.")
                    continue
                
                result = count_ways(n)
                print(f"Number of ways to express {n} as sum of 4s and 5s: {result}")
                
                if result > 0 and result <= 10:
                    print("Combinations:")
                    for num_fours in range(n // 4 + 1):
                        remaining = n - 4 * num_fours
                        if remaining % 5 == 0:
                            num_fives = remaining // 5
                            print(f"  {num_fours} fours + {num_fives} fives = {4*num_fours} + {5*num_fives} = {n}")
                elif result > 10:
                    print("(Too many combinations to display)")
                print()
                
            except ValueError:
                print("Please enter a valid integer or 'q' to quit.")
                
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()
