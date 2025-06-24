print("Enter the number of observations (N):")
N = int(input())
observations = []

print("Enter each observation as 'T X' (time and position):")
for _ in range(N):
    t, x = map(int, input().split())
    observations.append((t, x))

observations.sort()

max_speed = 0.0

for i in range(N):
    for j in range(i + 1, N):
        t1, x1 = observations[i]
        t2, x2 = observations[j]
        speed = abs(x2 - x1) / abs(t2 - t1)
        if speed > max_speed:
            max_speed = speed

print(f"{max_speed:.1f}")
