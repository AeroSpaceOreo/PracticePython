# Exercise 33: Birthday Dictionaries
dict = {
    'ryu': '07/21/1964',
    'mega man': '12/17/1986',
    'booker dewitt': '04/19/1874',
    'ezio auditore': '06/24/1459',
    'cloud strife': '08/19/1986'
    }

name = []
for key in dict:
    name.append(key.title())
print('Names in this list are: ' + str(name))
    
user = input('Input the name for the birthday you want to check: ').lower()
print(dict[user])
