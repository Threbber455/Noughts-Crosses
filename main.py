# Project 1
# Completed on the 10th July 2022 at 10:13PM.

board = {}

def player_to_string(player):
    if(player == 1):
        return "One"
    else:
        return "Two" 

def check_win(player) -> bool:
    win = False

    if(not board[1] == "-" and not board[2] == "-" and not board[3] == "-"):
        if(board[1] == board[2] and board[2] == board[3]):
            win = True

    if(not board[4] == "-" and not board[5] == "-" and not board[6] == "-"):
        if(board[4] == board[5] and board[5] == board[6]):
            win = True   

    if(not board[7] == "-" and not board[8] == "-" and not board[9] == "-"):
        if(board[7] == board[8] and board[8] == board[9]):
            win = True           
    
    if(not board[1] == "-" and not board[4] == "-" and not board[7] == "-"):
        if(board[1] == board[4] and board[4] == board[7]):
            win = True

    if(not board[2] == "-" and not board[5] == "-" and not board[8] == "-"):
        if(board[2] == board[5] and board[5] == board[8]):
            win = True        

    if(not board[3] == "-" and not board[6] == "-" and not board[9] == "-"):
        if(board[3] == board[6] and board[6] == board[9]):
            win = True            

    if(not board[1] == "-" and not board[5] == "-" and not board[9] == "-"):
        if(board[1] == board[5] and board[5] == board[9]):
            win = True        

    if(not board[3] == "-" and not board[6] == "-" and not board[9] == "-"):
        if(board[3] == board[6] and board[6] == board[9]):
            win = True

    if(not win and not board[1] == "-" and not board[2] == "-" and not board[3] == "-" and not board[4] == "-" and not board[5] == "-" and not board[6] == "-" and not board[7] == "-" and not board[8] == "-" and not board[9] == "-"):
        print_input_board(board)
        print("Nobody Wins!")
        return True     
    
    if(win):
        print_input_board(board)
        print("Player " + player_to_string(player) + " wins!")
        return True
    else:
        return False    

def turn(player) -> bool:
    if(player == 1):
        print("Player One Turn (X)")
        char = "X"
    else: 
        print("Player Two Turn (O)") 
        char = "O"
    print_input_board(board)

    user_input = input("Number: ")

    if(not isinstance(int(user_input), int) or int(user_input) > 9 or int(user_input) < 1):
        print("Please enter a number between 1-9 (inclusive).")
        turn(player)
        return False

    if(not board[int(user_input)] == "-"):
        print("Selected slot already has a nought or cross in.")
        turn(player)
        return False    

    board[int(user_input)] = char 

    if(not check_win(player)):
        if(player == 1):
            turn(2)
        else:
            turn(1)

    return True

def start() -> None:
    for i in range(1, 10):
        board[i] = "-"
    print("Player 1 -> X")
    print("Player 2 -> O")

    turn(1)

def print_input_board(given_board) -> None:
    board_string = ""
    for key in given_board:
        if(key % 3 == 0):
            if(given_board[key] == "-"):
                if(key == 9):
                    board_string += str(key)
                else:
                    board_string += str(key) + "\n"
            else:       
                if(key == 9):
                    board_string += given_board[key]
                else:  
                    board_string += given_board[key] + "\n"   
        else:
            if(given_board[key] == "-"):
                board_string += str(key) + " | "
            else:
                board_string += given_board[key] + " | "  

    print(board_string)  

start()   
