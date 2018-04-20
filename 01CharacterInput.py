# Exercise 1: Character Input

from datetime import datetime

current_date = datetime.now()
print(current_date)
print("Insert X to break")
# Print today's year
year = current_date.year
print("The current year is: " + str(year))

# User input
name = input("What is your name? ")
print("Name:", name) 
    
age = int(input("What is your age? "))
print("Age: ", str(age))

if age < 100:
    variance = 100 - age
    year_hundred = year + variance
    print("Dear " + name + ", you will turn 100 years old at " + str(year_hundred))
elif age == 100:
    print("Congratulations, you are 100 years old!")
else:
    var = age - 100
    pass_hundred = year - var
    print(name + ", you have passed 100 years old at year " + str(pass_hundred))
