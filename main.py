"""
Tic-Tac-Toe: The Ultimate Edition 2.0
- Gorgeous visual presentation
- Human vs Human or Human vs AI
- Robust error handling
- Scoreboard tracking
"""

from typing import List, Tuple, Optional
import sys
from time import sleep
import random

class TicTacToe:
    WINNING_LINES: List[Tuple[int, int, int]] = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    PLAYER_MARKS = ("❌", "⭕")
    COLOR_CODES = {"❌": "\033[91m", "⭕": "\033[94m", "reset": "\033[0m"}
    BOARD_SIZE = 9

    def __init__(self, vs_ai=False) -> None:
        self.board: List[str] = [str(i) for i in range(1, 10)]
        self.current_player: str = self.PLAYER_MARKS[0]
        self.game_active: bool = True
        self.round: int = 1
        self.scores = {self.PLAYER_MARKS[0]: 0, self.PLAYER_MARKS[1]: 0, "tie": 0}
        self.vs_ai = vs_ai

    def display_header(self) -> None:
        print("\n\033[1;36m" + "✨" * 25)
        print(f"✨  TIC-TAC-TOE • Round {self.round}  ✨")
        print("✨" * 25 + "\033[0m")
        print(f"\033[1;35mScore — {self.PLAYER_MARKS[0]}: {self.scores[self.PLAYER_MARKS[0]]} | "
              f"{self.PLAYER_MARKS[1]}: {self.scores[self.PLAYER_MARKS[1]]} | Ties: {self.scores['tie']}\033[0m")

    def display_board(self) -> None:
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
        return 1 <= position <= 9 and self.board[position-1] not in self.PLAYER_MARKS

    def make_move(self, position: int) -> None:
        if not self.validate_move(position):
            raise ValueError("Invalid position. Choose an unoccupied number (1-9).")
        self.board[position-1] = self.current_player

    def check_winner(self) -> Optional[str]:
        for a, b, c in self.WINNING_LINES:
            if self.board[a] == self.board[b] == self.board[c] in self.PLAYER_MARKS:
                self.game_active = False
                return self.board[a]
        if all(cell in self.PLAYER_MARKS for cell in self.board):
            self.game_active = False
            return "tie"
        return None

    def switch_player(self) -> None:
        sleep(0.5)
        self.current_player = self.PLAYER_MARKS[1] if self.current_player == self.PLAYER_MARKS[0] else self.PLAYER_MARKS[0]

    def ai_move(self) -> None:
        available_moves = [i+1 for i, cell in enumerate(self.board) if cell not in self.PLAYER_MARKS]
        self.make_move(random.choice(available_moves))

    def reset_game(self) -> None:
        self.board = [str(i) for i in range(1, 10)]
        self.current_player = self.PLAYER_MARKS[0]
        self.game_active = True
        self.round += 1

    def show_help(self) -> None:
        print("\n\033[1;35mHOW TO PLAY:")
        print("• Choose a number (1-9) for your move")
        print("• First to get 3 in a row wins")
        print("• Commands: 'help', 'exit', 'restart'\033[0m")

    def play(self) -> None:
        print("\033[2J\033[H")
        print("\033[1;35m" + "🌟" * 30)
        print("🌟   WELCOME TO TIC-TAC-TOE ULTIMATE   🌟")
        print("🌟" * 30 + "\033[0m")
        self.show_help()
        
        while True:
            try:
                while self.game_active:
                    self.display_board()
                    
                    if self.vs_ai and self.current_player == self.PLAYER_MARKS[1]:
                        print("\n\033[1;33mAI is thinking...\033[0m")
                        sleep(0.7)
                        self.ai_move()
                    else:
                        choice = input(f"\n\033[1;32mPlayer {self.current_player}'s turn [1-9]: \033[0m").strip().lower()
                        if choice in ('exit', 'quit'):
                            print("\n\033[1;33mThanks for playing! Goodbye.\033[0m")
                            sys.exit(0)
                        elif choice == 'help':
                            self.show_help()
                            continue
                        elif choice == 'restart':
                            self.reset_game()
                            continue
                        elif not choice.isdigit():
                            print("\n\033[1;31m⚠️ Enter a valid number!\033[0m")
                            continue
                        
                        self.make_move(int(choice))
                    
                    result = self.check_winner()
                    if result:
                        self.display_board()
                        if result == "tie":
                            print("\n\033[1;33m🤝 It's a tie!\033[0m")
                            self.scores["tie"] += 1
                        else:
                            print(f"\n\033[1;32m🎉 Player {result} wins! 🎉\033[0m")
                            self.scores[result] += 1
                    else:
                        self.switch_player()
                
                play_again = input("\n\033[1;36mPlay again? (y/n): \033[0m").lower()
                if play_again == 'y':
                    self.reset_game()
                    continue
                else:
                    print("\n\033[1;35mThanks for playing! 👋\033[0m")
                    break

            except ValueError as e:
                print(f"\n\033[1;31m⚠️ Error: {e}\033[0m")
            except KeyboardInterrupt:
                print("\n\033[1;33m\nGame interrupted. Goodbye!\033[0m")
                sys.exit(0)

if __name__ == "__main__":
    try:
        mode = input("Play vs AI? (y/n): ").lower() == 'y'
        TicTacToe(vs_ai=mode).play()
    except Exception as e:
        print(f"\n\033[1;31m💥 Critical error: {e}\033[0m")
        sys.exit(1)