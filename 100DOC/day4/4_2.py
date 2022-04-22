#HEADS OR TAILS
#  A virtual coin toss programme
import random

toss = random.randint(0, 1)
if toss == 0:
    print("HEADS")
else:
    print("TAILS")