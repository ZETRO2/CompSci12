def generate_cantor_set(N):
    print(f"\n=== DEBUGGING: Starting Cantor set generation for N = {N} ===")
    
    cantor_fractions = set(range(N + 1))
    
    print(f"DEBUG: Initial set size: {len(cantor_fractions)}")
    print(f"DEBUG: Initial fractions: {sorted(cantor_fractions)}")
    
    filter_num = 1
    max_filters = 20 
    
    while filter_num <= max_filters:
        print(f"\n--- Applying Filter {filter_num} ---")
        
        num_intervals = 3 ** filter_num
        interval_length = 1.0 / num_intervals
        
        print(f"DEBUG: Filter {filter_num} - Number of intervals: {num_intervals}")
        print(f"DEBUG: Filter {filter_num} - Each interval length: {interval_length}")
        
        to_remove = set()
        
        groups_processed = 0
        for group_start in range(0, num_intervals, 3):
            if group_start + 2 < num_intervals:
                groups_processed += 1
                middle_interval_index = group_start + 1
                
                interval_start = middle_interval_index * interval_length
                interval_end = (middle_interval_index + 1) * interval_length
                
                print(f"DEBUG: Filter {filter_num} - Group {groups_processed}: intervals {group_start}, {group_start+1}, {group_start+2}")
                print(f"DEBUG: Filter {filter_num} - Removing middle interval [{interval_start:.6f}, {interval_end:.6f}]")
                
                for x in list(cantor_fractions):
                    fraction_value = x / N
                    
                    if interval_start <= fraction_value <= interval_end:

                        if interval_start < fraction_value < interval_end:
                            to_remove.add(x)
                            print(f"DEBUG: Filter {filter_num} - Marking {x}/{N} = {fraction_value:.6f} for removal (strictly inside)")
                        elif fraction_value == interval_start or fraction_value == interval_end:
                          
                            if not (fraction_value == 0.0 or fraction_value == 1.0):
                                left_boundary = middle_interval_index * interval_length
                                right_boundary = (middle_interval_index + 1) * interval_length
  
                                
                                to_remove.add(x)
                                print(f"DEBUG: Filter {filter_num} - Marking {x}/{N} = {fraction_value:.6f} for removal (on boundary)")
        
        print(f"DEBUG: Filter {filter_num} - Processed {groups_processed} groups of 3 intervals")
        
        if to_remove:
            print(f"DEBUG: Filter {filter_num} - Removing {len(to_remove)} fractions: {sorted(to_remove)}")
            cantor_fractions -= to_remove
            print(f"DEBUG: Filter {filter_num} - Remaining fractions: {sorted(cantor_fractions)}")
            print(f"DEBUG: Filter {filter_num} - Remaining count: {len(cantor_fractions)}")
        else:
            print(f"DEBUG: Filter {filter_num} - No fractions removed, stopping")
            break
            
        filter_num += 1
    
    if filter_num > max_filters:
        print(f"WARNING: Reached maximum filter limit of {max_filters}")
    
    result = sorted(cantor_fractions)
    print(f"\n=== FINAL RESULT ===")
    print(f"Total fractions in Cantor set: {len(result)}")
    print(f"Fractions: {result}")
    
    if N == 12:
        print(f"\n=== MANUAL ANALYSIS FOR N=12 ===")
        expected = [0, 1, 3, 4, 8, 9, 11, 12]
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        print(f"Match: {result == expected}")
        
        print(f"\nLet's trace what should happen:")
        print(f"Filter 1: Remove middle third [1/3, 2/3] = [4/12, 8/12] = [0.333..., 0.666...]")
        print(f"  Should remove: 5/12=0.417, 6/12=0.5, 7/12=0.583")
        print(f"  Remaining after filter 1: 0,1,2,3,4,8,9,10,11,12")
        
        print(f"Filter 2: Each remaining interval split into 3, remove middle thirds")
        print(f"  Left interval [0, 1/3]: split into [0,1/9], [1/9,2/9], [2/9,1/3]")
        print(f"  Remove middle [1/9, 2/9] = [0.111..., 0.222...]")
        print(f"  Should remove: 2/12=0.167 (since 1/9 ≈ 0.111 and 2/9 ≈ 0.222)")
        print(f"  Right interval [2/3, 1]: split into [2/3,7/9], [7/9,8/9], [8/9,1]")
        print(f"  Remove middle [7/9, 8/9] = [0.777..., 0.888...]")
        print(f"  Should remove: 10/12=0.833 (since 7/9 ≈ 0.778 and 8/9 ≈ 0.889)")
    
    return result


def analyze_sample_manually():

    print("\n=== MANUAL STEP-BY-STEP ANALYSIS FOR N=12 ===")
    N = 12
    fractions = [(x, x/N) for x in range(N+1)]
    
    print("Initial fractions:")
    for x, val in fractions:
        print(f"  {x}/12 = {val:.6f}")
    
    print("\nCantor set construction:")
    print("Filter 1: Remove middle third [1/3, 2/3]")
    print(f"  1/3 = {1/3:.6f}, 2/3 = {2/3:.6f}")
    
    remaining = []
    removed_f1 = []
    
    for x, val in fractions:
        if 1/3 < val < 2/3:  
            removed_f1.append((x, val))
        else:
            remaining.append((x, val))
    
    print(f"  Removed: {[x for x, _ in removed_f1]} -> {removed_f1}")
    print(f"  Remaining: {[x for x, _ in remaining]}")
    
    print("\nFilter 2: For each remaining interval, remove middle third")
    print("Left interval [0, 1/3]: remove middle third [1/9, 2/9]")
    print(f"  1/9 = {1/9:.6f}, 2/9 = {2/9:.6f}")
    
    print("Right interval [2/3, 1]: remove middle third [7/9, 8/9]")
    print(f"  7/9 = {7/9:.6f}, 8/9 = {8/9:.6f}")
    
    final_remaining = []
    removed_f2 = []
    
    for x, val in remaining:
        if (1/9 < val < 2/9) or (7/9 < val < 8/9):
            removed_f2.append((x, val))
        else:
            final_remaining.append((x, val))
    
    print(f"  Removed in filter 2: {[x for x, _ in removed_f2]} -> {removed_f2}")
    print(f"  Final remaining: {[x for x, _ in final_remaining]}")
    
    return [x for x, _ in final_remaining]


def generate_cantor_set_corrected(N):

    print(f"\n=== CORRECTED CANTOR SET GENERATION FOR N = {N} ===")
    
    if N == 12:
        manual_result = analyze_sample_manually()
        print(f"Manual analysis result: {manual_result}")
    
    cantor_fractions = set(range(N + 1))
    
    filter_num = 1
    max_filters = 20
    
    while filter_num <= max_filters:
        print(f"\n--- Corrected Filter {filter_num} ---")
        
        to_remove = set()

        power_of_3 = 3 ** filter_num
        
        interval_length = 1.0 / power_of_3
        
        print(f"DEBUG: Filter {filter_num} - Interval length: {interval_length}")
        print(f"DEBUG: Filter {filter_num} - Number of intervals: {power_of_3}")
        
        for group_start in range(0, power_of_3, 3):
            if group_start + 2 < power_of_3:
                middle_start = (group_start + 1) * interval_length
                middle_end = (group_start + 2) * interval_length
                
                print(f"DEBUG: Removing interval [{middle_start:.6f}, {middle_end:.6f}]")
                
                for x in list(cantor_fractions):
                    fraction_value = x / N
                    
                    epsilon = 1e-12
                    
                    if middle_start + epsilon < fraction_value < middle_end - epsilon:
                        to_remove.add(x)
                        print(f"DEBUG: Removing {x}/{N} = {fraction_value:.6f}")
        
        if to_remove:
            cantor_fractions -= to_remove
            print(f"DEBUG: Removed {len(to_remove)} fractions: {sorted(to_remove)}")
            print(f"DEBUG: Remaining: {sorted(cantor_fractions)}")
        else:
            print(f"DEBUG: No more fractions to remove")
            break
        
        filter_num += 1
    
    return sorted(cantor_fractions)


def main():

    print("=" * 60)
    print("CANTOR SET FILTER PROBLEM SOLVER")
    print("=" * 60)
    print()
    print("This program finds all integers x where 0 ≤ x ≤ N such that")
    print("the fraction x/N is in the Cantor set.")
    print()
    print("The Cantor set is constructed by repeatedly removing the")
    print("middle third of intervals using filters.")
    print()
    print("INSTRUCTIONS:")
    print("- Enter a positive integer N when prompted")
    print("- The program will show all x values where x/N is in the Cantor set")
    print("- Debug information will be displayed to show the filtering process")
    print()
    
    while True:
        try:
            user_input = input("Enter N (positive integer, or 'quit' to exit): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            N = int(user_input)
            
            if N <= 0:
                print("ERROR: N must be a positive integer. Please try again.")
                continue
            
            if N > 1000:
                confirm = input(f"WARNING: N={N} is large and may take time. Continue? (y/n): ")
                if confirm.lower() not in ['y', 'yes']:
                    continue
            
            print(f"\nProcessing N = {N}...")
            result = generate_cantor_set_corrected(N)
            
            print("\n" + "=" * 50)
            print("FINAL ANSWER:")
            print("=" * 50)
            print(f"For N = {N}, the integers x where x/N is in the Cantor set are:")
            print()
            
            for i, x in enumerate(result):
                if i > 0 and i % 10 == 0:
                    print() 
                print(f"{x:3d}", end=" ")
            
            print(f"\n\nTotal count: {len(result)} integers")
            
            if N == 12:
                expected = [0, 1, 3, 4, 8, 9, 11, 12]
                print(f"\nVERIFICATION:")
                print(f"Expected: {expected}")
                print(f"Got:      {result}")
                print(f"Match: {result == expected}")
            
            print(f"\nSome example fractions in the Cantor set:")
            for i, x in enumerate(result[:min(8, len(result))]):
                print(f"  {x}/{N} = {x/N:.6f}")
                if i >= 7:
                    break
            
            if len(result) > 8:
                print(f"  ... and {len(result) - 8} more")
            
            print("\n" + "-" * 50)
            
        except ValueError:
            print("ERROR: Please enter a valid integer or 'quit'.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"ERROR: An unexpected error occurred: {e}")
            print("Please try again with a different input.")


if __name__ == "__main__":
    main()
