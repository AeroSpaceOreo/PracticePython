# Exercise 14: List Remove Duplicates
import random
inp_a = int(input('Input length for list a: '))
inp_b = int(input('Input length for list b: '))

lst_a = []
for i in range(inp_a):
    lst_a.append(random.randint(1,20))
print(lst_a)

lst_b = []
for j in range(inp_b):
    lst_b.append(random.randint(1,20))
print(lst_b)

# Append and convert to set
lst_a += lst_b
lst_a = set(lst_a)
print('The combined list is: ')
print(lst_a)


