"""
Tic-Tac-Toe: The Ultimate Edition
A beautifully crafted implementation with:
- Stunning visual presentation
- Intuitive gameplay
- Robust error handling
- Professional code structure
"""

from typing import List, Tuple, Optional
import sys
from time import sleep

class TicTacToe:
    """A visually stunning and professionally crafted Tic-Tac-Toe game."""
    
    # Game constants
    WINNING_LINES: List[Tuple[int, int, int]] = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    PLAYER_MARKS = ("❌", "⭕")  # Modern symbols
    COLOR_CODES = {"❌": "\033[91m", "⭕": "\033[94m", "reset": "\033[0m"}
    BOARD_SIZE = 9

    def __init__(self) -> None:
        """Initialize a fresh game session."""
        self.board: List[str] = [str(i) for i in range(1, 10)]
        self.current_player: str = self.PLAYER_MARKS[0]
        self.game_active: bool = True
        self.round: int = 1

    def display_header(self) -> None:
        """Show the beautiful game header."""
        print("\n\033[1;36m" + "✨" * 25)
        print(f"✨  TIC-TAC-TOE • Round {self.round}  ✨")
        print("✨" * 25 + "\033[0m")

    def display_board(self) -> None:
        """Render the game board with artistic flair."""
        self.display_header()
        
        print("\033[1;37m" + "╔═══╦═══╦═══╗")
        for i in range(0, 9, 3):
            row = []
            for j in range(3):
                cell = self.board[i+j]
                if cell in self.PLAYER_MARKS:
                    row.append(f"{self.COLOR_CODES[cell]}{cell}{self.COLOR_CODES['reset']}")
                else:
                    row.append(f"\033[1;37m{cell}\033[0m")
            
            print("║ " + " ║ ".join(row) + " ║")
            if i < 6:
                print("╠═══╬═══╬═══╣")
        print("╚═══╩═══╩═══╝\033[0m")

    def validate_move(self, position: int) -> bool:
        """Check if move is valid."""
        return 1 <= position <= 9 and self.board[position-1] not in self.PLAYER_MARKS

    def make_move(self, position: int) -> None:
        """Process player move with validation."""
        if not self.validate_move(position):
            raise ValueError("Invalid position. Choose an unoccupied number (1-9).")
        
        self.board[position-1] = self.current_player

    def check_winner(self) -> Optional[str]:
        """Determine if there's a winner or tie."""
        for line in self.WINNING_LINES:
            a, b, c = line
            if self.board[a] == self.board[b] == self.board[c] in self.PLAYER_MARKS:
                self.game_active = False
                return self.board[a]
        
        if all(cell in self.PLAYER_MARKS for cell in self.board):
            self.game_active = False
            return "tie"
            
        return None

    def switch_player(self) -> None:
        """Alternate between players with animation."""
        print(f"\n\033[1;33mPlayer {self.current_player} thinking...\033[0m")
        sleep(0.7)
        self.current_player = self.PLAYER_MARKS[1] if self.current_player == self.PLAYER_MARKS[0] else self.PLAYER_MARKS[0]

    def reset_game(self) -> None:
        """Prepare a fresh game board."""
        self.board = [str(i) for i in range(1, 10)]
        self.current_player = self.PLAYER_MARKS[0]
        self.game_active = True
        self.round += 1

    def show_help(self) -> None:
        """Display helpful instructions."""
        print("\n\033[1;35mHOW TO PLAY:")
        print("• Choose a number (1-9) corresponding to board position")
        print("• First to get 3 in a row wins")
        print("• Commands: 'help', 'exit', 'restart'\033[0m")

    def play(self) -> None:
        """Main game loop with elegant presentation."""
        print("\033[2J\033[H")  # Clear screen
        print("\033[1;35m" + "🌟" * 30)
        print("🌟      WELCOME TO TIC-TAC-TOE      🌟")
        print("🌟" * 30 + "\033[0m")
        self.show_help()
        
        while True:
            try:
                if not self.game_active:
                    break
                    
                self.display_board()
                
                choice = input(f"\n\033[1;32mPlayer {self.current_player}'s turn [1-9]: \033[0m").strip().lower()
                
                if choice in ('exit', 'quit'):
                    print("\n\033[1;33mThanks for playing! Goodbye.\033[0m")
                    sys.exit(0)
                elif choice == 'help':
                    self.show_help()
                    continue
                elif choice == 'restart':
                    self.reset_game()
                    print("\n\033[1;36mGame restarted!\033[0m")
                    continue
                
                position = int(choice)
                self.make_move(position)
                
                result = self.check_winner()
                if result == "tie":
                    self.display_board()
                    print("\n\033[1;33m🤝 It's a tie! Well played both!\033[0m")
                elif result:
                    self.display_board()
                    print(f"\n\033[1;32m🎉 Player {result} wins! Congratulations!\033[0m")
                else:
                    self.switch_player()
                    
            except ValueError as e:
                print(f"\n\033[1;31m⚠️ Error: {e}\033[0m")
            except KeyboardInterrupt:
                print("\n\033[1;33m\nGame interrupted. Thanks for playing!\033[0m")
                sys.exit(0)
                
            sleep(0.5)
        
        play_again = input("\n\033[1;36mPlay again? (y/n): \033[0m").lower()
        if play_again == 'y':
            self.reset_game()
            self.play()
        else:
            print("\n\033[1;35mThanks for playing! Until next time! 👋\033[0m")

if __name__ == "__main__":
    try:
        game = TicTacToe()
        game.play()
    except Exception as e:
        print(f"\n\033[1;31m💥 Critical error: {e}\033[0m")
        sys.exit(1)