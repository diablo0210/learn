# OOP : Object Oriented Programming

## Constructing a new object:
# import turtle
# timmy = turtle.Turtle()
# or
import turtle
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.color("green")

## Object Attributes : important data that it can keep track of
my_screen = Screen()
print(my_screen.canvheight)

## Object.Method
my_screen.exitonclick()