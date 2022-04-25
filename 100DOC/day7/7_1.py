# Functions with Inputs

# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello!")
    print("How are you?")
    print("Lovely weather today.\n")

greet()

def greet_2(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?\n")

greet_2("Vivek")

greet_2("Sneha")

# Functions with more than one input
def greet_3(name, location):
    print(f"Hello {name}.")
    print(f"What's the weather like in {location}.\n")

greet_3("Sneha", "Bokaro")

greet_3("Bokaro", "Sneha")
# if we switch the position of the arguments, it will lead to an error.

# hence to make the code less error prone, a good practice would be to assign the parameters within the bracket
greet_3(name="Sneha", location="Jharkhand")

# now, even if we interchange the positions, it will still give me the same results
greet_3(location="Jharkhand", name="Sneha")