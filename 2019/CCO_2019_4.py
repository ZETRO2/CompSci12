def main():
    print("=" * 80)
    print("CARD SCORING")
    print("=" * 80)
    print("This program finds the optimal strategy for scoring cards.")
    print("You draw cards in order and can choose when to score your current hand.")
    print("Scoring a hand of x cards gives you x^(k/2) points.")
    print()
    
    print("STEP 1: Enter Parameters")
    print("-" * 24)
    print("Enter two integers k and n separated by a space:")
    print("- k: The scoring exponent parameter (positive even integer)")
    print("- n: The number of cards to draw (positive integer)")
    print("Example: 4 5")
    print("Your input: ", end="")
    
    try:
        line = input().strip().split()
        k, n = int(line[0]), int(line[1])
        if k <= 0 or n <= 0:
            print("Error: Both k and n must be positive integers.")
            return
        print(f"Parameters: k = {k}, n = {n}")
        print(f"Scoring function: x^{k/2}")
    except (ValueError, IndexError):
        print("Error: Please enter two valid positive integers separated by a space.")
        return
    
    print()
    
    if k == 2:
        print("SPECIAL CASE DETECTED:")
        print("-" * 20)
        print("When k = 2, the answer is simply n.")
        print(f"Result: {n}")
        print("=" * 80)
        return
    
    print("STEP 2: Enter Card Sequence")
    print("-" * 27)
    print(f"Enter {n} integers (the cards you will draw in order).")
    print("Each integer represents the value/type of the card.")
    print("Enter one card value per line:")
    
    sequence = []
    for i in range(n):
        print(f"Card {i+1}: ", end="")
        try:
            card = int(input().strip())
            sequence.append(card)
        except ValueError:
            print("Error: Please enter a valid integer.")
            return
    
    print(f"Card sequence: {sequence}")
    print()
    print("Processing...")
    print()
    
    MAXN = 1000005
    pos = [0] * MAXN
    cnt = [0] * MAXN  
    dp = [0.0] * MAXN
    po = [0.0] * (2 * MAXN) 
    buf = [[] for _ in range(MAXN)] 
    
    def poww(x):
        idx = x + MAXN
        if po[idx] > 1e-4:
            return po[idx]
        po[idx] = abs(x) ** (k / 2.0)
        return po[idx]
    
    def g(i, x):
        return dp[i-1] + poww(x - pos[i] + 1)
    
    def f(i, j):
        l, r = 0, MAXN - 1
        while l <= r:
            m = (l + r) // 2
            if g(i, m) > g(j, m):
                r = m - 1
            else:
                l = m + 1
        return r
    
    for x in range(1, n + 1):
        a = sequence[x - 1]  
        
        pos[x] = cnt[a]
        cnt[a] += 1
        
        while (len(buf[a]) >= 2 and 
               f(buf[a][-2], buf[a][-1]) <= f(buf[a][-1], x)):
            buf[a].pop()
        
        buf[a].append(x)
        
        while (len(buf[a]) >= 2 and 
               g(buf[a][-2], pos[x]) >= g(buf[a][-1], pos[x])):
            buf[a].pop()
        
        dp[x] = g(buf[a][-1], pos[x])
    
    print("RESULT:")
    print("-" * 8)
    print(f"Maximum score: {dp[n]:.10f}")
    

if __name__ == "__main__":
    main()
