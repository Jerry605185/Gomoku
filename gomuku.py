import random
def move(n,board):
    while True:
        userinputrow = input("Please enter a row index between 0 and " + str(n-1) + ":")
        userinputcol = input("Please enter a column index between 0 and " + str(n-1) + ":")
        if(not userinputrow.isdigit() or not userinputcol.isdigit()):
            print("(" + userinputrow + ", " + userinputcol + ")" + " is not a legal input!")
            continue
        row, col = int(userinputrow), int(userinputcol)
        if(row not in range(n) or col not in range(n)):
            print("(" + userinputrow + ", " + userinputcol + ")" + " is not a legal space!")
            continue
        if(board[row][col] != " "):
            print("(" + userinputrow + ", " + userinputcol + ")" + " is not an available space!")
            continue
        else:
            return row , col
        
def make_empty_board(n):
    board = [[" " for _ in range(n)]for _ in range(n)]
    return board

    

def print_board(n, board):
  boundary_line = ("+---" * n) + "+"
  for i in range(n):
    print(boundary_line)
    row_i = "|"
    for j in range(n):
      row_i += " " + board[i][j] + " " + "|"
    print(row_i)
  print(boundary_line)

def row_win(n,board,player):
    for row in board:
        counter = 0
        if (spaces == player for spaces in row):
            counter += 1
            if(counter >= 5):
                return True
        else:
            counter = 0
    return False

def play_gomuku(n):
    print("20th century")
    print("War aint the answer in modern world. So to solve the yellow river dispute the shang royal family and King Wu")
    print(" decide to play a game of gomoku, whoever wins the game wins the yellow river base")
    print("Help King Wu to win the yellow river base, In exchange he is ready to give you 10% of the land.")
    make_empty_board(n)

#player's stone will get destroyed occasionally
#player's stone can be traitor?
