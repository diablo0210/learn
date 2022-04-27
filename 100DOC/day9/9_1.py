# Python Dictionaries = {Key:Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents it from running as expected.",
    "Function": "A piece of code that we can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# retrieving items from a dictionary:
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
print(programming_dictionary["Loop"])

# adding new items to the dictionary:
programming_dictionary["Python Dictionary"] = "A dictionary is created by using curly braces."
print(programming_dictionary["Python Dictionary"])

# creating an empty dictionary:
empty_dict = {}

# editing an item in dictionary:
programming_dictionary["Bug"] = "A moth in the computer."
print(programming_dictionary)

# Loop through a dictionary:
for i in programming_dictionary:
    print(i)
    print(programming_dictionary[i])

# wipe an existing dictionary:
programming_dictionary = {}
print(programming_dictionary)
