def main():
    print("=" * 50)
    print("WINTER DRIVING")
    print("=" * 50)
    print("This program processes a weighted tree and finds optimal partitions.")
    print("It uses dynamic programming and meet-in-the-middle techniques.")
    print()
    
    print("STEP 1: Enter Number of Nodes")
    print("-" * 32)
    print("Enter the number of nodes in the tree (n).")
    print("Example: 5")
    print("Your input: ", end="")
    
    try:
        n = int(input().strip())
        if n <= 0:
            print("Error: Number of nodes must be positive.")
            return
        print(f"Tree will have {n} nodes.")
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return
    
    print()
    
    print("STEP 2: Enter Node Values")
    print("-" * 26)
    print(f"Enter {n} positive integers (the weight/value of each node).")
    print("Separate values with spaces on a single line.")
    print("Example: 3 1 4 2 5")
    print("Your input: ", end="")
    
    try:
        values = list(map(int, input().strip().split()))
        if len(values) != n:
            print(f"Error: Please enter exactly {n} values.")
            return
        for val in values:
            if val <= 0:
                print("Error: All node values must be positive.")
                return
        print(f"Node values: {values}")
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
        return
    
    print()
    
    print("STEP 3: Enter Tree Structure")
    print("-" * 28)
    print(f"Enter {n-1} integers (parent of nodes 2, 3, ..., {n}).")
    print("Node 1 is the root. Each parent must be between 1 and the current node number.")
    print("Example for 5 nodes: 1 1 2 2")
    print("This means: node 2's parent is 1, node 3's parent is 1, node 4's parent is 2, node 5's parent is 2")
    print("Your input: ", end="")
    
    try:
        parents = list(map(int, input().strip().split()))
        if len(parents) != n - 1:
            print(f"Error: Please enter exactly {n-1} parent values.")
            return
        for i, parent in enumerate(parents):
            if parent < 1 or parent > i + 1:
                print(f"Error: Parent of node {i+2} must be between 1 and {i+1}.")
                return
        print(f"Parent structure: {parents}")
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
        return
    
    print()
    print("Processing tree...")
    print()
    
    adj = [[] for _ in range(n + 1)]
    arr = [0] * (n + 1)
    sum_vals = [0] * (n + 1)
    cnt = [0] * (n + 1)
    
    for i in range(n):
        arr[i + 1] = values[i]
    
    tot = sum(values)
    
    for i in range(n - 1):
        parent = parents[i]
        child = i + 2
        adj[parent].append(child)
        adj[child].append(parent)
    
    def dfs(u, p):
        sum_vals[u] = arr[u]
        for x in adj[u]:
            if x != p:
                dfs(x, u)
                cnt[u] += cnt[x] + (arr[u] * sum_vals[x])
                sum_vals[u] += sum_vals[x]
    
    ma = 0
    
    def dfs2(u, p, up_cnt=0, up_sum=0):
        nonlocal ma
        
        cur = []
        cur_sum = 0
        cur_cnt = 0
        cur_ans = up_cnt
        threshold = tot - arr[u]
        
        for x in adj[u]:
            if x != p:
                cur_sum += sum_vals[x]
                cur_cnt += cnt[x]
                cur_ans += cnt[x]
                cur.append(sum_vals[x])
        
        cur.append(threshold - cur_sum)
        cur.sort()
        cur_ans += arr[u] * threshold
        
        if cur[-1] >= threshold - cur[-1]:
            cur_ans += cur[-1] * (threshold - cur[-1])
        else:
            n1 = len(cur) // 2
            n2 = len(cur) - n1
            
            sub1 = []
            for x in range(1 << n1):
                cc = 0
                for y in range(n1):
                    if (x >> y) & 1:
                        cc += cur[y]
                sub1.append(cc)
            
            sub2 = []
            for x in range(1 << n2):
                cc = 0
                for y in range(n2):
                    if (x >> y) & 1:
                        cc += cur[y + n1]
                sub2.append(cc)
            
            sub1.sort()
            sub2.sort(reverse=True)
            
            cur_ma = 0
            y = 0
            for x in range(len(sub1)):
                while y < len(sub2) and sub1[x] + sub2[y] > threshold // 2:
                    y += 1
                for z in range(-1, 2):
                    if 0 <= y + z < len(sub2):
                        val = (sub1[x] + sub2[y + z]) * (threshold - sub1[x] - sub2[y + z])
                        cur_ma = max(cur_ma, val)
            
            cur_ans += cur_ma
        
        ma = max(ma, cur_ans)
        cur_sum += up_sum
        cur_cnt += up_cnt
        
        for x in adj[u]:
            if x != p:
                new_cnt = cur_cnt - cnt[x] + (cur_sum - sum_vals[x]) * arr[u]
                new_sum = cur_sum + arr[u] - sum_vals[x]
                dfs2(x, u, new_cnt, new_sum)
    
    dfs(1, 1)
    dfs2(1, 1)
    
    for x in range(1, n + 1):
        ma += arr[x] * (arr[x] - 1)
    
    print("RESULT:")
    print("-" * 8)
    print(f"Maximum value: {ma}")
    
    print()
    print("Processing complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
