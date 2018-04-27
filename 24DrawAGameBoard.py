# Exercise 24: Draw A Game Board
print('What size of game board do you want?')
size = int(input('(e.g. type 3 for 3x3): '))
row = ' ---' * size
col = '|   ' * (size + 1)

for i in range(size):
    print(row)
    print(col)
print(row)
