print("Enter the number of rows (M):")
M = int(input())
print("Enter the number of columns (N):")
N = int(input())

print("Enter the grid, one row per line, with values separated by spaces:")
grid = []
for i in range(M):
    row = list(map(int, input().split()))
    grid.append(row)

queue = []
visited = []
queue.append((0, 0))
visited.append((0, 0))
found = False

while queue:
    r, c = queue.pop(0)
    value = grid[r][c]
    for a in range(1, int(value ** 0.5) + 1):
        if value % a == 0:
            b = value // a
            positions = [(a - 1, b - 1), (b - 1, a - 1)]
            for nr, nc in positions:
                if 0 <= nr < M and 0 <= nc < N and (nr, nc) not in visited:
                    if nr == M - 1 and nc == N - 1:
                        found = True
                        break
                    queue.append((nr, nc))
                    visited.append((nr, nc))
        if found:
            break
    if found:
        break

if found or (M - 1, N - 1) in visited:
    print("yes")
else:
    print("no")
