def solve_triangle():
    print("=== Triangle Data Structure Solver ===")
    print("Please enter the triangle size N and sub-triangle size K:")
    n, k = map(int, input().split())
    
    print(f"\nNow enter the triangle with {n} rows:")
    print("(Row i should contain i space-separated integers)")
    
    triangle = []
    for i in range(n):
        print(f"Enter row {i+1} (should have {i+1} elements):", end=" ")
        row = list(map(int, input().split()))
        triangle.append(row)
    
    print(f"\nProcessing triangle to find all sub-triangles of size {k}...")
    
    total_sum = 0
    subtriangle_count = 0
    
    for start_row in range(n - k + 1):  
        max_start_col = len(triangle[start_row + k - 1]) - k + 1
        for start_col in range(max_start_col):
            max_element = 0
            elements_in_subtriangle = []
            
            for sub_row in range(k):
                actual_row = start_row + sub_row
                row_elements = []
                for sub_col in range(sub_row + 1):
                    actual_col = start_col + sub_col
                    element = triangle[actual_row][actual_col]
                    row_elements.append(element)
                    max_element = max(max_element, element)
                
                elements_in_subtriangle.append(row_elements)
            
            subtriangle_count += 1
            total_sum += max_element
            
            print(f"Sub-triangle {subtriangle_count} starting at row {start_row+1}, col {start_col+1}:")
            for row_elements in elements_in_subtriangle:
                print(f"  {row_elements}")
            print(f"  Maximum element: {max_element}")
            print()
    
    print(f"Found {subtriangle_count} sub-triangles of size {k}")
    print(f"Sum of all maximum elements: {total_sum}")
    
    return total_sum

def test_with_sample():
    """Test with the provided sample to verify correctness"""
    print("=== Testing with Sample Input ===")
    
    triangle = [
        [3],
        [1, 2],
        [4, 2, 1],
        [6, 1, 4, 2]
    ]
    n, k = 4, 2
    
    print(f"Triangle of size {n}:")
    for i, row in enumerate(triangle):
        spaces = " " * (n - i - 1)
        print(f"{spaces}{' '.join(map(str, row))}")
    
    print(f"\nFinding all sub-triangles of size {k}:")
    
    total_sum = 0
    subtriangle_count = 0
    
    for start_row in range(n - k + 1): 
        for start_col in range(len(triangle[start_row]) - k + 1):
            max_element = 0
            elements_in_subtriangle = []
            
            for sub_row in range(k): 
                actual_row = start_row + sub_row
                row_elements = []
                for sub_col in range(sub_row + 1): 
                    actual_col = start_col + sub_col
                    element = triangle[actual_row][actual_col]
                    row_elements.append(element)
                    max_element = max(max_element, element)
                
                elements_in_subtriangle.append(row_elements)
            
            subtriangle_count += 1
            total_sum += max_element
            
            print(f"Sub-triangle {subtriangle_count}:")
            for row_elements in elements_in_subtriangle:
                print(f"  {row_elements}")
            print(f"  Maximum: {max_element}")
            print()
    
    print(f"Total sum: {total_sum}")
    print(f"Expected: 23")
    return total_sum

print("First, let's test with the sample input to verify correctness:")
test_result = test_with_sample()

print(f"\n{'='*50}")
print("Now you can input your own triangle:")
print("(Press Ctrl+C to exit)")

try:
    result = solve_triangle()
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
