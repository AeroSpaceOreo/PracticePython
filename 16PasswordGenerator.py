# Exercise 16: Password Generate
import random

user = input('Do you want your password "weak" or "strong"? ')

def rand_int():
    return str(random.randint(0,9))

def rand_sym():
    symbols = ['!', '?', '@', '#', '$', '%', '&' ,'*']
    return random.choice(symbols)

def rand_alpha():
    alphabet = 'abcdefghijklmnopqustuvwxyz'
    alphabet += alphabet.upper()
    return random.choice(alphabet)

def password_weak():
    letter_pool = ['apple', 'ball', 'cat', 'dog', 'elephant', 'fish', \
                   'grizzly', 'horse', 'igloo', 'jazz', 'koala', 'lion', \
                   'monkey', 'nerd', 'octo', 'panda', 'quail', 'raw', \
                   'snake', 'turtle', 'utopia', 'violet', 'whale', \
                   'xray', 'young', 'zebra']
    letter_pool2 = letter_pool
    one_or_two = random.randint(1,2)
    if one_or_two == 1:
        return 'Your password is: ' + random.choice(letter_pool)
    elif one_or_two == 2:
        first_choice = random.choice(letter_pool)
        idx = letter_pool2.index(first_choice)
        del letter_pool2[idx]
        second_choice = random.choice(letter_pool2)
        return 'Your password is: ' + first_choice + second_choice

# Could further add a mid strength option combining word + randoms

def password_strong(arg):
    password = ''
    
    while len(password) < arg:
        int = random.randint(1,3)
        if int == 1:
            password += rand_int()
        elif int == 2:
            password += rand_sym()
        elif int == 3:
            password += rand_alpha()
    return 'Your password is: ' + password
    
if user == 'weak':
    print(password_weak())

elif user == 'strong':
    len_password = int(input('How long do you want your password? '))
    print(password_strong(len_password))

else:
    print('You did not enter weak or strong')
    
