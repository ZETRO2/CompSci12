def solve():
    print("=== Good Influencers Problem Solver ===")
    print("This program finds the minimum cost to make all students intend to write the CCC.")
    print()
    
    print("Enter the number of students:")
    n = int(input())
    print(f"Got {n} students")
    print()
    
    print(f"Enter {n-1} friendships (each as two space-separated student IDs from 1 to {n}):")
    print("Example: if students 1 and 3 are friends, enter: 1 3")
    
    adj = [[] for _ in range(n)]
    for i in range(n - 1):
        print(f"Friendship {i+1}:")
        a, b = map(int, input().split())
        a -= 1 
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    
    print(f"Got all {n-1} friendships")
    print()
    
    print(f"Enter initial intentions as a string of {n} characters:")
    print("Use 'Y' if the student intends to write CCC, 'N' if they don't")
    print(f"Example: YNYN means student 1 intends (Y), student 2 doesn't (N), etc.")
    intentions = input().strip()
    
    while len(intentions) != n:
        print(f"Error: Expected {n} characters, got {len(intentions)}. Please try again:")
        intentions = input().strip()
    
    print(f"Got intentions: {intentions}")
    print()
    
    print(f"Enter {n} space-separated costs (cost to pay each student as an influencer):")
    print("Example: 4 3 6 2 means it costs $4 to pay student 1, $3 for student 2, etc.")
    costs = list(map(int, input().split()))
    
    while len(costs) != n:
        print(f"Error: Expected {n} costs, got {len(costs)}. Please try again:")
        costs = list(map(int, input().split()))
    
    print(f"Got costs: {costs}")
    print()
    
    print("=== Initial State ===")
    initially_wanting = sum(1 for c in intentions if c == 'Y')
    initially_not_wanting = n - initially_wanting
    print(f"Students initially wanting to write CCC: {initially_wanting}")
    print(f"Students initially NOT wanting to write CCC: {initially_not_wanting}")
    
    if initially_not_wanting == 0:
        print("All students already want to write CCC! No cost needed.")
        return 0
    
    print()
    print("=== Finding Optimal Solution ===")
    
    intends = [intentions[i] == 'Y' for i in range(n)]
    
    total_cost = 0
    steps = 0
    
    while not all(intends):
        steps += 1
        print(f"Step {steps}:")
        
        best_influencer = -1
        best_value = -1
        
        candidates = []
        for i in range(n):
            if not intends[i]:
                continue
            
            can_influence = []
            for neighbor in adj[i]:
                if not intends[neighbor]:
                    can_influence.append(neighbor + 1)  
            
            if len(can_influence) == 0:
                continue
            
            candidates.append((i, len(can_influence), costs[i], can_influence))
            
            value = len(can_influence) * 1000 - costs[i]
            
            if value > best_value:
                best_value = value
                best_influencer = i
        
        print("  Available influencers:")
        for student_idx, influence_count, cost, influenced_list in candidates:
            student_num = student_idx + 1
            print(f"    Student {student_num}: Can influence {influence_count} students {influenced_list} for cost ${cost}")
        
        if best_influencer == -1:
            print("  No valid influencers found! Problem unsolvable.")
            break
        
        best_student_num = best_influencer + 1
        influence_count = len([n for n in adj[best_influencer] if not intends[n]])
        print(f"  → Paying student {best_student_num} (cost: ${costs[best_influencer]}, influences: {influence_count} students)")
        
        total_cost += costs[best_influencer]
        
        newly_influenced = []
        for neighbor in adj[best_influencer]:
            if not intends[neighbor]:
                newly_influenced.append(neighbor + 1)  
                intends[neighbor] = True
        
        print(f"  → Students {newly_influenced} now intend to write CCC")
        
        currently_wanting = sum(intends)
        print(f"  → Total students now wanting to write CCC: {currently_wanting}/{n}")
        print()
    
    print("=== Final Result ===")
    if all(intends):
        print(f"SUCCESS! All students now intend to write CCC.")
        print(f"Minimum cost required: ${total_cost}")
    else:
        print("FAILED! Could not make all students intend to write CCC.")
        print("This shouldn't happen with valid input.")
    
    return total_cost

if __name__ == "__main__":
    result = solve()
