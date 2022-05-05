# Password Generator (self)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

let = int(input("How many letters would you like in your password?\n"))
num = int(input("How many numbers would you like in your password?\n"))
sym = int(input("How many symbols would you like in your password?\n"))

# Easy level(without jumbling)
password = ""
for char in range(1, let + 1):
    password += random.choice(letters)
for char in range(1, num + 1):
    password += random.choice(numbers)
for char in range(1, sym + 1):
    password += random.choice(symbols)
print(password)

# Hard level(with jumbling)
pass_list = []
for char in range(1, let + 1):
    pass_list.append(random.choice(letters))
for char in range(1, num + 1):
    pass_list.append(random.choice(numbers))
for char in range(1, sym + 1):
    pass_list.append(random.choice(symbols))
print(pass_list)
random.shuffle(pass_list)
print(pass_list)

# converting the list into string
pass_str = ""
for char in pass_list:
    pass_str += char
print(pass_str)
