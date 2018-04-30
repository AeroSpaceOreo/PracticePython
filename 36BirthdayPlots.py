# Example 36: Birthday Plots
import json
from bokeh.plotting import figure, show, output_file

output_file('PlotForExercise36.html') # not necessary needed

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

# Bokeh drawing
# Month sorter(not printing empty months), also corresponding count
month = ['January', 'February', 'March', 'April', 'May', 'June', \
         'July', 'August', 'September', 'October', 'November', 'December']
x = []
y = []
for m in month:
    if m in birthday_count.keys():
        x.append(m)
        y.append(birthday_count[m])

p = figure(x_range = x) # x_range assign above month var for full range
p.vbar(x = x, top = y, width = 0.5)

show(p)

