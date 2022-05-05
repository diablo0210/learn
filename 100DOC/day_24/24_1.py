## How to open, read and write to file using the "with" keyword

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# # alternatively

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     # no need to close the file here

# write mode...will replace the existing data
with open("my_file.txt", mode="w") as file:
    file.write("I have a 4 year old lab named Momo.")

# append mode...will add to the existing data
with open("my_file.txt", mode="a") as file:
    file.write("\nShe is the best dog in the whole world.")
