# Exercise 02: Odd or Even

number = int(input('Input a integer: '))
if number % 2 == 0: # Even
    if number >= 4 and number % 4 == 0:
        print("The number is even, and a multiple of 4")
    else:
        print("The number is even")
else: #Odd
    print("The number is odd")
