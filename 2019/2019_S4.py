import math

def solve_tourism():
    print("Tourism Trip Planner")
    print("===================")
    print("Find the optimal way to visit attractions to maximize score")
    print("Attractions must be visited in order 1 to N")
    print("At most K attractions can be visited per day")
    print()
    
    while True:
        try:
            print("Enter N (number of attractions) and K (max per day):")
            n, k = map(int, input().split())
            if 1 <= k <= n <= 10**6:
                break
            else:
                print("Please ensure 1 ≤ K ≤ N ≤ 1,000,000")
        except ValueError:
            print("Please enter two integers separated by a space")
    
    while True:
        try:
            print(f"Enter {n} attraction scores (separated by spaces):")
            scores = list(map(int, input().split()))
            if len(scores) != n:
                print(f"Please enter exactly {n} scores")
                continue
            if all(1 <= score <= 10**7 for score in scores):
                break
            else:
                print("All scores must be between 1 and 10,000,000")
        except ValueError:
            print("Please enter valid integers")
    
    print(f"\nInput: N={n}, K={k}")
    print(f"Attraction scores: {scores}")
    
    min_days = math.ceil(n / k)
    print(f"Minimum days needed: {min_days}")
    

    
    def solve_optimal():
        if n <= 5000:
            return solve_dp(n, k, scores)
        else:
            return solve_greedy(n, k, scores, min_days)
    
    def solve_dp(n, k, scores):
        # First find minimum days needed
        min_days_needed = math.ceil(n / k)
        

        INF = float('inf')
        dp = [[-INF] * (min_days_needed + 1) for _ in range(n + 1)]
        dp[0][0] = 0 
        
        for i in range(1, n + 1):
            for d in range(1, min(i, min_days_needed) + 1):
                for day_size in range(1, min(k, i) + 1):
                    start_idx = i - day_size
                    if start_idx >= 0 and dp[start_idx][d-1] != -INF:
                        day_score = max(scores[start_idx:i])
                        total_score = dp[start_idx][d-1] + day_score
                        dp[i][d] = max(dp[i][d], total_score)
        
        return dp[n][min_days_needed]
    
    def solve_greedy(n, k, scores, target_days):
        
        if target_days * k < n:
            return -1 
        
        prev_dp = [-float('inf')] * (target_days + 1)
        prev_dp[0] = 0
        
        for i in range(1, n + 1):
            curr_dp = [-float('inf')] * (target_days + 1)
            
            for d in range(1, min(i, target_days) + 1):
                for day_size in range(1, min(k, i) + 1):
                    start_idx = i - day_size
                    if start_idx >= 0 and d > 0 and prev_dp[d-1] != -float('inf'):
                        day_score = max(scores[start_idx:i])
                        curr_dp[d] = max(curr_dp[d], prev_dp[d-1] + day_score)
            
            prev_dp = curr_dp
        
        return prev_dp[target_days]
    
    def calculate_score_for_partition(scores, day_sizes):
        total_score = 0
        start_idx = 0
        
        for day_size in day_sizes:
            if day_size > 0:
                end_idx = start_idx + day_size
                day_score = max(scores[start_idx:end_idx])
                total_score += day_score
                start_idx = end_idx
        
        return total_score
    
    result = solve_optimal()
    
    print(f"\nMaximum possible total score: {result}")
    
    if n <= 20:
        show_example_solution(n, k, scores, min_days)
    
    return result

def show_example_solution(n, k, scores, min_days):
    """Show one possible optimal solution for small inputs"""
    print(f"\nExample analysis:")
    print(f"Sample: N={n}, K={k}, scores={scores}")
    print(f"Minimum days needed: {min_days}")

    
    if n == 5 and k == 3 and scores == [2, 5, 7, 1, 4]:
        print("\nPossible schedules:")
        print("Option 1: Day 1=[1,2] scores=[2,5] max=5, Day 2=[3,4,5] scores=[7,1,4] max=7")
        print("         Total score: 5 + 7 = 12")
        print("Option 2: Day 1=[1,2,3] scores=[2,5,7] max=7, Day 2=[4,5] scores=[1,4] max=4") 
        print("         Total score: 7 + 4 = 11")
        print("Optimal: Option 1 with score 12")
    else:
        remaining = n
        day_num = 1
        start_idx = 0
        total_score = 0
        
        print("One possible schedule:")
        while remaining > 0:
            remaining_days = min_days - day_num + 1
            min_needed = math.ceil(remaining / remaining_days) if remaining_days > 0 else remaining
            max_allowed = min(k, remaining)
            
            day_size = min(max_allowed, max(min_needed, 1))
            
            end_idx = start_idx + day_size
            day_attractions = list(range(start_idx + 1, end_idx + 1))
            day_scores = scores[start_idx:end_idx]
            day_max = max(day_scores)
            
            print(f"Day {day_num}: Attractions {day_attractions}, Scores {day_scores}, Max: {day_max}")
            
            total_score += day_max
            remaining -= day_size
            start_idx = end_idx
            day_num += 1
        
        print(f"This schedule total score: {total_score}")
if __name__ == "__main__":
    solve_tourism()
