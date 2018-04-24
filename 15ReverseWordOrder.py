# Exercise 15: Reverse Word Order
string = input('Please input a sentence: ')

def reverser(arg):
    splitter = string.split()
    result = []
    for item in splitter:
        result = splitter[::-1]
        return ' '.join(result)

print(reverser(string))
    

