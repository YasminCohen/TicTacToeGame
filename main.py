import random

LEN_MIX_DRIX_CHECKERED = 9

def update_matrix(index,matrix,sign):
    match index:
        case 0:
            matrix[0][0] = sign
        case 1:
            matrix[0][1] = sign
        case 2:
            matrix[0][2] = sign
        case 3:
            matrix[1][0] = sign
        case 4:
            matrix[1][1] = sign
        case 5:
            matrix[1][2] = sign
        case 6:
            matrix[2][0] = sign
        case 7:
            matrix[2][1] = sign
        case 8:
            matrix[2][2] = sign
        case _:
            raise Exception("The index not valid, try again")

def input_name_user():
    while True:
        try:
            name = input("Enter your name: ").strip()
            if not name.replace(" ","").isalpha() or not name or len(name)>20:
                raise Exception("The name not valid, try again...")
            else:
                return name
        except Exception as e:
            print(e)

def player_registration(again_computer):
    first_player = input_name_user()
    if again_computer:
        second_player = "Computer"
    else:
        second_player = input_name_user()
    sign_array = ["X","O"]
    random.shuffle(sign_array)
    sign_of_first = sign_array[0]
    sign_of_second = sign_array[1]
    input_sign = input(f"{first_player}, choose your sign:\n"
                       f"- Enter 'X' to play as X\n"
                       f"- Enter 'O' to play as O\n"
                       f"- Enter 'E' to let us pick one for you\n")
    if input_sign == "X":
        sign_of_first = "X"
        sign_of_second = "O"
    elif input_sign == "O":
        sign_of_first = "O"
        sign_of_second = "X"
    player_sign = {
        first_player : sign_of_first,
        second_player : sign_of_second
    }
    return player_sign

def print_board(matrix, previous_elections, current_selection = None):
    counter = 0
    if current_selection:
        current_place, sign = current_selection
    else:
        current_place =-1
        sign = None
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

def input_index_user(player_current, previous_elections):
    while True:
        try:
            input_selection = input(f"{player_current} Enter a position on the board from 0-9: ")
            guess = int(input_selection)
            if guess <0 or guess >8 or guess in previous_elections:
                raise Exception("The guess not valid, try again...")
            else:
                return guess
        except Exception as e:
            print(e)

def put_sign(player_current,player_sign, matrix, previous_elections,again_computer):
    print(f"{player_current}'s turn: ")
    print()
    print_board(matrix, previous_elections)
    if again_computer and player_current == "Computer":
        while True:
            place_on_board = random_place()
            if not place_on_board in previous_elections:
                print(f"The comuter choose the place : {place_on_board} ")
                break
    else:
        place_on_board = input_index_user(player_current, previous_elections)
    name_player = player_current
    sign = player_sign[name_player]
    current_selection = (place_on_board,sign)
    print_board(matrix, previous_elections,current_selection)
    previous_elections[place_on_board] = sign
    update_matrix(place_on_board, matrix, sign)
    if row_check(matrix) or column_check(matrix) or diagonal_check(matrix):
        print(row_check(matrix))
        print(column_check(matrix))
        print(diagonal_check(matrix))
        print(f"The winner is {name_player}!")
        return True
    elif len(previous_elections)== len(matrix)*len(matrix[0]):
        print("The situation is a draw.")
        return True
    return False

def row_check(matrix):
    for i in range(len(matrix)):
        flag = True
        for j in range(1,len(matrix[0])):
            if matrix[i][j] != matrix[i][j-1]:
                flag = False
        if flag:
            return True
    return False

def column_check(matrix):
    for j in range(len(matrix[0])):
        flag = True
        for i in range(1,len(matrix)):
            if matrix[i][j] != matrix[i-1][j]:
                flag = False
        if flag:
            return True
    return False

def diagonal_check(matrix):
    flag = True
    for i in range(1,len(matrix)):
        if matrix[i][i]!= matrix[i-1][i-1]:
            flag = False
            break
    if flag:
        return True
    flag = True
    for i in range(1, len(matrix)):
        if matrix[i][len(matrix)-1-i] != matrix[i-1][len(matrix)-i]:
            flag = False
            break
    if flag:
        return True
    return False

def play_game(player_sign,again_computer):
    print("Welcome to the game, the positions on the board are as follows:")
    matrix = [["0","1","2"],["3","4","5"],["6","7","8"]]
    print_matrix(matrix)
    previous_elections = {}
    list_key = list(player_sign.keys())
    counter = 0
    while len(previous_elections) < LEN_MIX_DRIX_CHECKERED:
        if counter%2 == 0:
            player_current = list_key[0]
        else:
            player_current = list_key[1]
        win_or_draw = put_sign(player_current,player_sign,matrix,previous_elections,again_computer)
        counter+=1
        if win_or_draw:
            return True
    return False

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
           print(f"[{matrix[i][j]}]", end=" ")
        print()
def random_place():
    number_random = random.randint(0,8)
    return number_random

def start_game():
    playing_again_comuter = input("If you want to play again computer, enter Y, otherwise enter any letter you want.")
    again_computer = False
    if playing_again_comuter!="Y":
        player_sign = player_registration(again_computer)
    else:
        again_computer = True
        player_sign = player_registration(again_computer)
    while True:
        win_or_draw = play_game(player_sign,again_computer)
        if win_or_draw:
            restart = input("If you want to play again, enter Y, otherwise enter any letter you want.")
            if restart != "Y":
                break
    print("game over!")
if __name__ == '__main__':
    start_game()


