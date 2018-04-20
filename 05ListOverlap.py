# Exercise 04: ListOverlap
import random
lst_len1 = int(input('Please input the length of 1st list: '))
lst_len2 = int(input('Please input the length of 2nd list: '))

# list a
a = []
for i in range(lst_len1):
    a.append(random.randint(1,100))
print(a)

# list b
b = []
for j in range(lst_len2):
    b.append(random.randint(1,100))
print(b)

print('----The overlap numbers are----')

overlap_lst = []
for i in a:
    for j in b:
        if i == j:
            overlap_lst.append(i)
            
# clear out duplicates
overlap_clear = []
for i in overlap_lst:
    if i not in overlap_clear:
        overlap_clear.append(i)
overlap_clear.sort()

overlap = []
for i in overlap_clear:
    overlap.append(str(i))

print(" ".join(overlap))
