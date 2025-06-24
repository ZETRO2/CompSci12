def main():
    print("=" * 10)
    print("Sirtet")
    print("=" * 10)
    print("This program processes a grid of '#' and '.' characters.")
    print("It finds connected components and applies shortest path calculations.")
    print()
    
    print("STEP 1: Enter Grid Dimensions")
    print("-" * 30)
    print("Enter the number of rows (n) and columns (m) separated by a space.")
    print("Example: 5 7")
    print("Your input: ", end="")
    
    try:
        line = input().strip().split()
        n, m = int(line[0]), int(line[1])
        print(f"Grid size: {n} rows × {m} columns")
    except (ValueError, IndexError):
        print("Error: Please enter two valid integers separated by a space.")
        return
    
    print()
    
    print("STEP 2: Enter Grid Data")
    print("-" * 25)
    print(f"Enter {n} lines, each containing exactly {m} characters.")
    print("Use '#' for filled cells and '.' for empty cells.")
    print("Example:")
    print("  .#.....")
    print("  .#.....")
    print("  .......")
    print()
    
    arr = []
    for _ in range(n):
        arr.append([0] * m)
    
    mp = []
    for _ in range(n):
        mp.append([0] * m)
    
    vis = []
    for _ in range(n):
        vis.append([False] * m)
    
    cc = 0
    
    for x in range(n):
        print(f"Enter row {x + 1}: ", end="")
        line = input().strip()
        
        if len(line) != m:
            print(f"Error: Row {x + 1} should have exactly {m} characters.")
            return
        
        for y in range(m):
            if line[y] == '#':
                arr[x][y] = 1
            elif line[y] == '.':
                arr[x][y] = 0
            else:
                print(f"Error: Invalid character '{line[y]}' at position {y + 1}. Use only '#' or '.'")
                return
    
    print()
    print("Processing grid...")
    print()
    
    for x in range(n):
        for y in range(m):
            if vis[x][y] or not arr[x][y]:
                continue
            
            cc += 1
            vis[x][y] = True
            mp[x][y] = cc
            
            queue = [(x, y)]
            head = 0
            
            while head < len(queue):
                xx, yy = queue[head]
                head += 1
                
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    nx = xx + dx
                    ny = yy + dy
                    
                    if (0 <= nx < n and 0 <= ny < m and 
                        arr[nx][ny] and not vis[nx][ny]):
                        vis[nx][ny] = True
                        mp[nx][ny] = cc
                        queue.append((nx, ny))
    
    cc += 1
    adj = []
    for _ in range(cc + 1):
        adj.append([])
    
    for y in range(m):
        prev_mp = -1
        prev = -1
        
        for x in range(n):
            if arr[x][y]:
                if prev != -1:
                    adj[mp[x][y]].append((prev_mp, x - prev - 1))
                prev = x
                prev_mp = mp[x][y]
        
        if prev != -1:
            adj[cc].append((prev_mp, n - prev - 1))
    
    INF = 999999999
    dist = [INF] * (cc + 1)
    
    pq = [(0, cc)]
    dist[cc] = 0
    
    while pq:
        min_idx = 0
        for i in range(1, len(pq)):
            if pq[i][0] < pq[min_idx][0]:
                min_idx = i
        
        w, u = pq[min_idx]
        pq.pop(min_idx)
        
        if w > dist[u]:
            continue
        
        for neighbor, weight in adj[u]:
            if dist[neighbor] > dist[u] + weight:
                dist[neighbor] = dist[u] + weight
                pq.append((dist[neighbor], neighbor))
    
    ne = []
    for _ in range(n):
        ne.append([0] * m)
    
    for x in range(n):
        for y in range(m):
            if arr[x][y]:
                new_x = x + dist[mp[x][y]]
                if new_x < n: 
                    ne[new_x][y] = 1
    
    print("RESULT:")
    print("-" * 8)
    for x in range(n):
        row = ""
        for y in range(m):
            row += '#' if ne[x][y] else '.'
        print(row)
    
    print()
    print("Processing complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
