# Initial game board (1-9 numbers represent positions)
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --------------------------
# FUNCTION: DISPLAY GAME BOARD
# --------------------------
def game_board():
    """Print the current game board with borders"""
    print(f" {board[0]} | {board[1]} | {board[2]}")  # Top row
    print("---+---+---")                              # Horizontal divider
    print(f" {board[3]} | {board[4]} | {board[5]}")  # Middle row
    print("---+---+---")                              # Horizontal divider
    print(f" {board[6]} | {board[7]} | {board[8]}")  # Bottom row

# --------------------------
# FUNCTION: PLAYER'S TURN
# --------------------------
def turns_of_player(player, pos):
    """Update board with player's symbol (X/O) at given position"""
    board[pos] = player  # Replace number with X/O

# --------------------------
# FUNCTION: WIN CHECKER
# --------------------------
def winning_function(player):
    """Check if current player has won"""
    # All possible winning combinations (rows, columns, diagonals)
    winning_condition = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Middle column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal top-left to bottom-right
        (2, 4, 6),  # Diagonal top-right to bottom-left
    ]    

    # Check each winning condition
    for a, b, c in winning_condition:
        if board[a] == board[b] == board[c] == player:
            game_board()  # Show final board
            print(f"🎉 {player} जीत गया! 🎉")  # Winner announcement
            exit(0)  # Exit game

# --------------------------
# FUNCTION: MAIN GAME LOGIC
# --------------------------
def start_game():
    """Main function to control game flow"""
    print("🌟 Tic Tac Toe में आपका स्वागत है 🌟")
    game_board()  # Show initial board
    
    player = "X"  # X starts first
    
    while True:
        # Get player input (1-9 converted to 0-8 index)
        position = int(input(f"{player} की बारी - कहाँ रखना चाहते हो (1-9): ")) - 1
        
        # Update board and check win
        turns_of_player(player, position)
        winning_function(player)
        
        # Switch player after each turn
        game_board()  # Show updated board
        player = "O" if player == "X" else "X"  # Toggle between X and O

# Start the game when script runs
if __name__ == "__main__":
    start_game()