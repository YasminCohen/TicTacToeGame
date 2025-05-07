import random

def update_board(current_selection, matrix):
    index,sign = current_selection
    row = index // NUM_COLUMNS
    col = index % NUM_COLUMNS
    matrix[row][col] = sign

def input_name_user():
    while True:
        try:
            name = input().strip()
            if not name.replace(" ","").isalpha() or not name or not len(name) in range(MIN_NAME_LENGTH, MAX_NAME_LENGTH+1) :
                raise Exception("The name is invalid,the name must be between 2-20 letters, and must not contain numbers, try again...")
            else:
                return name
        except Exception as e:
            print(e)

def input_index(current_player_name, previous_elections):
    print(f"{current_player_name}, it's your turn.")
    while True:
        try:
            input_selection = input(f"Enter a position on the board, a number between 0 and 8, (or enter 'R' to restart the game).\n")
            if input_selection == "R":
                return -1
            index = int(input_selection)
            if not index in range(9) or index in previous_elections:
                raise Exception("The index invalid,the index must be number between 0 and 8, and you cannot choose a place that is already taken, try again...")
            else:
                return index
        except Exception as e:
            print(e)

def player_registration(against_computer):
    if against_computer:
        print("Enter your name:")
        first_player = input_name_user()
        second_player = "Computer"
    else:
        print("Enter the name of the first player:")
        first_player = input_name_user()
        print("Enter the name of the second player:")
        second_player = input_name_user()

    player_sign = {}
    sign = input(f"{first_player}, choose your sign, Enter 'X' to play as X, Enter 'O' to play as O, Enter any other key if you don't want to choose a sign\n")
    if sign == "X":
        player_sign[first_player] , player_sign[second_player] = ("X","O")
    elif sign == "O":
        player_sign[first_player] , player_sign[second_player] = ("O", "X")
    else:
        sign_array = ["X", "O"]
        random.shuffle(sign_array)
        player_sign[first_player], player_sign[second_player] = (sign_array[0], sign_array[1])

    print(f"{first_player}'s sign is { player_sign[first_player]}, and {second_player}'s sign is { player_sign[second_player]}.")
    return player_sign

def print_board(matrix, previous_elections, current_selection = None):
    if current_selection:
        current_place, sign = current_selection
    else:
        current_place,sign = (-1,None)

    counter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if counter in previous_elections:
                print(f"[{previous_elections[counter]}]", end=" ")
            elif counter == current_place:
                print(f"[{sign}]", end=" ")
            else:
                print(f"[ ]", end = " ")
            counter+=1
        print()

def is_row(matrix):
    for i in range(NUM_ROWS):
        flag = True
        for j in range(1,NUM_COLUMNS):
            if matrix[i][j] is None or matrix[i][j-1] is None:
                flag = False
            elif matrix[i][j] != matrix[i][j-1]:
                flag = False
        if flag:
            return True
    return False

def is_column(matrix):
    for j in range(NUM_COLUMNS):
        flag = True
        for i in range(1,NUM_ROWS):
            if matrix[i][j] is None or matrix[i-1][j] is None:
                flag = False
            elif matrix[i][j] != matrix[i-1][j]:
                flag = False
        if flag:
            return True
    return False

def is_diagonal(matrix, direct):
    flag = True
    for i in range(1,NUM_ROWS):
        if direct == "left":
            if matrix[i][i] is None or matrix[i-1][i-1] is None:
                flag = False
            elif matrix[i][i]!= matrix[i-1][i-1]:
                flag = False
                break
        else:
            if matrix[i][NUM_ROWS-1-i] is None or matrix[i-1][NUM_ROWS-i] is None:
                flag = False
            elif matrix[i][NUM_ROWS-1-i] != matrix[i-1][NUM_ROWS-i]:
                flag = False
                break
    return flag

def play_turn(player_current, matrix, previous_elections, against_computer):

    player_name, sign = player_current
    if against_computer and player_name == "Computer":
        print(f"Board status: ")
        print_board(matrix, previous_elections)
        print()
        while True:
            index = random.randint(0, 8)
            if not index in previous_elections:
                print(f"The computer's turn, index {index} selected")
                break
    else:
        print(f"Board status: ")
        print_board(matrix, previous_elections)
        print()
        index = input_index(player_name, previous_elections)
        if index == -1:
            return "Restart"

    current_selection = (index, sign)
    previous_elections[index] = sign
    update_board(current_selection, matrix)

    if is_row(matrix) or is_column(matrix) or is_diagonal(matrix,"left") or is_diagonal(matrix,"right"):
        print_board(matrix, previous_elections, current_selection)
        print(f"The winner is {player_name}!")
        return "Winner"
    elif len(previous_elections)== BOARD_SIZE:
        print_board(matrix, previous_elections, current_selection)
        print("The situation is a draw.")
        return "Draw"
    return "Continue"

def play_game(player_sign,again_computer):
    matrix = [[None, None, None], [None, None, None], [None,None, None]]
    previous_elections = {}

    list_key = list(player_sign.keys())
    random.shuffle(list_key)
    print(f"{list_key[0]} plays first in this game")

    counter = 0
    while len(previous_elections) < BOARD_SIZE:
        if counter%2 == 0:
            player_name = list_key[0]
        else:
            player_name = list_key[1]
        flag = play_turn((player_name, player_sign[player_name]), matrix, previous_elections, again_computer)
        counter+=1
        if flag !="Continue":
            return flag
    return ""

def choose_mode_and_register():
    while True:
        try:
            choose_mode = input(f"Welcome to tic-tac-toe game!\n"
                                f"Enter 0 to play with another player, or 1 to play against the computer.\n")
            against_computer = False
            mode = int(choose_mode)
            if mode == 0:
                player_sign = player_registration(against_computer)
            elif mode == 1:
                against_computer = True
                player_sign = player_registration(against_computer)
            else:
                raise Exception("The input not valid,there are only two options, the number 0 or 1, try again...")
            return player_sign, against_computer
        except Exception as e:
            print(e)

def print_location_guide():
    print("These are the positions you can choose from on the board: ")
    matrix = [["0","1","2"],["3","4","5"],["6","7","8"]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"[{matrix[i][j]}]", end=" ")
        print()
    print()

def ask_replay_same_players():
    same_players = input("Would you like to play again with the same players? Press 'Y' for yes, or any other key to change players.\n")
    if same_players == "Y":
        return True
    return False

def start_game():
    replay_same_players = False
    player_sign = None
    again_computer = None
    while True:
        if not replay_same_players:
            player_sign, again_computer = choose_mode_and_register()
            print_location_guide()
        flag = play_game(player_sign,again_computer)
        if flag == "Restart":
            replay_same_players = ask_replay_same_players()
            continue
        replay_same_players = False
        if flag == "Winner" or flag == "Draw":
            restart = input("If you want to play again, enter Y, otherwise enter any other key.\n")
            if restart != "Y":
                break
            else:
                replay_same_players = ask_replay_same_players()

    print("Game over!")

if __name__ == '__main__':
    BOARD_SIZE = 9
    NUM_COLUMNS = 3
    NUM_ROWS = 3
    MAX_NAME_LENGTH = 20
    MIN_NAME_LENGTH = 2
    start_game()


