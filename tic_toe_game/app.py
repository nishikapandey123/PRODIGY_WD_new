# Initialize the Tic Tac Toe board
board = [" " for _ in range(9)]

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(symbol):
    # Check rows, columns, and diagonals for a win
    for i in range(0, 9, 3):
        if all(board[i + j] == symbol for j in range(3)):
            return True
    for i in range(3):
        if all(board[i + j] == symbol for j in range(0, 9, 3)):
            return True
    if all(board[i] == symbol for i in [0, 4, 8]) or all(board[i] == symbol for i in [2, 4, 6]):
        return True
    return False


current_player = "X"

while True:
    display_board()
    position = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move. Try again.")
        continue

    board[position] = current_player

    if check_win(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break

    if " " not in board:
        display_board()
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"

def reset_board():
    global board
    board = [" " for _ in range(9)]


while True:
    display_board()
    position = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move. Try again.")
        continue

    board[position] = current_player

    if check_win(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "y":
            reset_board()
            continue
        else:
            print("Thanks for playing!")
            break

    if " " not in board:
        display_board()
        print("It's a draw!")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "y":
            reset_board()
            continue
        else:
            print("Thanks for playing!")
            break

    current_player = "O" if current_player == "X" else "X"
