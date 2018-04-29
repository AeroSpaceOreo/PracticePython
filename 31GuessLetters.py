# Exercise 31: Guess Letters
import random
with open('sowpods.txt', 'r') as open_file:
    content = open_file.read().lower().split()

line = random.choice(content)
lst = list(line)
# print(line)
hangman = '*' * len(line)
print(hangman)
print(str(len(line)) + ' letters')

last_guess = ''

while hangman != line:
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
            print(hangman)
            last_guess = user
            
    else:
        print('You did not enter a letter, try again')
        
if hangman == line:
    print("You've got the letter! Congratulations!")
