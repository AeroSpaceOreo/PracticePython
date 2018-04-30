# Example 35: Birthday Months
import json

with open('bday.json') as open_file:
          dict = json.load(open_file)
lst = []
for item in dict['game character']:
    lst.append(item['name'])
print('The names in this list are: ' + str(lst))

def month_to_alpha(imp):
    if imp == '01':
        return 'January'
    elif imp == '02':
        return 'February'
    elif imp == '03':
        return 'March'
    elif imp == '04':
        return 'April'
    elif imp == '05':
        return 'May'
    elif imp == '06':
        return 'June'
    elif imp == '07':
        return 'July'
    elif imp == '08':
        return 'August'
    elif imp == '09':
        return 'September'
    elif imp == '10':
        return 'October'
    elif imp == '11':
        return 'November'
    elif imp == '12':
        return 'December'

birthday_count = {}
# Create dictionary key
for item in dict['game character']:
    bday = item['birthday']
    birthday_count[month_to_alpha(bday[0:2])] = 0
# Count every key with same month
for item in dict['game character']:
    bday = item['birthday']
    birthday_count[month_to_alpha(bday[0:2])] += 1
    
print('The birthday count for months are: ' + str(birthday_count))

#name = input('Input the name for the birthday you want to check: ').lower()
#for item in dict['game character']:
#    if item['name'] == name:
#        print(item['birthday'])
