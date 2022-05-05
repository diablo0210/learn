# Love Calculator

print("Welcome to the Love Calculator!!!")
name1 = input("Enter the first name : ")
name2 = input("Enter the second name : ")
name1 = name1.lower()
name2 = name2.lower()
# FOR CONVERTING THE NAMES INTO LOWER CASE LETTERS
T1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
T2 = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
L1 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
L2 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")
# FOR COUNTING THE NUMBER OF LETTERS
x = T1 + T2
y = L1 + L2
print(f"Your compatibility is {x}{y}%.")
fs = int(str(x) + str(y))
if fs < 10 or fs > 90:
    print("You go together like coke and mentos.")
if fs <= 50 and fs >= 40:
    print("You are alright together.")
