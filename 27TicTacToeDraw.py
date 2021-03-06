# Exercise 27: Tic Tac Toe Draw
from datetime import datetime

now = datetime.now()
print('The current time is %02d/%02d/%04d %02d:%02d:%02d' \
      % (now.month, now.day, now.year, \
         now.hour, now.minute, now.second))

input('Welcome to the two-player Tic Tac Toe game, press ENTER to continue...')

board = [[0,0,0], [0,0,0], [0,0,0]] # Just an empty board
boardOandX = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

def wincheck(a):
    # Check diag win condition
    if a[1][1] != 0:
        if a[0][0] == a[1][1] == a[2][2]:
            return True
        elif a[0][2] == a[1][1] == a[2][0]:
            return True
        
    for r in range(3):  
        # Check row/col win condition
        if a[r][0] == a[r][1] == a[r][2] and a[r][0] == a[r][1] == a[r][2] != 0:
            return True
    for c in range(3):
        if a[0][c] == a[1][c] == a[2][c] and a[0][c] == a[1][c] == a[2][c] != 0:
            return True
turn = 0    

while turn < 9:
    # PLAYER ONE
    print('Player one, your turn')
    r1, c1 = input('Input (rol,col) with a comma \n [type (break,) to break]: ').split(',')
    if r1 == 'break' or c1 == 'break':
        break
    row_1 = int(r1) - 1
    col_1 = int(c1) - 1
    
    while board[row_1][col_1] == 2 or board[row_1][col_1] == 1: #Duplicate Placement
        print('That place is already occupied!')
        r1, c1 = input('Input (rol,col) with a comma \n [type (break,) to break]: ').split(',')
        if r1 == 'break' or c1 == 'break':
            break
        row_1 = int(r1) - 1
        col_1 = int(c1) - 1
    
    board[row_1][col_1] = 1
    boardOandX[row_1][col_1] = 'X'
    for i in range(3):
        print(boardOandX[i])
    print('----------')
        
    
    if wincheck(board) == True:
        print('Player one, you have won! Congratulations!')
        break
    turn += 1
    
    if turn == 9: # Draw game after 9 turns
        print("It's a draw")
        break

    # PLAYER TWO
    print('Player two, your turn')
    r2, c2 = input('Input (rol,col) with a comma \n [type (break,) to break]: ').split(',')
    if r2 == 'break' or c2 == 'break':
        break
    row_2 = int(r2) - 1
    col_2 = int(c2) - 1
    
    while board[row_2][col_2] == 1 or board[row_2][col_2] == 2:
        print('That place is already occupied!')
        r2, c2 = input('Input (rol,col) with a comma \n [type (break,) to break]: ').split(',')
        if r2 == 'break' or c2 == 'break':
            break
        row_2 = int(r2) - 1
        col_2 = int(c2) - 1
    
    board[row_2][col_2] = 2
    boardOandX[row_2][col_2] = 'O'
    for i in range(3):
        print(boardOandX[i])
    print('----------')
        
    if wincheck(board) == True:
        print('Player two, you have won! Congratulations!')
        break
    turn += 1
