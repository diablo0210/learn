# f strings

score = 25
height = 1.69
# print("your score is: " + score); TypeError: can only concatenate str (not "int") to str
print("your score is : " + str(score))

# instead we can use f strings

print(f"your score is : {score}")
print(f"your score is {score} and your height is {height} meter.")