# using len() function to get the number of characters in a string

print(len("Hello"))

print(len("5468854545542"))

print("hello"[1])
# subscripting: the pulling out of a particular element from a string

print("123" + "456")
# concatenation of strings

print(123 + 456)
# without double quotes means not string, hence we obtain the sum

num_char = len(input("What is your name?\n"))
# print("Your name has" + num_char + "characters.")
# TypeError: can only concatenate str (not "int") to str

print(type(num_char))
#to find out the type of variable if unsure.

#typecasting:conversion or changing of one particular data type to another
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

print(70 + 80)

print(str(70) + str(80))

print("70" + "80")
