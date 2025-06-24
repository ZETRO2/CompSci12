def solve_symmetric_mountains():

    print("=== Symmetric Mountains Solver ===")
    print("Enter the number of mountains:")
    n = int(input().strip())
    
    print("Enter the heights of the mountains (space-separated):")
    heights = list(map(int, input().strip().split()))
    
    results = []
    
    for crop_length in range(1, n + 1):
        min_asymmetric_value = float('inf')
        
        for start in range(n - crop_length + 1):
            crop = heights[start:start + crop_length]
            
            asymmetric_value = calculate_asymmetric_value(crop)
            
            if asymmetric_value < min_asymmetric_value:
                min_asymmetric_value = asymmetric_value
        
        results.append(min_asymmetric_value)
    
    print(" ".join(map(str, results)))

def calculate_asymmetric_value(crop):
    n = len(crop)
    asymmetric_value = 0
    
    for i in range(n // 2):
        left_mountain = crop[i]
        right_mountain = crop[n - 1 - i]
        asymmetric_value += abs(left_mountain - right_mountain)
    
    return asymmetric_value

def test_sample1():
    print("Testing Sample 1:")
    heights = [3, 1, 4, 1, 5, 9, 2]
    n = len(heights)
    
    print(f"Heights: {heights}")
    
    results = []
    for crop_length in range(1, n + 1):
        min_asymmetric_value = float('inf')
        best_crop = None
        best_start = -1
        
        for start in range(n - crop_length + 1):
            crop = heights[start:start + crop_length]
            asymmetric_value = calculate_asymmetric_value(crop)
            
            if asymmetric_value < min_asymmetric_value:
                min_asymmetric_value = asymmetric_value
                best_crop = crop
                best_start = start
        
        results.append(min_asymmetric_value)
        print(f"Length {crop_length}: Best crop = {best_crop} (start at {best_start}), asymmetric value = {min_asymmetric_value}")
    
    print(f"Results: {' '.join(map(str, results))}")
    print("Expected: 0 2 0 5 2 10 10")
    print()

def test_sample2():
    print("Testing Sample 2:")
    heights = [1, 3, 5, 6]
    n = len(heights)
    
    print(f"Heights: {heights}")
    
    results = []
    for crop_length in range(1, n + 1):
        min_asymmetric_value = float('inf')
        best_crop = None
        best_start = -1
        
        for start in range(n - crop_length + 1):
            crop = heights[start:start + crop_length]
            asymmetric_value = calculate_asymmetric_value(crop)
            
            if asymmetric_value < min_asymmetric_value:
                min_asymmetric_value = asymmetric_value
                best_crop = crop
                best_start = start
        
        results.append(min_asymmetric_value)
        print(f"Length {crop_length}: Best crop = {best_crop} (start at {best_start}), asymmetric value = {min_asymmetric_value}")
    
    print(f"Results: {' '.join(map(str, results))}")
    print("Expected: 0 1 3 7")
    print()

def manual_verification():
    print("Manual verification for Sample 1:")
    heights = [3, 1, 4, 1, 5, 9, 2]
    print(f"Heights: {heights}")
    print()
    
    print("Checking all crops of length 5:")
    for start in range(len(heights) - 5 + 1):
        crop = heights[start:start + 5]
        asymmetric_value = calculate_asymmetric_value(crop)
        print(f"Crop {crop}: asymmetric value = {asymmetric_value}")
        
        pairs = []
        total = 0
        for i in range(len(crop) // 2):
            left = crop[i]
            right = crop[len(crop) - 1 - i]
            diff = abs(left - right)
            pairs.append(f"|{left} - {right}| = {diff}")
            total += diff
        print(f"  Calculation: {' + '.join(pairs)} = {total}")
        print()

if __name__ == "__main__":
    test_sample1()
    test_sample2()
    manual_verification()
    
    print("="*50)
    print("Now running interactive solver:")
    solve_symmetric_mountains()
