#Bankers' Roulette
import random

list = input("Enter the Names separated by a comma and a space: \n")

# using str.split() to convert the Input string into a list
list1 = list.split(", ")
print(list1)

# creating the random number
x = list1.index(list1[-1])
print(x)
y = random.randint(0, x)
print(y)
person_paying = list1[y]
print(f"The person paying the bill is {person_paying}.")

# Alternatively
p = len(list1)
print(p)
# to obtain the number of items in the list
q = p - 1
print(q)
r = random.randint(0, q)
print(r)
pp = list1[r]
print(f"The person paying the bill is {pp}.")



# Using random.choice for picking a random item in the list
print(list1)
p1 = random.choice(list1)
print(f"the person paying the bill is {p1}")
