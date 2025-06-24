def solve_good_triplets():
    print("Enter N and C:")
    n, c = map(int, input().split())
    
    print(f"Enter {n} positions (0 to {c-1}):")
    positions = list(map(int, input().split()))
    
    import math
    points = []
    for pos in positions:
        angle = 2 * math.pi * pos / c
        x = math.cos(angle)
        y = math.sin(angle)
        points.append((x, y))
    
    print("Points on circle:")
    for i, (pos, point) in enumerate(zip(positions, points)):
        print(f"  P{i+1}: position {pos} -> ({point[0]:.3f}, {point[1]:.3f})")
    print()
    
    def cross_product_sign(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    
    def is_origin_inside_triangle(p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2  
        x3, y3 = p3
        
        denom = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
        
        if abs(denom) < 1e-10:
            return False
            
        a = ((y2 - y3) * (0 - x3) + (x3 - x2) * (0 - y3)) / denom
        b = ((y3 - y1) * (0 - x3) + (x1 - x3) * (0 - y3)) / denom
        c = 1 - a - b
        
        epsilon = 1e-10
        return a > epsilon and b > epsilon and c > epsilon
    
    count = 0
    good_triplets = []
    
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if positions[a] == positions[b] or positions[b] == positions[c] or positions[a] == positions[c]:
                    continue
                    
                if is_origin_inside_triangle(points[a], points[b], points[c]):
                    count += 1
                    good_triplets.append((a + 1, b + 1, c + 1))
    
    print(f"\nNumber of distinct good triplets: {count}")
    
    if count <= 20:  
        print("Good triplets found:")
        for triplet in good_triplets:
            a_idx, b_idx, c_idx = triplet[0]-1, triplet[1]-1, triplet[2]-1
            print(f"  {triplet} -> positions ({positions[a_idx]}, {positions[b_idx]}, {positions[c_idx]})")
    
    return count

print("=== Good Triplets Problem Solver ===")
print("\nSample Input:")
print("8 10")
print("0 2 5 5 6 9 0 0")
print("Expected Output: 6")
print("\nRun the solver:")

result = solve_good_triplets()
