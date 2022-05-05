# Using for loop with the range function

for x in range(0, 10):
    print(x)
# here in the range function(0, 10) the last number(10 in this case) is not included
# to include the last number, take +1 in the range

for x in range(0, 11):
    print(x)

# sum of all the numbers between a given range, say 0 to 10
sum = 0
for n in range(1, 11):
    sum += n
print(f"the sum total of all the numbers from 0 to 10 is {sum}")

# add all the numbers from 0 to 100
sum = 0
for n in range(1, 101):
    sum += n
print(f"the sum total of numbers from 0 to 100 is {sum}.")

# add all the numbers from 0 to 1000
sum = 0
for n in range(1, 1001):
    sum += n
print(f"the sum total of numbers from 0 to 1000 is {sum}.")

# jumping the steps in the range function
for n in range(0, 11, 2):
    print(n)

for n in range(0, 11, 3):
    print(n)

for n in range(0, 11, 4):
    print(n)

# sum of all the even numbers from 0 to 100
sum_even = 0
for n in range(0, 101, 2):
    print(n)
    sum_even += n
print(f"the sum of all the even numbers between 0 to 100 is {sum_even}.")

# alternate for getting the sum of even numbers
sum_even = 0
for n in range(0, 101):
    if n % 2 ==0:
        sum_even += n
print(f"sum of even numbers by modulo method is {sum_even}")

# sum of all the odd numbers from 0 to 100
sum_odd = 0
for n in range(1, 101, 2):
    print(n)
    sum_odd += n
print(f"the sum of all the odd numbers between 0 to 100 is {sum_odd}.")

