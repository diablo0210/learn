# BMI Calculator v2.0

h = input("Enter your height in meters: ")
w = input("Enter your weight in kg: ")
a = float(w) / float(h) ** 2
print(a)
print(round(a))
b = int(round(a))
print("Your BMI is: " + str(b))
if b <= 18.5:
    print("You are UNDERWEIGHT")
elif b<25:
    print("Yoh have a Normal Weight")
elif b<30:
    print("You are OVERWEIGHT!!!")
elif b<35:
    print("You are OBESE!!!")
else:
    print("You are CLINICALLY OBESE!!!")