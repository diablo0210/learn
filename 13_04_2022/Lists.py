friends = ["sneha", "verma", "rathi", "roshan", "poddar"]
print(friends)

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[-1])
print(friends[-2])
print(friends[1:])
print(friends[2:])
print(friends[3:])
print(friends[1:3])
print(friends[1:5])
print(friends[1:4])
print(friends[:-1])
print(friends[:-2])
friends[1] = "Mike"
print(friends[:-2])
friends[2] = "Bella"
print(friends[:-1])

friends.append("Sonu")
print(friends)

friends.insert(1, "Momo")
print(friends)
#to insert at a specific position

print(friends.index("poddar"))

print(friends.count("sneha"))
#to count the number of times an entry appears in the list

friends.sort()
print(friends)
#to sort the list in ascending order

friends.reverse()
print(friends)
#to reverse the order of the list

friends.remove("Bella")
print(friends)
#to remove a specific entry in the list

enemy = ["Putin", "Modi", "Kim", "Trump"]
friends.extend(enemy)
print(friends)
#to add lists

friends.pop()
print(friends)
#to remove the last element in the list

friends.clear()
print(friends)
# to clear out the whole list