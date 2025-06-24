def main():
    print("=" * 70)
    print("MARSHMALLOW MOLECULES")
    print("=" * 70)
    print("This program finds the minimum number of skewers needed to build")
    print("a stable marshmallow structure with transitivity constraints.")
    print()
    print("CONSTRAINT: If a < b < c, and skewers exist between (a,b) and (a,c),")
    print("then a skewer must also exist between (b,c).")
    print()
    
    print("STEP 1: Enter Structure Parameters")
    print("-" * 34)
    print("Enter N (number of marshmallows) and M (number of requirements):")
    print("Example: 6 4")
    print("Your input: ", end="")
    
    try:
        line = input().strip().split()
        N, M = int(line[0]), int(line[1])
        if N <= 0 or M < 0:
            print("Error: N must be positive, M must be non-negative.")
            return
        print(f"Structure: {N} marshmallows, {M} requirements")
    except (ValueError, IndexError):
        print("Error: Please enter two valid integers.")
        return
    
    print()
    
    if M == 0:
        print("No requirements specified.")
        print("Result: 0 skewers needed")
        return
    
    print("STEP 2: Enter Requirements")
    print("-" * 26)
    print(f"Enter {M} pairs (a_i, b_i) where a_i < b_i:")
    print("Each pair represents a required skewer connection.")
    print("Example format: 1 2")
    
    requirements = []
    for i in range(M):
        print(f"Requirement {i+1}: ", end="")
        try:
            line = input().strip().split()
            a, b = int(line[0]), int(line[1])
            if a >= b or a < 1 or b > N:
                print(f"Error: Invalid pair ({a}, {b}). Must have 1 ≤ a < b ≤ {N}")
                return
            requirements.append((a, b))
        except (ValueError, IndexError):
            print("Error: Please enter two valid integers.")
            return
    
    print(f"Requirements: {requirements}")
    print()
    print("Processing transitivity constraints...")
    print()
    

    adj = [[] for _ in range(N + 1)]
    
    for a, b in requirements:
        adj[a].append(b)
        adj[b].append(a)
    
    for i in range(1, N + 1):
        adj[i].sort()
    
    total_edges = 0
    required_edges = set((a, b) for a, b in requirements)
    all_edges = set()
    
    for a in range(1, N + 1):
        higher_neighbors = []
        for neighbor in adj[a]:
            if neighbor > a:
                higher_neighbors.append(neighbor)
        
        for i in range(len(higher_neighbors)):
            for j in range(i + 1, len(higher_neighbors)):
                b, c = higher_neighbors[i], higher_neighbors[j]
                if b > c:
                    b, c = c, b
                all_edges.add((b, c))
        
        for neighbor in adj[a]:
            if a < neighbor:
                all_edges.add((a, neighbor))
            else:
                all_edges.add((neighbor, a))
    
    changed = True
    while changed:
        changed = False
        new_edges = set()
        
        for a in range(1, N + 1):
            connected = set()
            for b, c in all_edges:
                if b == a:
                    connected.add(c)
                elif c == a:
                    connected.add(b)
            
            connected_list = sorted(connected)
            

            for b in connected_list:
                for c in connected_list:
                    if a < b < c:
                        if (b, c) not in all_edges:
                            new_edges.add((b, c))
                            changed = True
        
        all_edges.update(new_edges)
    
    total_edges = len(all_edges)
    
    print("ANALYSIS:")
    print("-" * 9)
    print(f"Original requirements: {len(requirements)}")
    print(f"Total edges after applying transitivity: {total_edges}")
    print(f"Additional edges needed: {total_edges - len(requirements)}")
    
    if total_edges > len(requirements):
        print()
        print("Additional edges required by transitivity constraint:")
        additional = all_edges - required_edges
        for a, b in sorted(additional):
            print(f"  ({a}, {b})")
    
    print()
    print("RESULT:")
    print("-" * 8)
    print(f"Minimum number of skewers needed: {total_edges}")
    

if __name__ == "__main__":
    main()
