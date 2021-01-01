

board=["-","-","-",
       "-","-","-",
       "-","-","-"]


game_is_still_going=True

winner = None

current_player = "X"



def Display_board():

        print( board[0]+"|"+ board[1] + "|" + board[2])
        print(board[3] + "|" + board[4] + "|" + board[5])
        print(board[6] + "|" + board[7] + "|" + board[8])


def  handles_turns(players):
   global  game_is_still_going

   print("It's " + players + " turn.")
   position = input("Choose a number between 1-9 :  ")#we're using this process to get the write position of the value entered by the user.
    # the user board contains a 3 x 3 metrics which makes a total 9 of i.e rows and colums .

    # The -1 subtract the value of what the user enter because list index statts from zero


   valid= False
   while not valid:
       while position not in ["1","2","3","4","5","6","7","8","9"] :#check the board list if what the user input matches with what is inside the board list.
       # and so when ever it matches, it breaks out of the while loop and the next players makes a move and the while loop repeat it self still there

       # is winner or a tie.


           position = input("Choose a number between 1-9 :  ")

       position = int(position)-1

       if board[position] == "-":
           valid=True

       else:
           print("You Can't go there.")

   board[position]= players
   Display_board()









def play_game():

     Display_board()#displays the board when the user start the game

     while game_is_still_going:
         handles_turns(current_player)# This beacuse the board state changes
         check_if_game_over()
         flip_player()


     #the game has ended
     if winner =="X"or winner=="O":
         print(winner + " won .")
     elif winner == None:
         print("iTie")



def check_if_game_over():
    check_if_player_wins()
    check_if_player_ties()



def  check_if_player_wins():

    global  winner



    #check_rows()
    row_winner =check_rows()
    #check_columns()
    colunm_winner= check_columns()
    #check_diagonals()
    diagonal_winner= check_diagonals()


    if row_winner:
        #current player wins
        winner = row_winner
    elif colunm_winner:
        #current player wins
        winner = colunm_winner
    elif diagonal_winner:
        #current player wins
        winner = diagonal_winner
    else:
        #there is a tie
        winner = None
    return

def check_rows():
    global game_is_still_going

    row_1= board[0]==board[1]==board[2] !="-"
    row_2= board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row does match , flag that there is a win and the loop stop
    if row_1 or row_2 or row_3 :
        game_is_still_going= False
#Returns the winner(X or O)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]



    return

def check_columns():

    global game_is_still_going

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_is_still_going = False
        # Returns the winner(X or O)
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]

    return

def check_diagonals():

    global  game_is_still_going

    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"


    if dia_1 or dia_2:
        game_is_still_going = False
        # Returns the winner(X or O)
    if dia_1:
        return board[0]
    if dia_2:
        return board[2]

    return



def check_if_player_ties() :
    global game_is_still_going
    if "-" not in board:
        game_is_still_going = False
    return

def  flip_player() :
    global  current_player

    if current_player=="X":

        current_player="O"
    elif current_player =="O":
        current_player="X"
    return


play_game()