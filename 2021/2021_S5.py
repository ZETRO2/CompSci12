def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve_math_homework():
    print("MATH HOMEWORK PROBLEM")
    print("=====================")
    print()
    print("Enter your input as follows:")
    print("Line 1: N M (sequence_length number_of_requirements)")
    print("Next M lines: Xi Yi Zi (positions and required GCD)")
    print()
    
    n, m = map(int, input().split())
    
    requirements = []
    for i in range(m):
        xi, yi, zi = map(int, input().split())
        requirements.append((xi - 1, yi - 1, zi))
    
    result = find_valid_sequence(n, requirements)
    
    if result is None:
        print("Impossible")
    else:
        print(" ".join(map(str, result)))

def find_valid_sequence(n, requirements):
    sequence = [1] * n
    
    sorted_requirements = sorted(requirements, key=lambda x: x[2], reverse=True)
    
    for xi, yi, zi in sorted_requirements:
        if xi == yi:
            sequence[xi] = zi
        else:
            current_gcd = gcd(sequence[xi], sequence[yi])
            
            if current_gcd == zi:
                continue 

            if sequence[xi] == 1 and sequence[yi] == 1:
                sequence[xi] = zi * 2 
                sequence[yi] = zi * 3 
            elif sequence[xi] == 1:
                sequence[xi] = find_compatible_value(sequence[yi], zi)
            elif sequence[yi] == 1:
                sequence[yi] = find_compatible_value(sequence[xi], zi)
            else:
                sequence[xi] = zi * 2
                sequence[yi] = zi * 3
    
    for xi, yi, zi in requirements:
        if gcd(sequence[xi], sequence[yi]) != zi:
            return None
    
    for val in sequence:
        if val > 1000000000:
            return None
    
    return sequence

def find_compatible_value(fixed_value, target_gcd):
    
    if fixed_value % target_gcd != 0:
        return target_gcd * 2
    
    m = fixed_value // target_gcd

    for k in [2, 1, 3, 4, 5]:
        if gcd(k, m) == 1:
            return target_gcd * k
    
    return target_gcd * 2

def find_sequence_backtrack(n, requirements):

    sequence = [1] * n
    
    sorted_requirements = sorted(requirements, key=lambda x: x[2], reverse=True)
    
    for xi, yi, zi in sorted_requirements:

        if sequence[xi] == 1 and sequence[yi] == 1:
            sequence[xi] = zi
            sequence[yi] = zi
        elif sequence[xi] == 1:
            sequence[xi] = zi * (sequence[yi] // zi) if sequence[yi] % zi == 0 else zi
        elif sequence[yi] == 1:
            sequence[yi] = zi * (sequence[xi] // zi) if sequence[xi] % zi == 0 else zi
        else:
            
            current_gcd = gcd(sequence[xi], sequence[yi])
            if current_gcd != zi:

                if zi % current_gcd == 0:
                    factor = zi // current_gcd
                    sequence[xi] *= factor
                    sequence[yi] *= factor
                else:
                    sequence[xi] = zi * 2
                    sequence[yi] = zi * 3
    
    for xi, yi, zi in requirements:
        if gcd(sequence[xi], sequence[yi]) != zi:
            return try_brute_force(n, requirements)
    
    for val in sequence:
        if val > 1000000000:
            return try_brute_force(n, requirements)
    
    return sequence

def try_brute_force(n, requirements):

    if n <= 10 and len(requirements) <= 10:
        return construct_from_constraints(n, requirements)
    
    return None

def construct_from_constraints(n, requirements):

    sequence = [1] * n
    
    position_constraints = {}
    for xi, yi, zi in requirements:
        if xi not in position_constraints:
            position_constraints[xi] = []
        if yi not in position_constraints:
            position_constraints[yi] = []
        position_constraints[xi].append((yi, zi))
        position_constraints[yi].append((xi, zi))
    
    changed = True
    iterations = 0
    while changed and iterations < 100:
        changed = False
        iterations += 1
        
        for xi, yi, zi in requirements:
            current_gcd = gcd(sequence[xi], sequence[yi])
            if current_gcd != zi:
                if zi > current_gcd:
                    lcm_factor = zi // current_gcd
                    if zi % current_gcd == 0:
                        sequence[xi] *= lcm_factor
                        sequence[yi] *= lcm_factor
                        changed = True
                    else:
                        sequence[xi] = zi * (sequence[xi] // zi + 1) if sequence[xi] % zi != 0 else sequence[xi]
                        sequence[yi] = zi * (sequence[yi] // zi + 1) if sequence[yi] % zi != 0 else sequence[yi]
                        changed = True
                else:
                    sequence[xi] = zi
                    sequence[yi] = zi
                    changed = True
    
    for xi, yi, zi in requirements:
        if gcd(sequence[xi], sequence[yi]) != zi:
            return None
    
    for val in sequence:
        if val > 1000000000:
            return None
    
    return sequence

if __name__ == "__main__":
    solve_math_homework()
