# alternative as given in the lecture
import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n"))
comp_choice = random.randint(0, 2)
print(f"The computer chose {comp_choice}")
if user_choice >= 3 or user_choice < 0:
    print("Invalid number. Please Try Again!")
elif user_choice == 0 and comp_choice == 2:
    print("You win!")
elif user_choice == 2 and comp_choice == 0:
    print("You Lost!")
elif comp_choice > user_choice:
    print("You lost!")
elif user_choice > comp_choice:
    print("You Won!")
elif comp_choice == user_choice:
    print("Its a Draw!")
