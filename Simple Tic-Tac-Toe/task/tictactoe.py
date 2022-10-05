import sys


def check_wins(player, board):
    winning_moves = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [2, 4, 6]]
    wins = 0
    for play in winning_moves:
        run = 0
        for place in play:
            if board[place] == player:
                run += 1
        if run == 3:
            wins += 1
    return wins


def game_over(board):
    if board.find("_") == -1:
        return True
    else:
        return False


def move_count(player, board):
    moves = 0
    for place in board:
        if place == player:
            moves += 1
    return moves


game_on = True
board = "_________"
player = "X"
while game_on:
    print("---------")
    print("|", board[0], board[1], board[2], "|")
    print("|", board[3], board[4], board[5], "|")
    print("|", board[6], board[7], board[8], "|")
    print("---------")
    x_wins = check_wins("X", board)
    o_wins = check_wins("O", board)
    if x_wins > 0:
        if x_wins > 1 or o_wins > 0:
            print("Impossible")
            sys.exit("Impossible")
        else:
            print("X wins")
            game_on = False
            continue
    elif o_wins > 0:
        if o_wins > 1 or x_wins > 0:
            print("Impossible")
            sys.exit("Impossible")
        else:
            print("O wins")
            game_on = False
            continue
    elif game_over(board):
        print("Draw")
        game_on = False
        continue
    else:
        noughts = move_count("O", board)
        crosses = move_count("X", board)
        fair_play = abs(noughts - crosses)
        if 2 < fair_play:
            print("Impossible")
            sys.exit("Impossible")
    two_entered = numbers_entered = coord_range = coord_valid = False
    while not(two_entered and numbers_entered and coord_range and coord_valid):
        try:
            row_string, column_string = input().split()
        except ValueError:
            print("Please enter two numbers!")
        else:
            two_entered = True
        try:
            row = int(row_string)
            column = int(column_string)
        except TypeError:
            print("You should enter numbers!")
        else:
            numbers_entered = True
        if 0 < row < 4 and 0 < column < 4:
            coord_range = True
        else:
            print("Coordinates should be from 1 to 3!")
            continue
        pos_index = (row - 1) * 3 + column - 1
        if board[pos_index] != '_':
            print("This cell is occupied! Choose another one!")
        else:
            coord_valid = True
    board_list = list(board)
    board_list[pos_index] = player
    seperator = ''
    board = seperator.join(board_list)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
