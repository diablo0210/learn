# List Comprehension

numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = 0
#     add_1 += n + 1
#     new_list.append(add_1)
#
# print(new_list)

# List comprehension : new_list = [new_item for item in list
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Vivek Sharma"
letters = [i for i in name]
print(letters)

double_range = [x*2 for x in range(1,5)]
print(double_range)

# Conditional List Comprehension: new_list = [new_item for item in list if test]
num_list = [x for x in range(1, 11)]
print(num_list)
even_nums = [x for x in num_list if x % 2 == 0]
print(even_nums)
odd_nums = [x for x in num_list if x % 2 != 0]
print(odd_nums)

