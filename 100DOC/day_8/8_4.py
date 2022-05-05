# Prime Number list

def prime(num):
    x = 0
    for i in range(1, num+1):
        if num % i == 0:
            x = x + 1
    if x ==2:
        print(num)

y = int(input("Enter the number upto which you want the list of prime numbers: "))
for j in range(0, y + 1):
    prime(j)