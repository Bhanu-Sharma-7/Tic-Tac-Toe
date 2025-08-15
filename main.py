import random
from typing import List, Tuple, Optional

class TicTacToe:
    WINNING_LINES = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    def __init__(self, vs_ai=False):
        self.board = [str(i) for i in range(1, 10)]
        self.players = ('X', 'O')
        self.current_player = 0
        self.scores = {'X': 0, 'O': 0, 'tie': 0}
        self.vs_ai = vs_ai
        self.game_active = True

    def display_board(self):
        print(f"\nRound: {sum(self.scores.values()) + 1}")
        print(f"Scores - X: {self.scores['X']} | O: {self.scores['O']} | Ties: {self.scores['tie']}")
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6: print("---------")

    def make_move(self, pos: int):
        if 1 <= pos <= 9 and self.board[pos-1] not in self.players:
            self.board[pos-1] = self.players[self.current_player]
            return True
        return False

    def check_winner(self) -> Optional[str]:
        for a, b, c in self.WINNING_LINES:
            if self.board[a] == self.board[b] == self.board[c] in self.players:
                self.game_active = False
                return self.board[a]
        if all(cell in self.players for cell in self.board):
            self.game_active = False
            return 'tie'
        return None

    def ai_move(self):
        available = [i+1 for i, cell in enumerate(self.board) if cell not in self.players]
        return random.choice(available) if available else None

    def reset(self):
        self.board = [str(i) for i in range(1, 10)]
        self.game_active = True

    def play(self):
        print("Tic-Tac-Toe - X goes first")
        while True:
            self.display_board()
            
            if self.vs_ai and self.current_player == 1:
                move = self.ai_move()
                print(f"AI plays at position {move}")
            else:
                move = input(f"Player {self.players[self.current_player]}'s move (1-9 or 'q' to quit): ")
                if move.lower() == 'q':
                    break

            try:
                pos = int(move)
                if not self.make_move(pos):
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a number 1-9")
                continue

            if winner := self.check_winner():
                self.display_board()
                msg = "It's a tie!" if winner == 'tie' else f"Player {winner} wins!"
                print(msg)
                self.scores[winner] += 1
                
                if input("Play again? (y/n): ").lower() == 'y':
                    self.reset()
                    self.current_player = 0
                    continue
                break
            
            self.current_player = 1 - self.current_player

if __name__ == "__main__":
    game = TicTacToe(vs_ai=input("Play vs AI? (y/n): ").lower() == 'y')
    game.play()