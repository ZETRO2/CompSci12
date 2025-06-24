print("Enter the text T (uppercase letters only):")
T = input().strip()
print("Enter the string S (uppercase letters only):")
S = input().strip()

cyclic_shifts = []
for i in range(len(S)):
    shift = S[i:] + S[:i]
    cyclic_shifts.append(shift)

found = False
for shift in cyclic_shifts:
    if shift in T:
        found = True
        break

if found:
    print("yes")
else:
    print("no")
