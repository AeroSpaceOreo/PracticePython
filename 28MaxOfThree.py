# Exercise 28: Max Of Three
print('[Enter break,, to break]')
a, b, c = input('Input three numbers, followed by comma: ').split(',')

if a > b and a > c:
    print(str(a) + ' is the largest number of the three')
elif b > a and b > c:
    print(str(b) + ' is the largest number of the three')
elif c > a and c > b:
    print(str(c) + ' is the largest number of the three')
