# Exercise 23: File Overlap
# List 1
with open('PrimeUnder1000.txt', 'r') as open_file:
    prime = open_file.read().splitlines()
    prime = list(prime)

# List 2
with open('happynumber.txt', 'r') as open_file2:
    happy_number = open_file2.read().splitlines()

# Using list comprehension
overlap = [x for x in prime for y in happy_number if x == y]
print('The overlap numbers are: ' + str(overlap))
