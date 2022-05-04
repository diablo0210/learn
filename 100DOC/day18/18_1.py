# Understanding Turtle graphics
import random
from turtle import Turtle, Screen
# from turtle import *
## import* is used to import everything in that module; its not a very good idea to do this

##  aliasing a module
# import turtle as t
# coco = t.Turtle()

coco = Turtle()
coco.shape("arrow")
coco.color("red")
coco.speed(8)

# for _ in range(4):
#     coco.forward(100)
#     coco.right(90)

# for i in range(10):
#     coco.forward(10)
#     coco.penup()
#     coco.forward(10)
#     coco.pendown()


# for sides in range(3, 11):
#     angle = (360 / sides)
#     x = 0
#     while x < sides:
#         x += 1
#         coco.forward(100)
#         coco.right(angle)

color_list = ["navy", "blue", "lime green", "yellow", "deep pink", "red", "dark magenta", "spring green"]
def draw_shape(sides):
    num_sides = sides
    angle = (360 / num_sides)
    coco.color(random.choice(color_list))
    x = 0
    while x < num_sides:
        x += 1
        coco.forward(100)
        coco.right(angle)

for i in range(3,10):
    draw_shape(i)


# import heroes
# print(heroes.gen())