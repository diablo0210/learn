# Average Height Calculator (using for loop)

list = input("Enter the heights of the students separated by a space:\n").split()
# .split() is used to split a string into a list where each word is a list item
total_number = len(list)
print(f"The total number of students is {total_number}.")
print(list)


# the list is a string currently

for n in range(0, len(list)):
    list[n] = int(list[n])
print(list)
# now the list is converted into integers

# Average Height Calculator (without using for loop)
total_height = sum(list)
avg = round(total_height / total_number)
print(f"The average = {avg}.")


# Average Height Calculator (By using for loop)
sum = 0
for i in list:
    sum += i
#     we can also use sum = i + sum
print(f"The total sum of heights is {sum}.")
# counting the number or items in the list using the for loop
total_num = 0
for j in list:
    total_num += 1
print(f"The total number of students is {total_num}.")
average = sum / total_num
average = round(average, 2)
print(f"The average height of the class is {average}.")

