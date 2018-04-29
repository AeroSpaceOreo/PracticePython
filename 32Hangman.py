# Exercise 32: Hangman
import random
with open('sowpods.txt', 'r') as open_file:
    content = open_file.read().lower().split()

line = random.choice(content)
lst = list(line)
print(line)
hangman = '*' * len(line)
print(hangman)
print(str(len(line)) + ' letters')

turn = 0
last_guess = ''

def handsomeman(turn):
    if turn == 1:
        print('|--O   ')
        print('|      ')
        print('|      ')
    elif turn == 2:
        print('|--O   ')
        print('|  |   ')
        print('|      ')
    elif turn == 3:
        print('|--O   ')
        print('| /|   ')
        print('|      ')
    elif turn == 4:
        print('|--O   ')
        print('| /|\  ')
        print('|      ')
    elif turn == 5:
        print('|--O   ')
        print('| /|\  ')
        print('| /    ')
    elif turn == 6:
        print('|--O   ')
        print('| /|\  ')
        print('| / \  ')
            

while hangman != line and turn < 6:
    user = input('Input a letter: ').lower()
    
    if user == 'break':
        break        
    
    elif len(user) == 1:
        if user == last_guess:
            print("You've already guess that letter")
            
        elif user in lst:
            hangman = list(hangman)
            for i in range(len(line)):
                if lst[i] == user:
                    hangman[i] = user
            hangman = ''.join(hangman)
            print(hangman)
            last_guess = user
            
        else:
            turn += 1
            print(hangman)
            print(str(6 - turn) + ' turns left')
            handsomeman(turn)
            last_guess = user
            
    else:
        print('You did not enter a letter, try again')
        
if hangman != line:
    print('You failed, HANGMAN')
else:
    print("You've got the letter! Congratulations!")
