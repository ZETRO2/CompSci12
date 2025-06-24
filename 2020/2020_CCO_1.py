
def main():
    print("Enter n:")
    while True:
        try:
            n = int(input())
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print("Enter l r y:")
    while True:
        try:
            l, r, y = map(int, input().split())
            break
        except ValueError:
            print("Enter exactly three integers for l r y:")

    mp = {}
    en = {}
    pos = []

    for _ in range(n):
        print("Enter xx v h:")
        while True:
            try:
                xx, v, h = map(int, input().split())
                break
            except ValueError:
                print("Enter exactly three integers for xx v h:")

        if v == 0:
            continue

        lx = xx - (y * h) // v
        rx = xx + (y * h) // v

        if (y * h) % v == 0:
            lx += 1
            rx -= 1

        lx = max(lx, l)
        rx = min(rx, r)

        if lx > rx:
            continue

        if lx not in mp:
            mp[lx] = []
        mp[lx].append(rx + 1)

        pos.append(lx)
        pos.append(rx + 1)

    pos.append(l)
    pos.append(r + 1)
    pos = sorted(set(pos))

    ans = [0] * (n + 1)
    cur_cnt = 0

    for i in range(len(pos) - 1):
        x = pos[i]

        cur_cnt -= en.get(x, 0)

        for z in mp.get(x, []):
            cur_cnt += 1
            en[z] = en.get(z, 0) + 1

        ans[cur_cnt] += pos[i + 1] - x

    for i in range(1, n + 1):
        ans[i] += ans[i - 1]

    for val in ans:
        print(val)

if __name__ == "__main__":
    main()
