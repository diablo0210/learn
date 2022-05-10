# To find and output the list of common items from 2 text files

with open("file_1.txt") as file1:
    f1 = file1.readlines()
    f1 = [x.strip() for x in f1]
    print(f1)
with open("file_2.txt") as file2:
    f2 = file2.readlines()
    f2 = [x.strip() for x in f2]
    print(f2)

common = [x for x in f1 if x in f2]
print(common)