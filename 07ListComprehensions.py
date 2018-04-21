# Exercise 07: List Comprehensions

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
# Target is to get the even elements in ONE line.
lst = [x for x in a if x % 2 == 0]; # Syntax of list comprehension
print(lst)
