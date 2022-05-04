# Draw a Turtle Spirograph

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
tim.pensize(2)
tim.speed("fastest")

for x in range(36):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(x*10)
