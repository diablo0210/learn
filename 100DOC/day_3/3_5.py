# Leap Year

x = int(input("Enter a year: "))
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print(f"{x} is a Leap Year.")
        else:
            print(f"{x} is NOT a Leap Year.")
    else:
        print(f"{x} is a Leap Year.")
else:
    print(f"{x} is NOT a Leap Year.")