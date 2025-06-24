def solve_lunch_concert():

    print("LUNCH CONCERT PROBLEM")
    print("====================")
    print()
    print("Enter your input as follows:")
    print("Line 1: Number of friends (N)")
    print("Next N lines: Pi Wi Di (position, walking_speed, hearing_distance)")
    print()
    
    n = int(input())
    
    friends = []
    for i in range(n):
        pi, wi, di = map(int, input().split())
        friends.append((pi, wi, di))
    
    if n == 2 and friends == [(10, 4, 3), (20, 4, 2)]:
        print("Debug: Sample 2 detected")
        time_at_14 = calculate_total_time(friends, 14)
        print(f"Time at c=14: {time_at_14}")
    
    result = find_minimum_walking_time(friends)
    print(result)

def find_minimum_walking_time(friends):

    if not friends:
        return 0
    
    min_time = float('inf')
    best_c = None
    
    all_positions = [pi for pi, wi, di in friends]
    min_range = min(all_positions) - 100
    max_range = max(all_positions) + 100
    
    for c in range(min_range, max_range + 1):
        total_time = calculate_total_time(friends, c)
        if total_time < min_time:
            min_time = total_time
            best_c = c
    
    print(f"Debug: Best position c={best_c}, min_time={min_time}")
    
    return min_time

def calculate_total_time(friends, concert_pos):

    total_time = 0
    
    for i, (pi, wi, di) in enumerate(friends):
        left_boundary = concert_pos - di
        right_boundary = concert_pos + di
        
        if pi < left_boundary:
            distance_to_walk = left_boundary - pi
        elif pi > right_boundary:
            distance_to_walk = pi - right_boundary
        else:
            distance_to_walk = 0
        
        walking_time = distance_to_walk * wi
        
        if concert_pos == 14 and len(friends) == 2: 
            print(f"Debug: Friend {i+1} at {pi}, speed {wi}, hearing distance {di}")
            print(f"  Hearing range: [{left_boundary}, {right_boundary}]")
            print(f"  Distance to walk: {distance_to_walk}")
            print(f"  Walking time: {walking_time}")
        
        total_time += walking_time
    
    return total_time

if __name__ == "__main__":
    solve_lunch_concert()
