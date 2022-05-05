# Nested if/else statements

print("Welcome to the Rollercoaster!!")
height = int(input("Enter your height in centimeters : "))
if height >= 120:
    print("Yay, you can ride the rollercoaster!!")
    age = int(input("Please enter your age : "))
    if age <12:
        print("Please pay Rs. 100.")
    elif age <= 18:
        print("Please pay Rs 150")
    else:
        print("Please pay Rs 200.")
else:
     print("Sorry, you have to grow taller before you can ride this rollercoaster.")
