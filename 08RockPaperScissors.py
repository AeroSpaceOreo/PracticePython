# Exercise 08: Rock Paper Scissors
import random
print('Print r for rock, p for paper, s for scissors')
player = input('Player, input your guess: ')

lst = ['r', 'p', 's']
com = random.choice(lst)
print('Com choice: ' + com)

def rps(p, c):
    if p == c: #Draw
        print("It's a draw")
    elif p == 'r':
        if c == 's':
            print('You win')
        else:
            print('You lose')
    elif p == 'p':
        if c == 'r':
            print('You win')
        else:
            print('You lose')
    elif p == 's':
        if c == 'p':
            print('You win')
        else:
            print('You lose')
    else:
        print('(ERROR)You did not print r, p, or s')

rps(player, com) #Run the function
