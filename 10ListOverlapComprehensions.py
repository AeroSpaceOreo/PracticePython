# Exercise 10: List Overlap Comprehensions
import random
lena = random.randint(10, 50)
lenb = random.randint(10, 50)

a = []
b = []

for i in range(1, lena):
    a.append(random.randint(1, 35))
for j in range(1, lenb):
    b.append(random.randint(1, 35))

print(a)
print(b)

c =  [x for x in a for y in b if x == y]

d = []
c.sort()
for i in c:
    if i not in d:
        d.append(i)
print('The overlap numbers are: ' + str(d))
