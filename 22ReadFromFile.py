# Exercise 22: Read From File
with open('nameslist.txt', 'r') as open_file:
    content = open_file.read().splitlines()
content = list(content)

namae = []
for name in content:
    if name not in namae:
        namae.append(name)
print('The names in this list are: ' + str(namae))

# Create dictionary for all name
dict = {}
for n in namae:
    dict[n] = 0


for i in content:
    dict[namae[namae.index(i)]] += 1

print('Number count of each name is', str(dict))


