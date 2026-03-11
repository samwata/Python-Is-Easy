# Tic-Tac-Toe Part B


def draw_field(field):
    for row in range(5):
        if row % 2 == 0:
            practical_row = row // 2
            for column in range(5):
                if column % 2 == 0:
                    practical_column = column // 2
                    if column != 4:
                        print(field[practical_column][practical_row], end="")
                    else:
                        print(field[practical_column][practical_row])
                else:
                    print("|", end="")
        else:
            print("-----")
    print()


def check_winner(field):
    # Check rows
    for row in range(3):
        if field[0][row] != " " and field[0][row] == field[1][row] == field[2][row]:
            return field[0][row]

    # Check columns
    for col in range(3):
        if field[col][0] != " " and field[col][0] == field[col][1] == field[col][2]:
            return field[col][0]

    # Check diagonals
    if field[0][0] != " " and field[0][0] == field[1][1] == field[2][2]:
        return field[0][0]
    if field[2][0] != " " and field[2][0] == field[1][1] == field[0][2]:
        return field[2][0]

    return None


def is_board_full(field):
    for col in field:
        if " " in col:
            return False
    return True


def start_game():
    current_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 1

    print("Welcome to Tic-Tac-Toe!\n")
    print("Enter row and column as numbers 0, 1, or 2.\n")
    draw_field(current_field)

    while True:
        tile = "X" if player == 1 else "O"
        print(f"Player {player} ({tile}) turn:")

        try:
            move_row = int(input("Please enter the row (0-2): "))
            move_column = int(input("Please enter column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.\n")
            continue

        if move_row not in range(3) or move_column not in range(3):
            print("Out of range. Please enter 0, 1, or 2.\n")
            continue

        if current_field[move_column][move_row] != " ":
            print("That space is already taken. Try again.\n")
            continue

        current_field[move_column][move_row] = tile
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