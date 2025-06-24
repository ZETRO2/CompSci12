print("Enter the number of drops of paint (N):")
N = int(input())
points = []

print("Enter each drop's coordinates as X,Y (no spaces):")
for i in range(N):
    x_str, y_str = input(f"Drop {i+1}: ").split(',')
    x, y = int(x_str), int(y_str)
    points.append((x, y))

min_x = min(x for x, y in points)
max_x = max(x for x, y in points)
min_y = min(y for x, y in points)
max_y = max(y for x, y in points)

frame_bottom_left = (min_x - 1, min_y - 1)
frame_top_right = (max_x + 1, max_y + 1)

frame_bottom_left = (max(0, frame_bottom_left[0]), max(0, frame_bottom_left[1]))
frame_top_right = (min(100, frame_top_right[0]), min(100, frame_top_right[1]))

print(f"{frame_bottom_left[0]},{frame_bottom_left[1]}")
print(f"{frame_top_right[0]},{frame_top_right[1]}")
