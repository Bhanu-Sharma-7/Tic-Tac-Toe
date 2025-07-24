class TicTacToe:
    def __init__(self):
        """Initialize the game board and set starting player"""
        self.board = [str(i) for i in range(1, 10)]  # Positions 1-9
        self.current_player = "X"  # X starts first
        self.winning_combinations = [
            (0, 1, 2),  # Top row
            (3, 4, 5),  # Middle row
            (6, 7, 8),  # Bottom row
            (0, 3, 6),  # Left column
            (1, 4, 7),  # Middle column
            (2, 5, 8),  # Right column
            (0, 4, 8),  # Diagonal top-left to bottom-right
            (2, 4, 6),  # Diagonal top-right to bottom-left
        ]

    def display_board(self):
        """Display the current game board with borders"""
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")
        print("\n")

    def make_move(self, position):
        """Make a move on the board"""
        # Convert to 0-based index and validate
        pos = position - 1
        if not (0 <= pos < 9):
            raise ValueError("Invalid position! Please choose between 1-9.")
        if self.board[pos] in ("X", "O"):
            raise ValueError("Position already taken! Choose another spot.")
        
        self.board[pos] = self.current_player

    def check_winner(self):
        """Check if current player has won"""
        for a, b, c in self.winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] == self.current_player:
                return True
        return False

    def is_board_full(self):
        """Check if the board is full (tie game)"""
        return all(cell in ("X", "O") for cell in self.board)

    def switch_player(self):
        """Switch to the other player"""
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        """Main game loop"""
        print("\n🌟 Welcome to Tic Tac Toe! 🌟")
        print("Player 1: X\nPlayer 2: O\n")
        
        while True:
            self.display_board()
            
            try:
                position = int(input(f"Player {self.current_player}'s turn - Enter position (1-9): "))
                self.make_move(position)
                
                if self.check_winner():
                    self.display_board()
                    print(f"🎉 Player {self.current_player} wins! 🎉")
                    break
                    
                if self.is_board_full():
                    self.display_board()
                    print("🤝 It's a tie! 🤝")
                    break
                    
                self.switch_player()
                
            except ValueError as e:
                print(f"\n⚠️ Error: {e} Please try again.\n")
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Thanks for playing!")
                break

if __name__ == "__main__":
    game = TicTacToe()
    game.play()