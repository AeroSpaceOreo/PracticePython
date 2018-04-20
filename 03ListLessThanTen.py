# Exercise 03: List Less Than Ten
import random
# create random list and print
randlst = []
for i in range(20):
    i = random.randint(1,20)
    randlst.append(i)
print(randlst)

userinput = int(input('Input an integer: '))

lst = []
for item in randlst:
    if item < userinput:
        lst.append(item)
print(lst)

#---Using pop---
#for item in randlst:
#    if item > 0:
#    randlst.pop(item)
#print(randlst)
