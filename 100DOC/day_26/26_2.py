# list comprehension exercises

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squares = [x**2 for x in numbers]
print(squares)
even = [x for x in numbers if x%2 == 0]
print(even)
odd = [x for x in numbers if x%2 != 0]
print(odd)