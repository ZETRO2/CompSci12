def solve_swipe():
    print("=== SWIPE GAME SOLVER ===")
    print("This program determines if array A can be transformed into array B using swipe operations.")
    print()
    
    print("Enter the length of the arrays:")
    n = int(input())
    
    print(f"Enter array A ({n} space-separated integers):")
    A = list(map(int, input().split()))
    
    print(f"Enter array B ({n} space-separated integers):")
    B = list(map(int, input().split()))
    
    print(f"\nArray A: {A}")
    print(f"Array B: {B}")
    print("\nSolving...")
    print()
    
    queue = [(A[:], [])]
    visited = {tuple(A)}
    
    while queue:
        current, operations = queue.pop(0)
        
        if current == B:
            print("✅ SOLUTION FOUND!")
            print(f"Number of operations needed: {len(operations)}")
            if len(operations) == 0:
                print("Arrays are already identical - no operations needed!")
            else:
                print("\nSequence of operations:")
                for i, (op_type, left, right) in enumerate(operations, 1):
                    if op_type == 'R':
                        print(f"  {i}. Swipe RIGHT on range [{left}, {right}]")
                    else:
                        print(f"  {i}. Swipe LEFT on range [{left}, {right}]")
                
                print(f"\nOutput format:")
                print("YES")
                print(len(operations))
                for op_type, left, right in operations:
                    print(op_type, left, right)
            return
        
        if len(operations) >= 15:
            continue
        
        for left in range(n):
            for right in range(left, n):
                new_array = current[:]
                for i in range(left, right + 1):
                    new_array[i] = current[left]
                
                state = tuple(new_array)
                if state not in visited:
                    visited.add(state)
                    queue.append((new_array, operations + [('R', left, right)]))
                
                new_array = current[:]
                for i in range(left, right + 1):
                    new_array[i] = current[right]
                
                state = tuple(new_array)
                if state not in visited:
                    visited.add(state)
                    queue.append((new_array, operations + [('L', left, right)]))
    
    print("❌ NO SOLUTION EXISTS!")
    print("It's impossible to transform array A into array B using the available swipe operations.")
    print("\nOutput format:")
    print("NO")

def show_examples():
    print("\n" + "="*50)
    print("EXAMPLES:")
    print("="*50)
    
    print("\nExample 1:")
    print("Input: n=3, A=[3,1,2], B=[3,1,1]")
    print("Solution: Swipe RIGHT on [1,2] (sets positions 1,2 to value at position 1)")
    print("Result: [3,1,2] → [3,1,1] ✅")
    
    print("\nExample 2:")
    print("Input: n=4, A=[1,2,4,3], B=[1,4,2,3]")
    print("Result: No solution exists ❌")
    
    print("\nExample 3:")
    print("Input: n=4, A=[2,1,4,3], B=[2,1,4,3]")
    print("Result: Arrays identical, 0 operations needed ✅")
    
    print("\nSwipe Operations Explained:")
    print("• Swipe RIGHT on [ℓ,r]: Copy value at position ℓ to all positions ℓ through r")
    print("• Swipe LEFT on [ℓ,r]: Copy value at position r to all positions ℓ through r")
    print("• Arrays are 0-indexed")

if __name__ == "__main__":
    show_examples()
    print("\n" + "="*50)
    solve_swipe()
