# Tic-Tac-Toe

def draw_field(current_field):
    for row in range(5):
        if row % 2 == 0:
            actual_row = row // 2
            for column in range(5):
                if column % 2 == 0:
                    actual_col = column // 2
                    if column != 4:
                        print(current_field[actual_row][actual_col], end="")
                    else:
                        print(current_field[actual_row][actual_col])
                else:
                    print("|", end="")
        else:
            print("-----")
    print()


def check_winner(current_field):
    # Check rows
    for row in current_field:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return row[0]

    # Check columns
    for col in range(3):
        if current_field[0][col] != " " and current_field[0][col] == current_field[1][col] == current_field[2][col]:
            return current_field[0][col]

    # Check diagonals
    if current_field[0][0] != " " and current_field[0][0] == current_field[1][1] == current_field[2][2]:
        return current_field[0][0]
    if current_field[0][2] != " " and current_field[0][2] == current_field[1][1] == current_field[2][0]:
        return current_field[0][2]

    return None


def is_board_full(current_field):
    for row in current_field:
        if " " in row:
            return False
    return True


def start_game():
    current_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 1

    print("Welcome to Tic-Tac-Toe!\n")
    print("Enter row and column as numbers 0, 1, or 2.\n")
    draw_field(current_field)

    while True:
        tile = "O" if player == 1 else "X"
        print(f"Player {player} ({tile}) turn:")

        try:
            move_row = int(input("Please enter the row (0-2): "))
            move_column = int(input("Please enter the column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.\n")
            continue

        if move_row not in range(3) or move_column not in range(3):
            print("Out of range. Please enter a number between 0 and 2.\n")
            continue

        if current_field[move_row][move_column] != " ":
            print("That space is already taken. Try again.\n")
            continue

        current_field[move_row][move_column] = tile
        draw_field(current_field)

        winner = check_winner(current_field)
        if winner:
            print(f"Player {player} ({tile}) wins!\n")
            break

        if is_board_full(current_field):
            print("It's a draw!\n")
            break

        player = 2 if player == 1 else 1


# Start the game
start_game()