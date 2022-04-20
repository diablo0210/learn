# tip calculator

x = input("What is the total bill amount?\n")
y = input("How many people to split the bill?\n")
z = input("What percentage tip would you like to give?\n")
a = float(x) * float(z) / 100 #total tip
b = float(x) + float(a) #total amount after tip
c = float(b)/float(y) #final amount per person
d = round(c, 2)
print(f"Each person should pay {d}.")