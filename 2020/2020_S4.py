print("Enter the seating arrangement (A, B, and C only):")
S = input().strip()
N = len(S)

countA = S.count('A')
countB = S.count('B')
countC = S.count('C')

S2 = S + S

prefixA = [0] * (2 * N + 1)
prefixB = [0] * (2 * N + 1)
prefixC = [0] * (2 * N + 1)
for i in range(1, 2 * N + 1):
    prefixA[i] = prefixA[i-1] + (1 if S2[i-1] == 'A' else 0)
    prefixB[i] = prefixB[i-1] + (1 if S2[i-1] == 'B' else 0)
    prefixC[i] = prefixC[i-1] + (1 if S2[i-1] == 'C' else 0)

min_swaps = N

for startA in range(N):
    endA = startA + countA
    endB = endA + countB
    numA_in_A = prefixA[endA] - prefixA[startA]
    numB_in_A = prefixB[endA] - prefixB[startA]
    numC_in_A = prefixC[endA] - prefixC[startA]

    numA_in_B = prefixA[endB] - prefixA[endA]
    numB_in_B = prefixB[endB] - prefixB[endA]
    numC_in_B = prefixC[endB] - prefixC[endA]

    swaps_AB = min(numA_in_B, numB_in_A)
    leftA_in_B = numA_in_B - swaps_AB
    leftB_in_A = numB_in_A - swaps_AB

    numC_in_C = countC - (prefixC[endB] - prefixC[startA])
    numA_in_C = countA - (numA_in_A + numA_in_B)
    numB_in_C = countB - (numB_in_A + numB_in_B)

    swaps_AC = min(numA_in_C, numC_in_A)
    leftA_in_C = numA_in_C - swaps_AC
    leftC_in_A = numC_in_A - swaps_AC

    swaps_BC = min(numB_in_C, numC_in_B)
    leftB_in_C = numB_in_C - swaps_BC
    leftC_in_B = numC_in_B - swaps_BC

    leftovers = leftA_in_B + leftB_in_A + leftA_in_C + leftC_in_A + leftB_in_C + leftC_in_B
    total_swaps = swaps_AB + swaps_AC + swaps_BC + (2 * leftovers) // 3

    if total_swaps < min_swaps:
        min_swaps = total_swaps

print(min_swaps)
