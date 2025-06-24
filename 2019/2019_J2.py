# Read the number of lines in the message
L = int(input("Enter the number of lines in the message: "))

for i in range(L):
    line = input(f"Enter line {i+1} (format: N symbol): ")
    # Split the input into number and symbol
    N, symbol = line.split()
    N = int(N)
    # Print the symbol N times
    print(symbol * N)
