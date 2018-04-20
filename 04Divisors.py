# Exercise 04: Divisors
num = int(input('Please input an integer: '))
lst = range(1, num + 1)

elst = []
for i in lst:
    if num % i == 0:
        elst.append(i)
print('The divisors of your input is')
print(elst)
