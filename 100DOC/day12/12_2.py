# Guess the number Game
import random
from numbergame_art import art
print(art)

def game(attempts):
    number = random.randint(0, 100)
    # print(number)
    while attempts > 0:
        guess = int(input(f"You have {attempts} attempts remaining. Make a guess: "))
        if guess > number:
            print("Too High!\n")
            attempts -= 1
        elif guess < number:
            print("Too Low!\n")
            attempts -= 1
        elif guess == number:
            print("Yay! You've got it right. You Win!!!")
            return
    if attempts == 0:
        print("No more attempts left. You Lose.")
    else:
        print("Game Over.")

print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty level. 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
    # print("You have 10 attempts.")
    game(attempts)
elif difficulty == "hard":
    attempts = 5
    # print("You have 5 attempts.")
    game(attempts)
else:
    print("Invalid input.")