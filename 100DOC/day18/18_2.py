# Random Walk Project in turtle graphics

import random
from turtle import Turtle, Screen


coco = Turtle()
coco.shape("arrow")
coco.color("red")
coco.speed(0)
coco.pensize(10)


color_list = ["black", "grey", "navy", "blue", "green", "yellow", "deep pink", "red", "dark magenta", "orange"]


x = True
dir = [0, 90, 180, 270]
def random_walk():
    while x is True:
        coco.color(random.choice(color_list))
        coco.forward(20)
        coco.right(random.choice(dir))

random_walk()

screen = Screen()
screen.exitonclick()


