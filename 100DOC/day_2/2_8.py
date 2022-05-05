#Days left until age 90

age = input("What is your current age? ")

x = (90 - int(age))
months = x * 12
weeks = x * 52
days = x * 365
print(f"You have {days} days, {weeks} weeks, and, {months} months remaining until you turn 90 years old.")