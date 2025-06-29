board = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

def game_board():
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def turns_of_player(player, pos):
    board[pos] = player

def winning_function(player):
    winning_condition = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]    

    for a, b, c in winning_condition:
        if board[a] == board[b] == board[c] == "X" or board[a] == board[b] == board[c] == "O":
            print(f"{player} is winner")
            exit(0)

def start_game():
    print("Welcome to the Tic Tac Toe")
    game_board()
    player = "X"
    while True:
        position = int(input("Enter where you put your symbol: ")) - 1
        turns_of_player(player, position)
        winning_function(player)

        if player == "X":
            game_board()
            player = "O"
        elif player == "O":
            game_board()
            player = "X"

if __name__ == "__main__":
    start_game()