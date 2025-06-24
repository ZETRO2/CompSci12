def solve_good_groups():
    print("Good Groups Constraint Checker")
    print("=" * 32)
    
    try:
        x = int(input("Enter number of 'must be together' constraints (X): "))
        
        same_group_constraints = []
        print(f"\nEnter {x} pairs that must be in the same group:")
        for i in range(x):
            pair = input(f"Pair {i+1} (name1 name2): ").strip().split()
            if len(pair) == 2:
                same_group_constraints.append((pair[0], pair[1]))
            else:
                print("Invalid input. Please enter exactly two names separated by space.")
                return
        
        y = int(input(f"\nEnter number of 'must be separate' constraints (Y): "))
        
        separate_group_constraints = []
        print(f"\nEnter {y} pairs that must be in separate groups:")
        for i in range(y):
            pair = input(f"Pair {i+1} (name1 name2): ").strip().split()
            if len(pair) == 2:
                separate_group_constraints.append((pair[0], pair[1]))
            else:
                print("Invalid input. Please enter exactly two names separated by space.")
                return
        
        g = int(input(f"\nEnter number of groups (G): "))
        
        groups = []
        print(f"\nEnter {g} groups (each group as names separated by spaces):")
        for i in range(g):
            group_input = input(f"Group {i+1}: ").strip()
            if group_input:
                group_members = group_input.split()
                groups.append(group_members)
            else:
                groups.append([])
        
        student_to_group = {}
        for group_idx, group in enumerate(groups):
            for student in group:
                student_to_group[student] = group_idx
        
        violations = 0
        
        print(f"\nChecking constraints...")
        print("-" * 20)
        
        for student1, student2 in same_group_constraints:
            if student1 in student_to_group and student2 in student_to_group:
                if student_to_group[student1] != student_to_group[student2]:
                    violations += 1
                    print(f"VIOLATION: {student1} and {student2} must be in same group but are not")
                else:
                    print(f"OK: {student1} and {student2} are in same group")
            else:
                print(f"WARNING: One or both students ({student1}, {student2}) not found in any group")
        
        for student1, student2 in separate_group_constraints:
            if student1 in student_to_group and student2 in student_to_group:
                if student_to_group[student1] == student_to_group[student2]:
                    violations += 1
                    print(f"VIOLATION: {student1} and {student2} must be in separate groups but are together")
                else:
                    print(f"OK: {student1} and {student2} are in separate groups")
            else:
                print(f"WARNING: One or both students ({student1}, {student2}) not found in any group")
        
        print(f"\nResult: {violations} constraint(s) violated")
        return violations
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None
    except KeyboardInterrupt:
        print("\n\nExiting...")
        return None

def main():
    while True:
        result = solve_good_groups()
        
        if result is not None:
            print(f"\nFinal Answer: {result}")
        
        print("\n" + "="*50)
        again = input("Solve another problem? (y/n): ").strip().lower()
        if again not in ['y', 'yes']:
            print("Goodbye!")
            break
        print()

if __name__ == "__main__":
    main()
