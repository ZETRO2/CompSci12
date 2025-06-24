print("Enter the value of P (the threshold number of people):")
P = int(input())
print("Enter the number of people who have the disease on Day 0 (N):")
N = int(input())
print("Enter the value of R (number of people each infected person infects the next day):")
R = int(input())

total_infected = N
new_infected = N
day = 0

while total_infected <= P:
    day += 1
    new_infected = new_infected * R
    total_infected += new_infected

print(day)
