def read_rule(num):
    rule = input(f"Enter substitution rule #{num} (format: LEFT RIGHT): ").strip().split()
    return (rule[0], rule[1])

print("You will enter 3 substitution rules.")
rules = [read_rule(i+1) for i in range(3)]

print("\nNow enter the number of substitutions S, the initial sequence I, and the final sequence F.")
S_I_F = input("Enter S, I, and F separated by spaces: ").strip().split()
S = int(S_I_F[0])
I = S_I_F[1]
F = S_I_F[2]

queue = []
queue.append((I, 0, []))
visited = set()

found = False

while queue and not found:
    current, steps, path = queue.pop(0) 
    if steps == S:
        if current == F:
            print("\nSequence of substitutions:")
            for rule_num, pos, result in path:
                print(f"{rule_num} {pos} {result}")
            found = True
        continue
    if (current, steps) in visited:
        continue
    visited.add((current, steps))

    for idx, (left, right) in enumerate(rules):
        start = 0
        while True:
            pos = current.find(left, start)
            if pos == -1:
                break
            new_string = current[:pos] + right + current[pos+len(left):]
            new_path = path + [(idx+1, pos+1, new_string)]
            queue.append((new_string, steps+1, new_path))
            start = pos + 1

if not found:
    print("No valid sequence of substitutions found.")
