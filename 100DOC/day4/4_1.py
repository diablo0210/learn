# Randomisation
# Random Module

import random
random_integer = random.randint(1, 10)
# generates a random integer between the given range; 1 and 10 both included
print(random_integer)

random_float = random.random()
# generates a random number between 0 and 1; [0.0, 1.0); 1 is not included
print(random_float)

# generating a random float number between 0 and 5
x = random.random()
print(x * 5.0)

# generating a random score between 0 - 100
score = random.randint(0,  100)
print(f"Your score is {score}.")
