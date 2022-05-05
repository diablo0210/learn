# Hangman game (my version)
import random
from hangman_words import word_list

chosen_word = random.choice(word_list)

display = []
for i in chosen_word:
    display.append("_")

life = 10
while '_' in display and life > 0:
    guess = input("Guess a letter in the word: ").lower()
    y = 0
    for i in chosen_word:
        if guess == i:
            display[y] = guess
        y += 1

    if guess not in chosen_word:
        print(f"Sorry, '{guess}' is not present in the word. You lose a life.")
        life -= 1
        print(f"You now have {life} lives remaining.")
    print(display)
if life == 10:
    print("Yay, You Won!!!")
else:
    print(f"Sorry, Game Over! The word was {chosen_word.upper()}.")
