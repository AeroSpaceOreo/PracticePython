# Exercise 13: Fibonacci
user = int(input('Input the desire Fibonnaci list length: '))

def fibonacci(arg):
    lst = [0,1]
    while len(lst) < user:
        for seq in range(user - 1):
            next_num = lst[seq + 1] + lst[seq]
            lst.append(next_num)
    lst.pop(lst[0])
    return lst

print('Your Fibonacci list with the length of ' + str(user) + ' is:')
print(fibonacci(user))
