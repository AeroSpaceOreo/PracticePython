# Exercise 06: String Lists

string = input('Input a palindrome string(such as ABBA, racecar, madam): ')
string = string.lower()
# find the aft-1/2 part of the string
after = string[len(string) : int(len(string) / 2) - 1 : -1]
after_odd = string[len(string) : int(len(string) / 2) : -1]

if string[0:int(len(string)/2)] == after:
    print('It is a palindrome string. With even characters.')
elif string[0:int(len(string)/2)] == after_odd:
    print('It is a palindrome string. With odd characters.')
else:
    print('It is not a palindrome.')
