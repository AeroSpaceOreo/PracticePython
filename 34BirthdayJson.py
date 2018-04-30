# Example 34: Birthday Json
import json

with open('bday.json') as open_file:
          dict = json.load(open_file)

lst = []
for item in dict['game character']:
    lst.append(item['name'])
print('The names in this list are: ' + str(lst))

name = input('Input the name for the birthday you want to check: ').lower()
for item in dict['game character']:
    if item['name'] == name:
        print(item['birthday'])
