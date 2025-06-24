def solve_troublesome_keys():
    print("=== Troublesome Keys Solver ===")
    print("Enter the keys that were pressed (first line):")
    keys_pressed = input().strip()
    print("Enter the letters that were displayed (second line):")
    letters_displayed = input().strip()
    
    print(f"\nDEBUG: Keys pressed: '{keys_pressed}'")
    print(f"DEBUG: Letters displayed: '{letters_displayed}'")
    print(f"DEBUG: Keys pressed length: {len(keys_pressed)}")
    print(f"DEBUG: Letters displayed length: {len(letters_displayed)}")
    
    pressed_freq = {}
    displayed_freq = {}
    
    for c in keys_pressed:
        pressed_freq[c] = pressed_freq.get(c, 0) + 1
    
    for c in letters_displayed:
        displayed_freq[c] = displayed_freq.get(c, 0) + 1
    
    print(f"\nDEBUG: Pressed frequencies: {pressed_freq}")
    print(f"DEBUG: Displayed frequencies: {displayed_freq}")
    
    silly_key = None
    wrong_letter = None
    quiet_key = None
    
    print("\nDEBUG: Analyzing each pressed key...")
    
    for key in pressed_freq:
        times_pressed = pressed_freq[key]
        times_displayed = displayed_freq.get(key, 0)
        
        print(f"DEBUG: Key '{key}' - pressed {times_pressed} times, displayed {times_displayed} times")
        
        if times_pressed > times_displayed:
            deficit = times_pressed - times_displayed
            print(f"DEBUG: Key '{key}' has deficit of {deficit}")
            
            found_silly_match = False
            print(f"DEBUG: Looking for letters with surplus to match deficit of {deficit}...")
            for letter in displayed_freq:
                times_letter_displayed = displayed_freq[letter]
                times_letter_pressed = pressed_freq.get(letter, 0)
                
                if times_letter_displayed > times_letter_pressed:
                    surplus = times_letter_displayed - times_letter_pressed
                    print(f"DEBUG: Letter '{letter}' has surplus of {surplus}")
                    
                    if deficit == surplus:
                        silly_key = key
                        wrong_letter = letter
                        found_silly_match = True
                        print(f"DEBUG: Found match! silly_key='{key}', wrong_letter='{letter}'")
                        break
            
            if not found_silly_match and times_displayed == 0:
                print(f"DEBUG: Key '{key}' never appears in output and no surplus match - quiet key")
                if quiet_key is None:  
                    quiet_key = key
                    print(f"DEBUG: Set quiet_key = '{key}'")
                continue
            

    
    print(f"\nDEBUG: Final results:")
    print(f"DEBUG: silly_key = {silly_key}")
    print(f"DEBUG: wrong_letter = {wrong_letter}")
    print(f"DEBUG: quiet_key = {quiet_key}")
    
    print(f"\n=== OUTPUT ===")
    if silly_key and wrong_letter:
        print(f"{silly_key} {wrong_letter}")
    else:
        print("-")
    
    if quiet_key:
        print(quiet_key)
    else:
        print("-")

if __name__ == "__main__":
    solve_troublesome_keys()
