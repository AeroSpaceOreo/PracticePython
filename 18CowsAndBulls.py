# Exercise 18: Cows And Bulls
import random

num = str(random.randint(1,9))
while len(num) < 4:
    rand = str(random.randint(0,9))
    if rand not in num:
        num += rand
    
print(num) ### Must delete later


def cow_and_bull(ans,gue):
    cow_count = 0
    bull_count = 0
        
    for i in ans:
        for j in gue:
            if i == j and ans.index(i) == gue.index(j):
                bull_count += 1
            elif i == j and ans.index(i) != gue.index(j):
                cow_count += 1
    if ans == gue:
        return True
    else:
        return cow_count, bull_count

def just_for_printing(a, b):
    return print(str(a) + ' cow, ' + str(b) + ' bull')
"""
    if a > 1 and b > 1:
        return print(str(a) + ' cows, ' + str(b) + ' bulls')
    elif (a == 0 and b == 0) or (a == 1 and b == 1):
        return print(str(a) + ' cow, ' + str(b) + ' bull')
    elif a > 1 and b == 0:
        return print(str(a) + ' cows, ' + str(b) + ' bull')
    elif a == 0 and b > 1:
        return print(str(a) + ' cow, ' + str(b) + ' bulls')
"""    

print('Welcome to the Cow and Bull game! You will get twenty guesses.')

count = 0

while count < 20:
    user = input('Please input a four digit number: ')
    if user == 'break':
        break
    
    if len(user) != 0:
        if cow_and_bull(num, user) == True:
            print('You got the number!')
            break
        else:
            cow, bull = cow_and_bull(num, user)
            just_for_printing(int(cow), int(bull))
            count += 1
            print('Your chances left: ' + str(20 - count))

