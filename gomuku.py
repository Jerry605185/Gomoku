print("20th century")
print("War aint the answer in modern world. So to solve the yellow river dispute the shang royal family and King Wu")
print(" decide to play a game of gomoku, whoever wins the game wins the yellow river base")
print("Help King Wu to win the yellow river base, In exchange he is ready to give you 10% of the land.")
def move():
    row_for_move = input("Please enter the row number you want to put the piece on:")
    col_for_move = input("Please enter the column number you want to put the piece on:")
    board[row_for_move][col_for_move] = 1
def print_board(board):
    counter = 15
    for row in board:
        my_str = ""
        for elem in row:
            if elem == 0:
                my_str += " ☐ "
            elif elem == 9:
                my_str = str(counter) + my_str
                counter -= 1
        print(my_str)

    print("-----------------------------------------------")
    print("0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15")

board = [
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

print_board(board)