def calculate_minimum_swaps():
    print("=" * 60)
    print("VALENTINA'S BOOK ARRANGEMENT CALCULATOR")
    print("=" * 60)
    print()
    print("This program helps Valentina arrange her books optimally.")
    print()
    print("Goal arrangement: All L books → All M books → All S books")
    print("Where:")
    print("  L = Large books")
    print("  M = Medium books") 
    print("  S = Small books")
    print()
    print("The program calculates the minimum number of swaps needed")
    print("to achieve this arrangement.")
    print()
    print("Input format:")
    print("  • Enter a string of L, M, and S characters")
    print("  • Each character represents a book size")
    print("  • At least 1 character required")
    print()
    print("-" * 60)
    
    while True:
        try:
            print("\nEnter the current arrangement of books:")
            print("(Use L for large, M for medium, S for small)")
            
            books = input("Book arrangement: ").strip().upper()
            
            if not books:
                print("Error: Please enter at least one book.")
                continue
            
            valid_chars = set(['L', 'M', 'S'])
            if not all(char in valid_chars for char in books):
                invalid_chars = set(books) - valid_chars
                print(f"Error: Invalid characters found: {invalid_chars}")
                print("Please use only L, M, and S.")
                continue
            
            count_L = books.count('L')
            count_M = books.count('M')
            count_S = books.count('S')
            
            print(f"\nBook counts:")
            print(f"  Large (L): {count_L}")
            print(f"  Medium (M): {count_M}")
            print(f"  Small (S): {count_S}")
            print(f"  Total books: {len(books)}")
            
            min_swaps = calculate_swaps(books, count_L, count_M, count_S)
            
            target = 'L' * count_L + 'M' * count_M + 'S' * count_S
            
            print(f"\nCurrent arrangement: {books}")
            print(f"Target arrangement:  {target}")
            print(f"\nMinimum swaps needed: {min_swaps}")
            
            if min_swaps > 0:
                print(f"\nExplanation:")
                explain_swaps(books, count_L, count_M, count_S)
            else:
                print(f"\nExplanation: Books are already arranged correctly!")
            
            break
            
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user.")
            return
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

def calculate_swaps(books, count_L, count_M, count_S):
    n = len(books)
    
    if count_L == n or count_M == n or count_S == n:
        return 0
    
    L_end = count_L
    M_end = count_L + count_M
    
    L_section_M = 0
    L_section_S = 0  
    
    M_section_L = 0  
    M_section_S = 0 
    
    S_section_L = 0  
    S_section_M = 0 
    
    for i, book in enumerate(books):
        if i < L_end:  
            if book == 'M':
                L_section_M += 1
            elif book == 'S':
                L_section_S += 1
        elif i < M_end:  
            if book == 'L':
                M_section_L += 1
            elif book == 'S':
                M_section_S += 1
        else:  
            if book == 'L':
                S_section_L += 1
            elif book == 'M':
                S_section_M += 1
    
    direct_LM = min(L_section_M, M_section_L)
    direct_LS = min(L_section_S, S_section_L) 
    direct_MS = min(M_section_S, S_section_M)
    
    remaining_LM = L_section_M - direct_LM 
    remaining_ML = M_section_L - direct_LM  
    remaining_LS = L_section_S - direct_LS 
    remaining_SL = S_section_L - direct_LS 
    remaining_MS = M_section_S - direct_MS 
    remaining_SM = S_section_M - direct_MS
    
    cycles_LMS = min(remaining_LM, remaining_MS, remaining_SL)
    cycles_LSM = min(remaining_LS, remaining_SM, remaining_ML)
    
    total_swaps = direct_LM + direct_LS + direct_MS + 2 * (cycles_LMS + cycles_LSM)
    
    return total_swaps

def explain_swaps(books, count_L, count_M, count_S):
    n = len(books)
    L_end = count_L
    M_end = count_L + count_M
    
    print("The arrangement needs to be: L...L M...M S...S")
    print(f"  L section: positions 1-{L_end}")
    if count_M > 0:
        print(f"  M section: positions {L_end+1}-{M_end}")
    if count_S > 0:
        print(f"  S section: positions {M_end+1}-{n}")
    
    L_section_wrong = []
    M_section_wrong = []
    S_section_wrong = []
    
    for i, book in enumerate(books):
        if i < L_end and book != 'L':
            L_section_wrong.append(f"Position {i+1}: {book}")
        elif L_end <= i < M_end and book != 'M':
            M_section_wrong.append(f"Position {i+1}: {book}")
        elif i >= M_end and book != 'S':
            S_section_wrong.append(f"Position {i+1}: {book}")
    
    if L_section_wrong or M_section_wrong or S_section_wrong:
        print("\nMisplaced books:")
        if L_section_wrong:
            print(f"  In L section (should be L): {', '.join(L_section_wrong)}")
        if M_section_wrong:
            print(f"  In M section (should be M): {', '.join(M_section_wrong)}")
        if S_section_wrong:
            print(f"  In S section (should be S): {', '.join(S_section_wrong)}")
    
    L_section_M = sum(1 for i, book in enumerate(books) if i < L_end and book == 'M')
    L_section_S = sum(1 for i, book in enumerate(books) if i < L_end and book == 'S')
    M_section_L = sum(1 for i, book in enumerate(books) if L_end <= i < M_end and book == 'L')
    M_section_S = sum(1 for i, book in enumerate(books) if L_end <= i < M_end and book == 'S')
    S_section_L = sum(1 for i, book in enumerate(books) if i >= M_end and book == 'L')
    S_section_M = sum(1 for i, book in enumerate(books) if i >= M_end and book == 'M')
    
    print(f"\nMisplaced book counts:")
    print(f"  M books in L section: {L_section_M}")
    print(f"  S books in L section: {L_section_S}") 
    print(f"  L books in M section: {M_section_L}")
    print(f"  S books in M section: {M_section_S}")
    print(f"  L books in S section: {S_section_L}")
    print(f"  M books in S section: {S_section_M}")
    
    direct_LM = min(L_section_M, M_section_L)
    direct_LS = min(L_section_S, S_section_L)
    direct_MS = min(M_section_S, S_section_M)
    
    print(f"\nSwap calculation:")
    print(f"  Direct L↔M swaps: min({L_section_M}, {M_section_L}) = {direct_LM}")
    print(f"  Direct L↔S swaps: min({L_section_S}, {S_section_L}) = {direct_LS}")
    print(f"  Direct M↔S swaps: min({M_section_S}, {S_section_M}) = {direct_MS}")
    
    remaining_LM = L_section_M - direct_LM
    remaining_ML = M_section_L - direct_LM
    remaining_LS = L_section_S - direct_LS
    remaining_SL = S_section_L - direct_LS
    remaining_MS = M_section_S - direct_MS
    remaining_SM = S_section_M - direct_MS
    
    cycles_LMS = min(remaining_LM, remaining_MS, remaining_SL)
    cycles_LSM = min(remaining_LS, remaining_SM, remaining_ML)
    
    if cycles_LMS > 0 or cycles_LSM > 0:
        print(f"  3-way cycles (each needs 2 swaps):")
        if cycles_LMS > 0:
            print(f"    L→M→S→L cycles: {cycles_LMS} (contributes {2*cycles_LMS} swaps)")
        if cycles_LSM > 0:
            print(f"    L→S→M→L cycles: {cycles_LSM} (contributes {2*cycles_LSM} swaps)")
    
    total = direct_LM + direct_LS + direct_MS + 2 * (cycles_LMS + cycles_LSM)
    print(f"  Total: {direct_LM} + {direct_LS} + {direct_MS} + {2*(cycles_LMS + cycles_LSM)} = {total} swaps")
    
def show_examples():
    print("\n" + "=" * 50)
    print("SAMPLE EXAMPLES:")
    print("=" * 50)
    
    print("\nExample 1: LMMS")
    print("Current: L M M S")
    print("Target:  L M M S")
    print("Result: 0 swaps (already arranged correctly)")
    
    print("\nExample 2: LLSLM")
    print("Current: L L S L M")
    print("Target:  L L L M S")
    print("Positions: 1 2 3 4 5")
    print("Issues:")
    print("  - Position 3 has S, should be L")
    print("  - Position 4 has L, should be M") 
    print("  - Position 5 has M, should be S")
    print("Result: 2 swaps needed")

def main():
    """Main function to run the book arrangement calculator."""
    try:
        while True:
            choice = input("Would you like to see sample examples first? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                show_examples()
                break
            elif choice in ['n', 'no']:
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        
        calculate_minimum_swaps()
        
        while True:
            print("\n" + "-" * 60)
            choice = input("Would you like to calculate swaps for another arrangement? (y/n): ").lower().strip()
            
            if choice in ['y', 'yes']:
                calculate_minimum_swaps()
            elif choice in ['n', 'no']:
                print("\nThank you for helping Valentina organize her books!")
                print("Goodbye!")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
                
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")

if __name__ == "__main__":
    main()
