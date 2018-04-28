# Exercise 29: Tic Tac Toe Game
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

p1_score = 0 #Scoreboards
p2_score = 0
draw = 0

while True:
    turn = 0    

    while turn < 9:
        # PLAYER ONE
        print('Player 1, your turn')
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
            print('Player 1, you have won! Congratulations!')
            p1_score += 1
            break
        turn += 1
    
        if turn == 9: # Draw game after 9 turns
            print("It's a draw")
            draw += 1
            break

        # PLAYER TWO
        print('Player 2, your turn')
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
            print('Player 2, you have won! Congratulations!')
            p2_score += 1
            break

        turn += 1

    
    print('###ScoreBoard###')
    print('Player 1 win: ' + str(p1_score))
    print('Player 2 win: ' + str(p2_score))
    print('Draw games: ' + str(draw))

    # Board Reset
    turn = 0
    board = [[0,0,0], [0,0,0], [0,0,0]]
    boardOandX = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    
    # Ask the user if they want to continue
    cont = str(input('Do you want to continue(y/n)? ')).lower()
    if cont == 'n' or cont == 'no':
        break

