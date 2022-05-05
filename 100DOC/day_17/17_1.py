# Creating a Class
# Adding Method to class
# Method is a function attached to an object

class User:
    def __init__(self, user_id, username):
        # __init__ function is used to initialise class/put the starting values of our attributes
        # print("new user being generated...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "diablo")
# user_1.id = "001"
# user_1.username = "diablo"
print(user_1.username)
print(user_1.id)

user_2 = User("002", "Arya")
# user_2.id = "002"
# user_2.username = "arya"
print(user_2.username)
print(user_2.id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

