# 🎮 Tic Tac Toe (Python Console Game)

A simple console-based Tic Tac Toe game built using Python. Two players take turns to play as `X` and `O`, and the game announces the winner once a winning condition is met.

## 📋 Features

- Classic 3x3 Tic Tac Toe board.
- Two-player mode in the terminal.
- Automatic win detection with early game exit.
- Clean and readable code.

## 🧠 How It Works

- The game board is represented using a list of 9 elements.
- Players take turns entering the position (1-9) where they want to place their symbol (`X` or `O`).
- The board updates after each turn.
- The game checks for a winner after every move.
- Once a player wins, the game exits and prints the winner.

## 🖥️ Demo

```
Welcome to the Tic Tac Toe
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
Enter where you put your symbol: 5
 X | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
...
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Run the Game

```bash
python tic_tac_toe.py
```

## 🧾 Game Rules

- The game board has positions labeled from 1 to 9.
- Players enter the position number where they want to place their symbol.
- The first player uses `X` and the second uses `O`.
- A player wins by having 3 of their symbols in a row (horizontally, vertically, or diagonally).

## 📌 Notes

- Currently, the game does **not** handle:
  - Invalid inputs (like entering a number outside 1-9)
  - Already-filled positions
  - Draw condition (no winner and board full)

## 🙌 Author

**Bhanu Sharma**  
*A beginner Python enthusiast building fun projects!*