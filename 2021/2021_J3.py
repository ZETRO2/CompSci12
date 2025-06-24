def decode_secret_instructions():
    
    print("=" * 60)
    print("PROFESSOR SANTOS' SECRET INSTRUCTIONS DECODER")
    print("=" * 60)
    print()
    print("This program decodes Professor Santos' secret instructions")
    print("to help her assistant find the biofuel formula.")
    print()
    print("How the encoding works:")
    print("• Each instruction is exactly 5 digits")
    print("• First 2 digits determine direction:")
    print("  - If sum is ODD → turn LEFT")
    print("  - If sum is EVEN (not zero) → turn RIGHT") 
    print("  - If sum is ZERO → same direction as previous")
    print("• Last 3 digits = number of steps (always ≥ 100)")
    print()
    print("Input format:")
    print("• Enter instructions one per line")
    print("• End with 99999 to finish")
    print("• First instruction cannot start with 00")
    print()
    print("-" * 60)
    
    while True:
        try:
            instructions = []
            print("\nEnter the secret instructions (end with 99999):")
            print()
            
            instruction_count = 0
            while True:
                instruction = input(f"Instruction {instruction_count + 1}: ").strip()
                
                if instruction == "99999":
                    if instruction_count == 0:
                        print("Error: You must enter at least one instruction before 99999.")
                        continue
                    break
                
                if not instruction.isdigit() or len(instruction) != 5:
                    print("Error: Each instruction must be exactly 5 digits.")
                    continue
                
                if instruction_count == 0 and instruction.startswith("00"):
                    print("Error: First instruction cannot start with 00.")
                    continue
                
                instructions.append(instruction)
                instruction_count += 1
            
            if not instructions:
                print("No instructions entered!")
                continue
            
            print("\n" + "=" * 40)
            print("DECODED INSTRUCTIONS:")
            print("=" * 40)
            
            previous_direction = None
            
            for i, instruction in enumerate(instructions, 1):
                first_digit = int(instruction[0])
                second_digit = int(instruction[1])
                steps = int(instruction[2:]) 
                
                digit_sum = first_digit + second_digit
                
                if digit_sum == 0:
                    if previous_direction is None:
                        direction = "right"
                    else:
                        direction = previous_direction
                elif digit_sum % 2 == 1: 
                    direction = "left"
                else: 
                    direction = "right"
                
                print(f"Instruction {i}: {instruction}")
                print(f"  First two digits: {first_digit} + {second_digit} = {digit_sum}")
                if digit_sum == 0:
                    print(f"  Direction: {direction} (same as previous)")
                elif digit_sum % 2 == 1:
                    print(f"  Direction: {direction} (sum is odd)")
                else:
                    print(f"  Direction: {direction} (sum is even)")
                print(f"  Steps: {steps}")
                print(f"  → {direction} {steps}")
                print()
                
                previous_direction = direction
            
            print("Output format (as required):")
            previous_direction = None
            for instruction in instructions:
                first_digit = int(instruction[0])
                second_digit = int(instruction[1])
                steps = int(instruction[2:])
                digit_sum = first_digit + second_digit
                
                if digit_sum == 0:
                    if previous_direction is None:
                        direction = "right"
                    else:
                        direction = previous_direction
                elif digit_sum % 2 == 1:
                    direction = "left"
                else:
                    direction = "right"
                
                print(f"{direction} {steps}")
                previous_direction = direction
            
            break
            
        except ValueError:
            print("\nError: Please enter valid numbers only.")
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user.")
            return
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

def show_example():
    """Show the sample example from the problem."""
    print("\n" + "=" * 50)
    print("SAMPLE EXAMPLE:")
    print("=" * 50)
    
    print("\nInput:")
    print("57234")
    print("00907") 
    print("34100")
    print("99999")
    
    print("\nDecoding process:")
    print("57234: 5+7=12 (even) → right, steps=234 → right 234")
    print("00907: 0+0=0 (same as previous) → right, steps=907 → right 907") 
    print("34100: 3+4=7 (odd) → left, steps=100 → left 100")
    
    print("\nOutput:")
    print("right 234")
    print("right 907")
    print("left 100")

def main():
    try:
        while True:
            choice = input("Would you like to see the sample example first? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                show_example()
                break
            elif choice in ['n', 'no']:
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        
        decode_secret_instructions()
        
        while True:
            print("\n" + "-" * 60)
            choice = input("Would you like to decode more secret instructions? (y/n): ").lower().strip()
            
            if choice in ['y', 'yes']:
                decode_secret_instructions()
            elif choice in ['n', 'no']:
                print("\nThank you for helping Professor Santos!")
                print("The assistant can now find the secret biofuel formula!")
                print("Goodbye!")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
                
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")

if __name__ == "__main__":
    main()
