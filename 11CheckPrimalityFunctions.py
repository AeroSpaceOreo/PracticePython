# Exercise 11: Check Primality Funcitons
user = int(input('Please input a number, will determine prime or not: '))

def primechecker(arg):
        if arg == 1 or arg == 0:
            return False
        elif arg > 2:
            for i in range(2, arg):
                if arg % i == 0:
                    return False
                else:
                    return True

def primeprinter(prime):
    if primechecker(user) == True:
        print(str(user) + ' is a prime number')
    elif primechecker(user) == False:
        print(str(user) + ' is not a prime number')

primeprinter(user)

