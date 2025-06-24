def calculate_fence_area():
    
    print("Enter number of fence pieces:")
    print("Enter heights (left to right):")  
    print("Enter widths of each piece:")
    print()
    
    try:
        N = int(input())
        
        heights = list(map(int, input().split()))
        
        widths = list(map(int, input().split()))
        
        total_area = 0
        
        for i in range(N):
            left_height = heights[i]
            right_height = heights[i + 1]
            width = widths[i]
            
            piece_area = width * (left_height + right_height) / 2
            total_area += piece_area
        
        if total_area == int(total_area):
            print(int(total_area))
        else:
            print(total_area)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculate_fence_area()
