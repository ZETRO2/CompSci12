def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

print("Welcome to Pretty Average Primes!")
T = int(input("Enter the number of test cases: "))
N_list = []
max_N = 0
for i in range(T):
    N = int(input(f"Enter value for N (test case {i+1}): "))
    N_list.append(N)
    if N > max_N:
        max_N = N

is_prime = sieve(2*max_N+10)

print("\nHere are the pairs of primes A and B such that N = (A+B)/2:\n")
for N in N_list:
    found = False
    for a in range(2, 2*N):
        b = 2*N - a
        if a > b: 
            break
        if is_prime[a] and is_prime[b]:
            print(f"{a} {b}")
            found = True
            break
    if not found:
        print("No pair found (should not happen based on problem statement).")
