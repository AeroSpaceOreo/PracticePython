# Exercise 20: Element Search
import random

lst = []
while len(lst) < 20:
    rand = random.randint(1,50)
    if rand not in lst:
        lst.append(rand)


lst.sort()   
print(lst)

def binary_search(element):
    for i in lst:
        if int(i) == int(element):
            return True

while True: # infinite loop
    user = input('Input a value between 1 and 20: ')
    if user == 'break':
        break
    elif binary_search(int(user)) == True:
        print('Your number is in the list!')
        break
    else:
        print('Your number is not in the list, try again')
