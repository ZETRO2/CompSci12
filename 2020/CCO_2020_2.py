def query(bit, x):
    res = 0
    while x > 0:
        res += bit[x]
        x -= x & -x
    return res

def update(bit, l, x):
    assert l > 0
    while l < len(bit):
        bit[l] += x
        l += l & -l

def update_range(bit, l, r, x):
    update(bit, l, x)
    update(bit, r + 1, -x)

def main():
    print("Enter n:")
    n = int(input())

    MAXN = 200005

    d = [0] * MAXN
    a = [0] * MAXN
    cnt = [0] * MAXN
    bit = [0] * MAXN
    pos = [[] for _ in range(MAXN)]
    killed = [False] * MAXN

    print("Enter d[1] to d[n]:")
    inputs = list(map(int, input().split()))
    for x in range(1, n + 1):
        d[x] = inputs[x - 1]
        a[x] = d[x]
        pos[d[x]].append(x)
        cnt[d[x]] += 1

    a = a[:n + 1]
    a_sorted = [0] + sorted(a[1:])

    for x in range(1, n + 1):
        if a_sorted[x] < x:
            print(-1)
            return

    ans = 0
    cur = set()
    act_x = n

    for x in range(n, 0, -1):
        for v in pos[x]:
            cur.add(v)

        if d[act_x] < x:
            it = max(cur)
            while it + query(bit, it) > x:
                cur.remove(it)
                it = max(cur)

            ans += x - it - query(bit, it)
            update(bit, it, -1)
            update(bit, n, 1)
            killed[it] = True
            cur.remove(it)
        else:
            act_x -= 1
            while act_x > 0 and killed[act_x]:
                act_x -= 1

    print(ans)

if __name__ == "__main__":
    main()
