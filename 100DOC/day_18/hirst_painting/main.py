import colorgram
from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# colors = colorgram.extract('image.jpg', 50)
# print(colors)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171),
              (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233),
              (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193),
              (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166),
              (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64), (119, 46, 39),
              (48, 65, 61)]

tim.speed("fastest")
tim.pensize(2)

y = 0
for i in range(10):
    y += 50
    for x in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.setx(0)
    tim.sety(y)
    tim.pendown()

screen = Screen()
screen.exitonclick()

