# Pizza Order

print("Welcome to Diblo's Den!")
s = input("What size pizza would you like to have? S, M, or L : ")
p = input("Do you want pepperoni? Y or N : ")
c = input("Do you want extra cheese? Y or N : ")
bill = 0
if s == "S":
    bill = 150
    if p == "Y":
        bill += 20
    if c == "Y":
        bill += 10
    print(f"Your total bill is Rs. {bill}.")
if s == "M":
    bill = 200
    if p == "Y":
        bill += 30
    if c == "Y":
        bill += 20
    print(f"Your total bill is Rs. {bill}.")
if s == "L":
    bill = 250
    if p == "Y":
        bill += 40
    if c == "Y":
        bill += 30
    print(f"Your total bill is Rs. {bill}.")



# alternate version
print("Welcome to Diblo's Den!")
size = input("What size pizza would you like to have? S, M, or L : ")
pep = input("Do you want pepperoni? Y or N : ")
cheese = input("Do you want extra cheese? Y or N : ")
bill = 0
if size == "S":
    bill += 150
elif size == "M":
    bill += 200
else:
    bill += 250

if pep == "Y":
    if size == "S":
        bill += 20
    elif size == "M":
        bill += 30
    else:
        bill += 40

if cheese == "Y":
    if size == "S":
        bill += 10
    elif size == "M":
        bill += 20
    else:
        bill += 30
print(f"Your final bill amount is Rs. {bill}.")