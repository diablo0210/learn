#Python Lists
# Understanding the offset and appending items to Lists

# List is a data structure; it is a way of organising and storing data(usually grouped or data having some relation) in python

states = ["Rajasthan", "Uttar Pradesh", "Madhya Pradesh", "Bihar", "Delhi", "Punjab", "Goa"]
print(states)
print(states[0])
print(states[1])
print(states[2])
print(states[-1])
print(states[-2])

# altering the list
states[2] = "Manipur"
print(states)

# adding single items to the list using append
states.append("Tripura")
print(states)

# adding multiple items using extend
states.extend(["J&K", "Haryana", "Uttaranchal"])
print(states)

# reversing the order
states.reverse()
print(states)

# sorting
states.sort()
print(states)

# counting the number of times an item appears in the list
print(states.count("Bihar"))

# to get the index of an item in the list
print(states.index("Punjab"))

# to pop out the last item in the list
states.pop()
print(states)


# to clear out the list
states.clear()
print(states)
