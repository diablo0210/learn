# BMI Calculator

h = input("Enter your height in meters: ")
w = input("Enter your weight in kg: ")
a = float(w) / float(h) ** 2
print(a)
b = int(a)
print("Your BMI is: " + str(b))