# Exercise 30: Pick Word
import random
with open('sowpods.txt', 'r') as open_file:
    content = open_file.read().split()

line = random.choice(content)
print(line)
