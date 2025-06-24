print("=== Chili Pepper Spiciness Calculator ===")
print("Available peppers: Poblano, Mirasol, Serrano, Cayenne, Thai, Habanero")
print()

n = int(input("How many peppers will you add? "))

pepper_shu = {
    "poblano": 1500,
    "mirasol": 6000,
    "serrano": 15500,
    "cayenne": 40000,
    "thai": 75000,
    "habanero": 125000
}

total_spiciness = 0

for i in range(n):
    pepper_name = input(f"Enter pepper {i+1}: ").strip().lower()
    if pepper_name in pepper_shu:
        total_spiciness += pepper_shu[pepper_name]
        print(f"Added {pepper_name.title()} ({pepper_shu[pepper_name]} SHU)")
    else:
        print(f"Warning: '{pepper_name}' not found. Skipping...")

print()
print(f"Total spiciness: {total_spiciness} SHU")
