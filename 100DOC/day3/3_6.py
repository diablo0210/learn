# Multiple if statements in succession

print("Welcome to the Rollercoaster!!")
height = int(input("Enter your height in centimeters : "))
bill = 0
if height >= 120:
    print("Yay, you can ride the rollercoaster!!")
    age = int(input("Please enter your age : "))
    if age <12:
        bill = 100
        print("For children below 12 years the ticket price is Rs. 100.")
    elif age <= 18:
        bill = 150
        print("For children between 12-18 the ticket price is Rs 150.")
    else:
        bill = 200
        print("For adults the ticket price is Rs 200.")
    photo = input("Do you want a photo? Y or N")
    if photo == "N":
        print(f"Your final price is {bill}.")
    else:
        bill += 50
        print(f"Your final price is {bill}.")
else:
     print("Sorry, you have to grow taller before you can ride this rollercoaster.")
