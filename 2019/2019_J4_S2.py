print("Welcome to the Flipper Simulator!")
print("Enter a sequence of flips (H for horizontal, V for vertical). Example: HV")

flips = input("Enter the sequence of flips: ").strip().upper()

grid = [
    [1, 2],
    [3, 4]
]

# Apply each flip in the sequence
for flip in flips:
    if flip == 'H':
        # Horizontal flip: swap top and bottom rows
        grid[0], grid[1] = grid[1], grid[0]
    elif flip == 'V':
        # Vertical flip: swap left and right columns in each row
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]
    else:
        print(f"Warning: Ignoring invalid character '{flip}'.")

print("Final grid:")
print(f"{grid[0][0]} {grid[0][1]}")
print(f"{grid[1][0]} {grid[1][1]}")
