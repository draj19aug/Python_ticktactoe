import random
## Function

def checkerName(players):
    if players[1].upper()== players[2].upper():
        return True
    else:
        False

def parseInt(num):
    try:        
        z= int(num)
        return num
    except ValueError:
        return None

def checkOverLap(board,row,column):
    if board[row-1][column-1] == "":
        return False
    else:
        return True
        
def restartGame(board,players,whoStarted):
    initializeBoard(board)
    whoStarted=togglePlayer(whoStarted)
    print("In this game",players[whoStarted],"will start the game")
    return whoStarted

def announceResult(state,players):
    if states[state] =="Draw":
        print("Game result  in a draw")
    elif states[state]  =="Player1":
        print("Congratulation",players[1],"wins")

    elif states[state] =="Player2":
        print("Congratulation",players[2],"wins")

    playMore = int(input("Do you want to Play more - (0/1) : - "))
    return playMore

def togglePlayer(playerIngame):
    if playerInGame ==1:
        return 2
    else:
        return 1

def checkBoard(board):
    for player in range(1,3):
        if player==1:
            symbol="X"
        else:
            symbol="O"
    
        for i in range(0,3):
            if (board[i][0]==symbol) and (board[i][1]==symbol) and (board[i][2]==symbol):     
                return player+1
             
        for i in range(0,3):
         if (board[0][i]==symbol)and (board[1][i]==symbol) and (board[2][i]==symbol):     
            return player+1      
             
        
        if (board[0][0]==symbol)and (board[1][1]==symbol) and (board[2][2]==symbol):     
            return player+1 
        if (board[0][2]==symbol)and (board[1][1]==symbol) and (board[2][0]==symbol):     
            return player+1   

    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == "" :
                return 0
    return 1
        
def printBoard(board):
    cellstr=""
    print("..........")
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=="":
                cellstr=" "
            elif board[i][j]=="X":
                cellstr="X"
            else:
                cellstr="O"    
            print("|",cellstr,end="")    
        print("|")
        if i<2:
            print("__________")
    print("..........")

def playMove(board,players,tossWinnerIndex):
    print(players[tossWinnerIndex],"will take move now")
   
    ## Row checking
    while True : 
        
        while True:
         xrow =parseInt(input("Choose Row where you want to put your bet:"))
         row =int(xrow or 4) 
         if row>3:
            print(" Enter Corrct Row Number (1-3)")
            # row=int(input("Choose Row where you want to put your bet:"))
         if row<4:
            break  
        ## Row end

        ## Column Checking
        
        while True:
          xcolumn=parseInt(input("Choose Column where you want to put your bet :"))
          column =int(xcolumn or 4)
          if column>3:
            print("Enter Correct Column Number (1-3)")
            # column=int(input("Choose ciolumn where you want to put your bet:"))
          if column<4:
            break   
        ## Column end
        if(checkOverLap(board,row,column)):
            print("This cell is already occupied, pls enter diffent row/column: ")
        else:
            break


    if tossWinnerIndex==1:
     board [row-1][column-1]="X"
    else:
      board[row-1][column-1]="O"

    printBoard(board)    

def whoWillStart():
    z= random.randint(1,2)
    return z

def initializeBoard(board):
    for i in range(3):
        for j in range(3):
            board[i][j]=""  

def startGame(board,players,tossWinnerIndex):
    initializeBoard(board)
    players[1]=input("Enter name of the Player 1 (symbol X):")
    players[2]=input("Enter name of the player 2(symbol O):")
    while True:
     if (checkerName(players)):
        print("This name is already occupied")
        players[2]=input("Enter name of the player 2(symbol O):")
     break
    print(players[tossWinnerIndex],"won the toss so he will start first")
## Function End



# Main Program
# Varibles start
board=[["X","X","0"],["","0",""],["","","X"]]
players=["","Player1","Player2"]
states=["Play","Draw","Player1","Player2"]
state=0
whoStarted=0
playerInGame=whoWillStart()
whoStarted=playerInGame
## Variables Ends
startGame(board,players,whoStarted)
# Game Loop

while True:   
   playMove(board,players,playerInGame)
   state=checkBoard(board)
   if state==0:
     playerInGame=togglePlayer(playerInGame)
   else:
       playmore=announceResult(state,players) 
       if playmore==0:
           print("Thanks for playing")
       else:
           playerInGame=restartGame(board,players,whoStarted)
           whostarted=playerInGame
# Game Loop End