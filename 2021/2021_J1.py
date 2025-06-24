def calculate_boiling_water():
    
    print("=" * 50)
    print("BOILING WATER ATMOSPHERIC PRESSURE CALCULATOR")
    print("=" * 50)
    print()
    print("This program calculates atmospheric pressure based on the")
    print("temperature at which water begins to boil.")
    print()
    print("Formula used: P = 5 × B - 400")
    print("Where:")
    print("  P = Atmospheric pressure (kPa)")
    print("  B = Boiling temperature (°C)")
    print()
    print("The program will also tell you if you are:")
    print("  • Below sea level (pressure > 100 kPa)")
    print("  • At sea level (pressure = 100 kPa)")
    print("  • Above sea level (pressure < 100 kPa)")
    print()
    print("-" * 50)
    
    while True:
        try:
            print("\nPlease enter the temperature at which water begins to boil.")
            print("(Must be between 80°C and 200°C)")
            
            boiling_temp = input("\nBoiling temperature in °C: ")
            
            boiling_temp = int(boiling_temp)
            
            if boiling_temp < 80 or boiling_temp > 200:
                print(f"\nError: Temperature must be between 80°C and 200°C.")
                print(f"You entered: {boiling_temp}°C")
                continue
            
            atmospheric_pressure = 5 * boiling_temp - 400
            
            if atmospheric_pressure > 100:
                elevation_code = -1
                elevation_description = "below sea level"
            elif atmospheric_pressure == 100:
                elevation_code = 0
                elevation_description = "at sea level"
            else:
                elevation_code = 1
                elevation_description = "above sea level"
            
            print("\n" + "=" * 30)
            print("RESULTS:")
            print("=" * 30)
            print(f"Boiling temperature: {boiling_temp}°C")
            print(f"Atmospheric pressure: {atmospheric_pressure} kPa")
            print(f"Elevation status: You are {elevation_description}")
            print()
            print("Output format (as required):")
            print(f"{atmospheric_pressure}")
            print(f"{elevation_code}")
            
            break
            
        except ValueError:
            print("\nError: Please enter a valid integer number.")
            print("Example: 99, 102, 150")
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user.")
            return
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

def main():
    """Main function to run the boiling water calculator."""
    try:
        calculate_boiling_water()
        
        while True:
            print("\n" + "-" * 50)
            choice = input("Would you like to calculate another temperature? (y/n): ").lower().strip()
            
            if choice in ['y', 'yes']:
                calculate_boiling_water()
            elif choice in ['n', 'no']:
                print("\nThank you for using the Boiling Water Calculator!")
                print("Goodbye!")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
                
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")

if __name__ == "__main__":
    main()
