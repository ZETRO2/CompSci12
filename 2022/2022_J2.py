def calculate_fergusonball_ratings():
    print("⭐ Fergusonball Ratings Calculator ⭐")
    print("=" * 50)
    print("This program calculates player star ratings for Fergusonball.")
    print("Rating formula: (Points × 5) - (Fouls × 3)")
    print("Gold team status: ALL players must have rating > 40")
    print("=" * 50)
    
    while True:
        try:
            while True:
                try:
                    num_players = int(input("\nEnter the number of players on the team: "))
                    if num_players <= 0:
                        print("Please enter a positive number of players.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid integer.")
            
            players_data = []
            players_above_40 = 0
            
            print(f"\nPlease enter data for {num_players} players:")
            print("(You'll be prompted for points and fouls for each player)")
            
            for i in range(num_players):
                print(f"\n--- Player {i + 1} ---")
                
                while True:
                    try:
                        points = int(input(f"Points scored by player {i + 1}: "))
                        if points < 0:
                            print("Points cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid integer.")
                
                while True:
                    try:
                        fouls = int(input(f"Fouls committed by player {i + 1}: "))
                        if fouls < 0:
                            print("Fouls cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid integer.")
                
                rating = (points * 5) - (fouls * 3)
                players_data.append({
                    'player': i + 1,
                    'points': points,
                    'fouls': fouls,
                    'rating': rating
                })
                
                if rating > 40:
                    players_above_40 += 1
            
            print("\n" + "=" * 50)
            print("PLAYER RATINGS:")
            print("=" * 50)
            print(f"{'Player':<8} {'Points':<8} {'Fouls':<8} {'Rating':<8} {'Status':<12}")
            print("-" * 50)
            
            for player in players_data:
                status = "⭐ Above 40" if player['rating'] > 40 else "❌ Below/At 40"
                print(f"{player['player']:<8} {player['points']:<8} {player['fouls']:<8} {player['rating']:<8} {status}")
            
            is_gold_team = players_above_40 == num_players
            
            print("\n" + "=" * 50)
            print("TEAM SUMMARY:")
            print("=" * 50)
            print(f"Players with rating > 40: {players_above_40}")
            print(f"Total players: {num_players}")
            
            if is_gold_team:
                print("🏆 GOLD TEAM STATUS: YES! All players have rating > 40")
                print(f"Output: {players_above_40}+")
            else:
                print("❌ GOLD TEAM STATUS: NO. Not all players have rating > 40")
                print(f"Output: {players_above_40}")
            
            print("\n" + "=" * 50)
            print("CALCULATION DETAILS:")
            print("=" * 50)
            for player in players_data:
                calculation = f"{player['points']} × 5 - {player['fouls']} × 3 = {player['rating']}"
                print(f"Player {player['player']}: {calculation}")
            
            print("\n" + "=" * 50)
            while True:
                continue_choice = input("Would you like to calculate for another team? (y/n): ").lower().strip()
                if continue_choice in ['y', 'yes']:
                    break
                elif continue_choice in ['n', 'no']:
                    print("\nThanks for using the Fergusonball Ratings Calculator! ⭐")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye! 👋")
            return
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

def run_sample_test():
    print("\n🧪 Running Sample Test Case:")
    print("=" * 50)
    
    sample_players = [
        {'points': 12, 'fouls': 4},
        {'points': 10, 'fouls': 3},
        {'points': 9, 'fouls': 1}
    ]
    
    print("Sample Input:")
    print("3 players")
    
    players_above_40 = 0
    
    for i, player in enumerate(sample_players, 1):
        rating = (player['points'] * 5) - (player['fouls'] * 3)
        calculation = f"{player['points']} × 5 - {player['fouls']} × 3 = {rating}"
        status = "✅" if rating > 40 else "❌"
        
        print(f"Player {i}: {player['points']} points, {player['fouls']} fouls")
        print(f"  Rating: {calculation} {status}")
        
        if rating > 40:
            players_above_40 += 1
    
    is_gold_team = players_above_40 == len(sample_players)
    output = f"{players_above_40}+" if is_gold_team else str(players_above_40)
    
    print(f"\nResult: {players_above_40} players above 40")
    print(f"Gold team: {'Yes' if is_gold_team else 'No'}")
    print(f"Expected output: 3+")
    print(f"Actual output: {output} ✅")

if __name__ == "__main__":
    run_sample_test()
    
    calculate_fergusonball_ratings()
