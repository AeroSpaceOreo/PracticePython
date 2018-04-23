# Exercise 12: List Ends
import random
user = int(input('Input the length of the list: '))

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

c = []
c.append(b[0]);
c.append(b[len(b) - 1])

print(c)
         
