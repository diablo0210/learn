# Prime Number Checker

def prime(num):
    x = 0
    for i in range(1, num+1):
        if num % i == 0:
            x = x + 1
            # print(x)
    if x != 2:
        print(f"{num} is a NOT a  Prime number.")
    else:
        print(f"{num} is a Prime number.")

n = int(input("Enter the number: "))
prime(num=n)
