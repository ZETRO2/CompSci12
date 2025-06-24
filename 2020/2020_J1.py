print("Enter the number of small treats Barley received:")
S = int(input())
print("Enter the number of medium treats Barley received:")
M = int(input())
print("Enter the number of large treats Barley received:")
L = int(input())

happiness = 1 * S + 2 * M + 3 * L

if happiness >= 10:
    print("happy")
else:
    print("sad")
