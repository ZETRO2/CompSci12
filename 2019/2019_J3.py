# Read the number of lines to process
N = int(input("Enter the number of lines to encode: "))

for i in range(N):
    # Prompt the user for each line of input
    line = input(f"Enter line {i+1}: ")
    if not line:
        print()  # Print empty line if input is empty
        continue

    result = []
    count = 1
    prev_char = line[0]

    # Loop through the line, starting from the second character
    for char in line[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(f"{count} {prev_char}")
            count = 1
            prev_char = char
    result.append(f"{count} {prev_char}")

    print(' '.join(result))
