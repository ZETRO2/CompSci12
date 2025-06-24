def solve_hop_chess():
    print("=== HOP CHESS GAME SOLVER ===")
    print("This program calculates the probability that Justin wins the game.")
    print()
    
    print("STEP 1: Enter the board dimensions")
    print("Format: R C (where R = number of rows, C = number of columns)")
    print("Example: 2 3 (for a 2x3 board)")
    R, C = map(int, input("Enter R C: ").split())
    print(f"Board size: {R} rows × {C} columns")
    print()
    
    print("STEP 2: Enter the board configuration")
    print("Use 'J' for Justin's pieces and 'D' for Donald's pieces")
    print(f"Enter {R} rows, each with exactly {C} characters:")
    print("Example: JJD (for row with Justin-Justin-Donald)")
    
    board = []
    for i in range(R):
        while True:
            row_input = input(f"Row {i+1}: ").strip()
            if len(row_input) == C and all(c in 'JD' for c in row_input):
                board.append(list(row_input))
                break
            else:
                print(f"Error: Please enter exactly {C} characters using only 'J' and 'D'")
    
    print("Board configuration:")
    for row in board:
        print(''.join(row))
    print()
    
    print("STEP 3: Enter the error factors")
    print("Error factor = maximum number of moves a player considers")
    print("Format: J D (Justin's error factor, then Donald's error factor)")
    print("Example: 3 1 (Justin considers up to 3 moves, Donald considers up to 1 move)")
    J, D = map(int, input("Enter J D: ").split())
    print(f"Justin's error factor: {J}")
    print(f"Donald's error factor: {D}")
    print()
    
    print("Calculating probability...")
    print()
    
    memo = {}
    
    def get_possible_moves(board, player):
        """Get all possible moves for a player"""
        moves = []
        rows, cols = len(board), len(board[0])
        
        player_positions = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == player:
                    player_positions.append((r, c))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        
        for r, c in player_positions:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '.':
                    moves.append(((r, c), (nr, nc)))
        
        return moves
    
    def make_move(board, move):
        """Make a move and return new board state"""
        (r1, c1), (r2, c2) = move
        new_board = [row[:] for row in board] 
        piece = new_board[r1][c1]
        new_board[r1][c1] = '.'
        new_board[r2][c2] = piece
        return new_board
    
    def board_to_tuple(board):
        """Convert board to hashable tuple for memoization"""
        return tuple(tuple(row) for row in board)
    
    def get_win_probability(board, is_justin_turn, justin_error, donald_error):
        """Calculate probability that Justin wins from current state"""
        board_key = (board_to_tuple(board), is_justin_turn, justin_error, donald_error)
        
        if board_key in memo:
            return memo[board_key]
        
        current_player = 'J' if is_justin_turn else 'D'
        error_factor = justin_error if is_justin_turn else donald_error
        
        possible_moves = get_possible_moves(board, current_player)
        
        if not possible_moves:
            result = 0.0 if is_justin_turn else 1.0
            memo[board_key] = result
            return result
        
        move_probabilities = []
        for move in possible_moves:
            new_board = make_move(board, move)
            prob = get_win_probability(new_board, not is_justin_turn, justin_error, donald_error)
            move_probabilities.append(prob)
        
        num_moves = len(possible_moves)
        
        if num_moves <= error_factor:
            result = sum(move_probabilities) / num_moves
        else:
            if is_justin_turn:
                move_probabilities.sort(reverse=True)
                result = sum(move_probabilities[:error_factor]) / error_factor
            else:
                move_probabilities.sort()
                result = sum(move_probabilities[:error_factor]) / error_factor
        
        memo[board_key] = result
        return result
    
    probability = get_win_probability(board, True, J, D)
    
    print("=== RESULT ===")
    print(f"Probability that Justin wins: {probability:.3f}")
    print()
    
    if probability > 0.8:
        print("Justin has a very high chance of winning!")
    elif probability > 0.6:
        print("Justin has a good chance of winning.")
    elif probability > 0.4:
        print("The game is fairly balanced.")
    elif probability > 0.2:
        print("Donald has a good chance of winning.")
    else:
        print("Donald has a very high chance of winning!")

def main():
    print("Welcome to the Hop Chess Probability Calculator!")
    print("=" * 50)
    print()
    
    while True:
        try:
            solve_hop_chess()
            print()
            again = input("Would you like to solve another game? (y/n): ").strip().lower()
            if again != 'y' and again != 'yes':
                break
            print("\n" + "=" * 50 + "\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again with valid input.")
            print()

if __name__ == "__main__":
    main()
