#Rock Paper Scissors Game
import random
choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, and, 2 for Scissors: "))
if choice == 0:
    print("You chose Rock.")
elif choice == 1:
    print("You chose Paper.")
elif choice == 2:
    print("You chose Scissors.")
else:
    print("Try Again!")

comp = random.randint(0, 2)
if comp == 0:
    print("The computer chose Rock.")
elif comp == 1:
    print("The computer chose Paper.")
elif comp == 2:
    print("The computer chose Scissors.")

if choice == comp:
    print("Its a Draw!")
if choice == 0 and comp == 1:
    print("The Computer Won!")
if choice == 0 and comp == 2:
    print("You Won!")
if choice == 1 and comp == 0:
    print("You Won!")
if choice == 1 and comp == 2:
    print("The Computer Won!")
if choice == 2 and comp == 0:
    print("The Computer Won!")
if choice == 2 and comp == 1:
    print("You Won!")



