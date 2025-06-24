
dusa_size = int(input("Enter Dusa's starting size: "))

yobi_line = input("Enter the sizes of the Yobis, separated by spaces: ")

yobi_sizes = [int(x) for x in yobi_line.strip().split()]

for yobi in yobi_sizes:
    if yobi < dusa_size:
        dusa_size += yobi
    else:
        break 
print("Dusa's size when it runs away is:", dusa_size)
