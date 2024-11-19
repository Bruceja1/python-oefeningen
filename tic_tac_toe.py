board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

gameRunning = True
currentPlayer = "X"

def print_board(board):
    barrier = " | "
    
    print(board[0] + barrier + board[1] + barrier + board[2])
    print(board[3] + barrier + board[4] + barrier + board[5])
    print(board[6] + barrier + board[7] + barrier + board[8])

def get_input(currentPlayer, board):
    userInput = int(input("Enter position...\n"))

    if currentPlayer == "X":
        board[userInput - 1] = "X"
    elif currentPlayer == "O":
        board[userInput - 1] = "O"

def switch_player():
    global currentPlayer
    
    if currentPlayer == "X":
        currentPlayer = "O"
        print("Now O")
        
    else:
        currentPlayer = "X"
        print("Now X")
    
while gameRunning:
    print_board(board)
    get_input(currentPlayer, board)
    switch_player()
    
            
