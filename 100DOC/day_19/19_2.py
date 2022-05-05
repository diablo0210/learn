# Turtle Race
import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)

color_list = ["purple", "blue", "green", "yellow", "orange", "red", "black"]

turtles_list = []
y = 0
for i in range(7):
    t_i = Turtle(shape="turtle")
    turtles_list.append(t_i)
    t_i.penup()
    t_i.color(color_list[i-1])
    y = -150 + i * 50
    t_i.goto(-200, y)

# print(turtles_list)
if user_bet:
    is_race_on = True


while is_race_on:
    for i in turtles_list:
        if i.xcor() > 230:
            is_race_on = False
            winner = i.pencolor()
            if winner == user_bet:
                print(f"{winner} is the winner. You've won!!!")
            else:
                print(f"{winner} is the winner. You've Lost!")
        displacement = random.randint(0, 10)
        i.forward(displacement)


screen.exitonclick()




