# Read input for Apples with instructions
apples_3pt = int(input("Enter the number of 3-point shots made by Apples: "))
apples_2pt = int(input("Enter the number of 2-point shots made by Apples: "))
apples_1pt = int(input("Enter the number of 1-point shots made by Apples: "))

# Read input for Bananas with instructions
bananas_3pt = int(input("Enter the number of 3-point shots made by Bananas: "))
bananas_2pt = int(input("Enter the number of 2-point shots made by Bananas: "))
bananas_1pt = int(input("Enter the number of 1-point shots made by Bananas: "))

# Calculate total scores
apples_score = apples_3pt * 3 + apples_2pt * 2 + apples_1pt * 1
bananas_score = bananas_3pt * 3 + bananas_2pt * 2 + bananas_1pt * 1

# Determine and print the result
if apples_score > bananas_score:
    print("A")
elif bananas_score > apples_score:
    print("B")
else:
    print("T")
