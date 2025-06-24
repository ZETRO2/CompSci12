def solve():
    print("Enter the number of columns in the 2xN grid (N):")
    n = int(input())

    print(f"Enter {n} integers for the top row, separated by spaces:")
    top_row = list(map(int, input().split()))

    print(f"Enter {n} integers for the bottom row, separated by spaces:")
    bottom_row = list(map(int, input().split()))

    def find_max_components():
        parent = {}
        component_sum = {}
        component_size = {}

        def find(x):
            if x not in parent:
                parent[x] = x
                row, col = x
                component_sum[x] = top_row[col] if row == 0 else bottom_row[col]
                component_size[x] = 1
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def can_union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            sum_x, size_x = component_sum[px], component_size[px]
            sum_y, size_y = component_sum[py], component_size[py]
            new_sum = sum_x + sum_y
            new_size = size_x + size_y
            return (sum_x * size_y == sum_y * size_x and new_sum % new_size == 0)

        def union(x, y):
            px, py = find(x), find(y)
            if px == py or not can_union(x, y):
                return False
            if component_size[px] < component_size[py]:
                px, py = py, px
            parent[py] = px
            component_sum[px] += component_sum[py]
            component_size[px] += component_size[py]
            return True

        cells = [(0, j) for j in range(n)] + [(1, j) for j in range(n)]
        for cell in cells:
            find(cell)

        for j in range(n - 1):
            union((0, j), (0, j + 1))
            union((1, j), (1, j + 1))
        for j in range(n):
            union((0, j), (1, j))

        roots = set()
        for cell in cells:
            roots.add(find(cell))
        return len(roots)

    def solve_small():
        if n > 10:
            return find_max_components()

        max_parts = 1

        def get_neighbors(r, c):
            neighbors = []
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 2 and 0 <= nc < n:
                    neighbors.append((nr, nc))
            return neighbors

        def is_connected_component(cells):
            if len(cells) <= 1:
                return True
            cells_set = set(cells)
            visited = {next(iter(cells))}
            queue = [next(iter(cells))]
            while queue:
                r, c = queue.pop(0)
                for nr, nc in get_neighbors(r, c):
                    if (nr, nc) in cells_set and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return len(visited) == len(cells)

        def get_average(cells):
            total = 0
            for r, c in cells:
                total += top_row[c] if r == 0 else bottom_row[c]
            return total / len(cells)

        all_cells = [(i, j) for i in range(2) for j in range(n)]

        def generate_partitions(cells, index, current_partitions):
            nonlocal max_parts
            if index == len(cells):
                if len(current_partitions) <= max_parts:
                    return
                valid = True
                target_avg = None
                for partition in current_partitions:
                    if not is_connected_component(partition):
                        valid = False
                        break
                    avg = get_average(partition)
                    if target_avg is None:
                        target_avg = avg
                    elif abs(avg - target_avg) > 1e-9:
                        valid = False
                        break
                if valid:
                    max_parts = max(max_parts, len(current_partitions))
                return

            cell = cells[index]
            for i, partition in enumerate(current_partitions):
                adjacent = any(abs(cell[0] - r) + abs(cell[1] - c) == 1 for r, c in partition)
                if adjacent:
                    partition.append(cell)
                    generate_partitions(cells, index + 1, current_partitions)
                    partition.pop()
            current_partitions.append([cell])
            generate_partitions(cells, index + 1, current_partitions)
            current_partitions.pop()

        generate_partitions(all_cells, 0, [])
        return max_parts

    result = solve_small()
    print("\nMaximum number of connected components with equal average:")
    print(result)

if __name__ == "__main__":
    solve()
