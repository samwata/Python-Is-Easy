from termcolor import colored, cprint
import os
import sys


def create_empty_board():
    return [[" " for _ in range(7)] for _ in range(7)]


def draw_board(current_field):
    for row in range(13):
        if row % 2 == 0:
            practical_row = int(row / 2)
            for column in range(13):
                if column % 2 == 0:
                    practical_column = int(column / 2)
                    color = "green"
                    if current_field[practical_column][practical_row] == "X":
                        color = "red"
                    elif current_field[practical_column][practical_row] == "O":
                        color = "yellow"
                    tile = colored(
                        current_field[practical_column][practical_row],
                        color,
                        attrs=["bold"],
                    )
                    if column != 12:
                        print(tile, end="")
                    else:
                        print(tile)
                else:
                    print("|", end="")
        else:
            print("-------------")
    print("\n")


def update_board(current_field, num, player):
    column = current_field[num]
    placed = False
    reversed_column = column[::-1]
    for idx, row in enumerate(reversed_column):
        if row == " ":
            reversed_column[idx] = "X" if player == 1 else "O"
            placed = True
            break
    if not placed:
        return False
    column = reversed_column[::-1]
    current_field[num] = column
    draw_board(current_field)
    return True


def is_board_full(current_field):
    for column in current_field:
        if " " in column:
            return False
    return True


def check_four_in_row(current_field):
    for column in current_field:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i - 1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                return column[i - 1]
    return False


def check_four_in_column(column_matrix):
    for column in column_matrix:
        counter = 0
        length = len(column)
        for i in range(1, length):
            if column[i - 1] != " " and column[i] != " " and column[i - 1] == column[i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                return column[i - 1]
    return False


def check_four_in_forward_diagonal(column_matrix, player):
    for i in range(len(column_matrix)):
        for j in range(len(column_matrix[i])):
            if j - 3 < 0:
                continue
            try:
                if (
                    column_matrix[i][j] == player
                    and column_matrix[i + 1][j - 1] == player
                    and column_matrix[i + 2][j - 2] == player
                    and column_matrix[i + 3][j - 3] == player
                ):
                    return True
            except IndexError:
                continue
    return False


def check_four_in_backward_diagonal(column_matrix, player):
    for i in range(len(column_matrix)):
        for j in range(len(column_matrix[i])):
            try:
                if (
                    column_matrix[i][j] == player
                    and column_matrix[i + 1][j + 1] == player
                    and column_matrix[i + 2][j + 2] == player
                    and column_matrix[i + 3][j + 3] == player
                ):
                    return True
            except IndexError:
                continue
    return False


def is_valid_move(column_number):
    return 1 <= column_number <= 7


def create_column_matrix(current_field):
    column_matrix = [[" " for _ in range(7)] for _ in range(7)]
    for i in range(7):
        for j in range(len(current_field[i])):
            column_matrix[j][i] = current_field[i][j]
    return column_matrix


def start_connect4():
    current_field = create_empty_board()
    player = 1
    no_win = True
    winner = ""

    print("Starting new game!\n")
    draw_board(current_field)

    while no_win:
        ask_column = colored(
            "Player " + str(player) + " turn, input column number:\n",
            "green",
            attrs=["bold"],
        )
        column_input = input(ask_column)

        if not column_input:
            cprint("Please input correct move.\n", "red", attrs=["bold"])
            continue

        try:
            column_number = int(column_input)
        except ValueError:
            cprint("Please input a number between 1 and 7.\n", "red", attrs=["bold"])
            continue

        if not is_valid_move(column_number):
            cprint("Please input correct move.\n", "red", attrs=["bold"])
            continue

        updated_flag = update_board(current_field, column_number - 1, player)
        if not updated_flag:
            cprint("That column is full. Please choose another.\n", "red", attrs=["bold"])
            continue

        current_player = player
        tile = "X" if player == 1 else "O"
        player = 2 if player == 1 else 1

        winner = check_four_in_row(current_field)
        if not winner:
            column_matrix = create_column_matrix(current_field)
            winner = check_four_in_column(column_matrix)
            if not winner:
                if check_four_in_backward_diagonal(column_matrix, tile):
                    winner = current_player
                elif check_four_in_forward_diagonal(column_matrix, tile):
                    winner = current_player

        if winner:
            no_win = False
        elif is_board_full(current_field):
            cprint("It's a draw! The board is full.\n", "yellow", attrs=["bold"])
            return

    if winner == "X" or winner == 1:
        winner = "1"
    else:
        winner = "2"
    cprint("THE WINNER IS PLAYER " + str(winner), "green", attrs=["bold"])


# Start the game
start_connect4()

# worked on by samson