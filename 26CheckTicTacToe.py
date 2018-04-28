# Exercise 26: Check Tic Tac Toe
board = [[0,0,0], [0,0,0], [0,0,0]] # Just an empty board

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
    r1 = input('Input the row: ')
    if r1 == 'break':
        break
    row_1 = int(r1) - 1
    c1 = input('Input the column: ')
    if c1 == 'break':
        break
    col_1 = int(c1) - 1
    
    while board[row_1][col_1] == 2 or board[row_1][col_1] == 1: #Duplicate Placement
        print('That place is already occupied!')
        r1 = input('Input the row: ')
        if r1 == 'break':
            break
        row_1 = int(r1) - 1
        c1 = input('Input the column: ')
        if c1 == 'break':
            break
        col_1 = int(c1) - 1
    
    board[row_1][col_1] = 1
    for i in range(3):
        print(str(board[i]) + '\n')
    print('----------')
        
    
    if wincheck(board) == True:
        print('Player one, you have won')
        break
    turn += 1
    
    if turn == 9: # Draw game after 9 turns
        print("It's a draw")
        break

    # PLAYER TWO
    print('Player two, your turn')
    r2 = input('Input the row: ')
    if r2 == 'break':
        break
    row_2 = int(r2) - 1
    c2 = input('Input the column: ')
    if c2 == 'break':
        break
    col_2 = int(c2) - 1
    while board[row_2][col_2] == 1 or board[row_2][col_2] == 2:
        print('That place is already occupied!')
        r2 = input('Input the row: ')
        if r2 == 'break':
            break
        row_2 = int(r2) - 1
        c2 = input('Input the column: ')
        if c2 == 'break':
            break
        col_2 = int(c2) - 1
    
    board[row_2][col_2] = 2
    for i in range(3):
        print(str(board[i]) + '\n')
    print('----------')
        
    if wincheck(board) == True:
        print('Player two, you have won')
        break
    turn += 1
