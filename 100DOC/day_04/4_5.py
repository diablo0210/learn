#Nested Lists

list1 = ["Rose", "Lily", "Magnolia", "Tulip", "Sunflower", "Periwinkle"]
list2 = ["Apple", "Orange", "Pear", "Watermelon", "Mango"]
list3 = [list1, list2]
print(list3)
print(list3[0])
print(list3[1])
print(list3[0][1])
print(list3[1][1])

print(len(list1))
print(len(list2))
print(len(list3))
list4 = list1 + list2
print(list4)
print(len(list4))

