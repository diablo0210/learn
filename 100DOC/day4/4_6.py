#Treasure Map

row1 = ["😀", "😀", "😀"]
row2 = ["😀", "😀", "😀"]
row3 = ["😀", "😀", "😀"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
location = input("Where do you want to put the treasure? Enter the column and row number\n")
column = int(location[0])
row = int(location[1])
print(column)
print(row)
map[row - 1][column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")