def parse_harp_tuning(instruction_line):
    instructions = []
    i = 0
    
    while i < len(instruction_line):
        strings = ""
        while i < len(instruction_line) and instruction_line[i].isupper():
            strings += instruction_line[i]
            i += 1
        
        if i < len(instruction_line) and instruction_line[i] in "+-":
            operation = instruction_line[i]
            i += 1
        else:
            break  
        
        turns = ""
        while i < len(instruction_line) and instruction_line[i].isdigit():
            turns += instruction_line[i]
            i += 1
        
        if strings and turns:
            action = "tighten" if operation == "+" else "loosen"
            instructions.append(f"{strings} {action} {turns}")
    
    return instructions

def main():
    print("Harp Tuning Instruction Parser")
    print("=" * 35)
    print("Enter harp tuning instructions (or 'quit' to exit)")
    print("Example: AFB+8HC-4")
    print()
    
    while True:
        try:
            user_input = input("Enter tuning instructions: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            print("\nFormatted Instructions:")
            print("-" * 22)
            instructions = parse_harp_tuning(user_input)
            
            if instructions:
                for instruction in instructions:
                    print(instruction)
            else:
                print("No valid instructions found. Please check your input format.")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Please try again with valid input.")
            print()

if __name__ == "__main__":
    main()
