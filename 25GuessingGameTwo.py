# Exercise 25: Guessing Game Two
import random

maxnum = 100
minnum = 0
rand = random.randint(minnum, maxnum)
   
print('Welcome to the guessing number game. Now pick a number between 0 and 100')
delay = input("When you're ready, press any button and then enter to continue...")

print("I'm going to try to guess the number, my initial guess is: " + str(rand))

while True:
    user = str(input('Is it high, low, or bingo: '))
    if user == 'bingo':
        print('It got your number, Skynet is coming!')
        break
    elif user == 'high':
        print('Too high!')
        maxnum = rand
        rand = random.randint(minnum, maxnum - 1)
        print('My next guess is ' + str(rand))
    elif user == 'low':
        print('Too low!')
        minnum = rand
        rand = random.randint(minnum + 1, maxnum)
        print('My next guess is ' + str(rand))
