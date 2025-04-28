import random


def player_registration():
    first_player = input("Enter your name.")
    second_player = input("Enter your name.")
    sign_array = ["X","O"]
    random.shuffle(sign_array)
    sign_of_first = sign_array[0]
    sign_of_second = sign_array[1]
    input_sign = input(f"{first_player} If you want your sign to be an X, "
                          f"enter an X, if you want a circle, enter an O, "
                          f"if you don't want to choose, enter an E.")
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
        print(f"current_place: {current_place},sign: {sign} ")
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

def put_sign(player_sign, matrix, previous_elections):
    print_board(matrix, previous_elections)
    input_selection = input("Enter a position on the board from 0-9, and write your name, in the following format: 1, yasmin")
    split_array = input_selection.split(",")
    current_selection = (int(split_array[0]),player_sign[split_array[1]])
    print(current_selection)
    print_board(matrix, previous_elections,current_selection)



if __name__ == '__main__':
   # result = player_registration()
   # print(result)
   # print_board([[0,1,2],[3,4,5],[6,7,8]], {0:"O",1: "X",2:"X"},(8,"X"))
   player_sign = {"yasmin": "X",
                  "tamar": "O"}
   put_sign(player_sign, [[0,1,2],[3,4,5],[6,7,8]], {0:"O",1: "X",2:"X"})