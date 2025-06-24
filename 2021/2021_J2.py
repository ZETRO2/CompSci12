def find_auction_winner():
    
    print("=" * 50)
    print("SILENT AUCTION WINNER FINDER")
    print("=" * 50)
    print()
    print("This program determines the winner of a silent auction.")
    print("You'll enter the number of bids, then for each bid:")
    print("  1. The bidder's name")
    print("  2. Their bid amount (in dollars)")
    print()
    print("Rules:")
    print("  • Winner has the highest bid")
    print("  • If there's a tie, the first person to bid wins")
    print("  • Bid amounts must be positive integers less than 2000")
    print()
    print("-" * 50)
    
    while True:
        try:
            print("\nHow many bids were placed at the auction?")
            num_bids = input("Number of bids (1-99): ")
            num_bids = int(num_bids)
            
            if num_bids < 1 or num_bids > 99:
                print(f"\nError: Number of bids must be between 1 and 99.")
                print(f"You entered: {num_bids}")
                continue
            
            bids = []
            
            print(f"\nNow enter the {num_bids} bid(s):")
            print("(Enter name on first line, bid amount on second line)")
            print()
            
            for i in range(num_bids):
                print(f"Bid #{i + 1}:")
                
                while True:
                    name = input(f"  Bidder's name: ").strip()
                    if name:
                        break
                    print("  Error: Name cannot be empty. Please enter a name.")
                
                while True:
                    try:
                        bid_amount = input(f"  Bid amount ($): ")
                        bid_amount = int(bid_amount)
                        
                        if bid_amount <= 0:
                            print("  Error: Bid amount must be positive.")
                            continue
                        elif bid_amount >= 2000:
                            print("  Error: Bid amount must be less than $2000.")
                            continue
                        
                        break
                        
                    except ValueError:
                        print("  Error: Please enter a valid integer for the bid amount.")
                
                bids.append((name, bid_amount, i))
                print()
            
            if not bids:
                print("No bids were placed!")
                continue
     
            bids.sort(key=lambda x: (-x[1], x[2]))
            
            winner_name = bids[0][0]
            winning_bid = bids[0][1]
            
            print("=" * 30)
            print("AUCTION RESULTS:")
            print("=" * 30)
            print(f"Winner: {winner_name}")
            print(f"Winning bid: ${winning_bid}")
            print()
            
            print("All bids (in order placed):")
            original_order_bids = sorted(bids, key=lambda x: x[2])
            for i, (name, amount, _) in enumerate(original_order_bids, 1):
                marker = " ← WINNER!" if name == winner_name and amount == winning_bid else ""
                print(f"  {i}. {name}: ${amount}{marker}")
            
            print()
            print("Output format (as required):")
            print(f"{winner_name}")
            
            break
            
        except ValueError:
            print("\nError: Please enter a valid integer number.")
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user.")
            return
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

def demo_examples():
    print("\n" + "=" * 50)
    print("SAMPLE EXAMPLES:")
    print("=" * 50)
    
    print("\nExample 1:")
    print("3 bids:")
    print("  Ahmed: $300")
    print("  Suzanne: $500") 
    print("  Ivona: $450")
    print("Winner: Suzanne (highest bid: $500)")
    
    print("\nExample 2:")
    print("2 bids:")
    print("  Ijeoma: $20")
    print("  Goor: $20")
    print("Winner: Ijeoma (tied at $20, but bid first)")

def main():
    try:
        while True:
            choice = input("Would you like to see sample examples first? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                demo_examples()
                break
            elif choice in ['n', 'no']:
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        
        find_auction_winner()
        
        while True:
            print("\n" + "-" * 50)
            choice = input("Would you like to find another auction winner? (y/n): ").lower().strip()
            
            if choice in ['y', 'yes']:
                find_auction_winner()
            elif choice in ['n', 'no']:
                print("\nThank you for using the Silent Auction Winner Finder!")
                print("Goodbye!")
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
                
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Goodbye!")

if __name__ == "__main__":
    main()
