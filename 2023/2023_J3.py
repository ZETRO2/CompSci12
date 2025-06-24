print("=== Special Event Scheduler ===")
print("Enter availability for each person (Y = available, . = not available)")
print("Format: Day1 Day2 Day3 Day4 Day5 (e.g., YY.Y.)")
print()

n = int(input("How many people are interested? "))

day_counts = [0, 0, 0, 0, 0] 

for i in range(n):
    availability = input(f"Person {i+1} availability: ").strip()
    
    for day in range(5):
        if day < len(availability) and availability[day] == 'Y':
            day_counts[day] += 1

max_attendees = max(day_counts)

best_days = []
for day in range(5):
    if day_counts[day] == max_attendees:
        best_days.append(day + 1) 

print()
print(f"Attendance by day: {day_counts}")
print(f"Maximum attendance: {max_attendees}")

if len(best_days) == 1:
    print(f"Best day to schedule: Day {best_days[0]}")
    print(best_days[0])
else:
    print(f"Best days to schedule: {best_days}")
    print(','.join(map(str, best_days)))
