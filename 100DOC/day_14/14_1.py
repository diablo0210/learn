# Higher Lower Game Project

import random
print("Welcome to the Higher-Lower Game!!!")
from game_data import data
print(data)
from art import logo
print(logo)

life = True
score = 0
while life is True:
    i = random.randint(0, len(data))
    a_name = data[i]['name']
    a_follower = data[i]['follower_count']
    a_description = data[i]['description']
    a_country = data[i]['country']
    print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")

    i = random.randint(0, len(data))
    b_name = data[i]['name']
    b_follower = data[i]['follower_count']
    b_description = data[i]['description']
    b_country = data[i]['country']
    print(f"Against B: {b_name}, a {b_description}, from {b_country}.")

    if a_follower > b_follower:
        greater = "a"
    else:
        greater = "b"
    choice = input("Who has more followers on instagram? 'A' or 'B': ").lower()

    if choice == greater:
        print("You are correct.")
        score += 1
        print(f"Your score is {score}.")
    else:
        print("Incorrect. Game Over!")
        print(f"Your final score is {score}.")
        life = False
