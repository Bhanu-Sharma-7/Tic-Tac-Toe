"""
Tic-Tac-Toe Game Implementation
Features:
- Object-oriented design with clear separation of concerns
- Type hints for better code clarity
- Comprehensive input validation
- Clean, professional board display
- Game state management
"""

from typing import List, Tuple, Optional
import sys

class TicTacToe:
    """A professional implementation of Tic-Tac-Toe with modern Python features."""
    
    WINNING_COMBINATIONS: List[Tuple[int, int, int]] = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    PLAYER_SYMBOLS = ("X", "O")
    BOARD_SIZE = 9

    def __init__(self) -> None:
        """Initialize a new game instance."""
        self.board: List[str] = [str(i) for i in range(1, 10)]
        self.current_player: str = self.PLAYER_SYMBOLS[0]
        self.game_over: bool = False

    def display_board(self) -> None:
        """Display the current game board with clean formatting."""
        print("\n" + "=" * 13)
        for i in range(0, self.BOARD_SIZE, 3):
            row = [f" {self.board[j]} " for j in range(i, i + 3)]
            print("|" + "|".join(row) + "|")
            if i < 6:
                print("|---+---+---|")
        print("=" * 13 + "\n")

    def validate_move(self, position: int) -> bool:
        """Validate if a move is legal."""
        return 1 <= position <= self.BOARD_SIZE and \
               self.board[position - 1] not in self.PLAYER_SYMBOLS

    def make_move(self, position: int) -> None:
        """Execute a player move with validation."""
        if not self.validate_move(position):
            raise ValueError("Invalid move. Position must be between 1-9 and unoccupied.")
        
        self.board[position - 1] = self.current_player

    def check_game_state(self) -> Optional[str]:
        """
        Check if the game has concluded.
        Returns:
            str: Winning player symbol if game won, "TIE" if tied, None otherwise
        """
        for combo in self.WINNING_COMBINATIONS:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] in self.PLAYER_SYMBOLS:
                self.game_over = True
                return self.board[a]
                
        if all(cell in self.PLAYER_SYMBOLS for cell in self.board):
            self.game_over = True
            return "TIE"
            
        return None

    def switch_player(self) -> None:
        """Alternate between players."""
        self.current_player = self.PLAYER_SYMBOLS[1] if self.current_player == self.PLAYER_SYMBOLS[0] else self.PLAYER_SYMBOLS[0]

    def reset_game(self) -> None:
        """Reset the game to its initial state."""
        self.__init__()

    def play(self) -> None:
        """Main game loop with proper state management."""
        print("\n🎮 Tic-Tac-Toe - Professional Edition")
        print("Instructions:")
        print("- Enter numbers 1-9 to make moves")
        print("- Ctrl+C to exit at any time\n")
        
        while not self.game_over:
            self.display_board()
            
            try:
                position = input(f"Player {self.current_player}'s move [1-9]: ")
                
                if position.lower() in ('exit', 'quit'):
                    print("\nGame exited.")
                    return
                    
                move = int(position)
                self.make_move(move)
                
                result = self.check_game_state()
                if result == "TIE":
                    self.display_board()
                    print("🏆 Game ended in a tie!")
                elif result:
                    self.display_board()
                    print(f"🏆 Player {result} wins!")
                else:
                    self.switch_player()
                    
            except ValueError as e:
                print(f"\n⚠️ Invalid input: {e}\n")
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Thanks for playing!")
                sys.exit(0)
                
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again == 'y':
            self.reset_game()
            self.play()

if __name__ == "__main__":
    try:
        game = TicTacToe()
        game.play()
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        sys.exit(1)