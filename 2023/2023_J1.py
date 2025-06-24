def solve_deliv_e_droid():
    print("=== Deliv-e-droid Score Calculator ===")
    print("Enter number of packages delivered:")
    packages = int(input())
    
    print("Enter number of collisions:")
    collisions = int(input())
    
    package_points = packages * 50
    collision_penalty = collisions * 10
    
    bonus = 500 if packages > collisions else 0
    
    final_score = package_points - collision_penalty + bonus
    
    print(f"\nCalculation:")
    print(f"Packages delivered: {packages} × 50 = {package_points} points")
    print(f"Collisions: {collisions} × 10 = -{collision_penalty} points")
    if bonus > 0:
        print(f"Bonus (packages > collisions): +{bonus} points")
    else:
        print("No bonus (packages ≤ collisions)")
    
    print(f"\nFinal score: {package_points} - {collision_penalty} + {bonus} = {final_score}")
    
    return final_score

print("Sample Input 1: 5 packages, 2 collisions")
print("Expected Output: 730")
print()

print("Sample Input 2: 0 packages, 10 collisions") 
print("Expected Output: -100")
print()

print("Run the calculator:")
result = solve_deliv_e_droid()
print(f"\nResult: {result}")
