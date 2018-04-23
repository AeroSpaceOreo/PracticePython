# Exercise 12: List Ends
import random

user = int(input('Input the length of the list: '))

def init_end(lst):
    return [lst[0], lst[len(lst) - 1]]


a = []
for i in range(user):
    a.append(random.randint(1,20))

# Sort
b = []
for j in a:
    if j not in b:
        b.append(j)
b.sort()
print('List is: ' + str(b))

print(init_end(b))
         
