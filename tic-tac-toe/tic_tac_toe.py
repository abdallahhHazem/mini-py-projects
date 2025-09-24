def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 12)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check cols
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diag

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for col in range(3)] for row in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn")

        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))

            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue

            board[row][col] = players[current_player]

            if check_winner(board, players[current_player]):
                print_board(board)
                print(f" Player {players[current_player]} wins!")
                break

            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch player
            current_player = 1 - current_player

        except (ValueError, IndexError):
            print("Invalid input. Please enter row and col as 0, 1, or 2.")


if __name__ == "__main__":
    tic_tac_toe()
