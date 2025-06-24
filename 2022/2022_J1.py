def calculate_leftover_cupcakes():
    print("🧁 Cupcake Party Calculator 🧁")
    print("=" * 40)
    print("This program calculates leftover cupcakes after distributing to 28 students.")
    print("Regular box = 8 cupcakes, Small box = 3 cupcakes")
    print("=" * 40)
    
    while True:
        try:
            print("\nPlease enter the number of boxes:")
            
            while True:
                try:
                    regular_boxes = int(input("Number of regular boxes (8 cupcakes each): "))
                    if regular_boxes < 0:
                        print("Please enter a non-negative number.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid integer.")
            
            while True:
                try:
                    small_boxes = int(input("Number of small boxes (3 cupcakes each): "))
                    if small_boxes < 0:
                        print("Please enter a non-negative number.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid integer.")
            
            total_cupcakes = (regular_boxes * 8) + (small_boxes * 3)
            
            students = 28
            leftover_cupcakes = total_cupcakes - students
            
            print("\n" + "=" * 40)
            print("CALCULATION RESULTS:")
            print("=" * 40)
            print(f"Regular boxes: {regular_boxes} × 8 = {regular_boxes * 8} cupcakes")
            print(f"Small boxes: {small_boxes} × 3 = {small_boxes * 3} cupcakes")
            print(f"Total cupcakes: {total_cupcakes}")
            print(f"Number of students: {students}")
            print(f"Leftover cupcakes: {leftover_cupcakes}")
            
            if leftover_cupcakes < 0:
                print(f"⚠️  Warning: You need {abs(leftover_cupcakes)} more cupcakes!")
            elif leftover_cupcakes == 0:
                print("✅ Perfect! Exactly enough cupcakes for everyone!")
            else:
                print(f"🎉 Great! You have {leftover_cupcakes} extra cupcakes!")
            
            print("\n" + "=" * 40)
            while True:
                continue_choice = input("Would you like to calculate again? (y/n): ").lower().strip()
                if continue_choice in ['y', 'yes']:
                    break
                elif continue_choice in ['n', 'no']:
                    print("\nThanks for using the Cupcake Party Calculator! 🧁")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye! 👋")
            return
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

def run_sample_tests():
    print("\n🧪 Running Sample Test Cases:")
    print("=" * 40)
    
    regular1, small1 = 2, 5
    total1 = (regular1 * 8) + (small1 * 3)
    leftover1 = total1 - 28
    print(f"Sample 1: {regular1} regular, {small1} small")
    print(f"Total: {regular1}×8 + {small1}×3 = {total1} cupcakes")
    print(f"Leftover: {total1} - 28 = {leftover1} cupcakes ✅")
    
    regular2, small2 = 2, 4
    total2 = (regular2 * 8) + (small2 * 3)
    leftover2 = total2 - 28
    print(f"\nSample 2: {regular2} regular, {small2} small")
    print(f"Total: {regular2}×8 + {small2}×3 = {total2} cupcakes")
    print(f"Leftover: {total2} - 28 = {leftover2} cupcakes ✅")

if __name__ == "__main__":
    run_sample_tests()
    
    calculate_leftover_cupcakes()
