from turtle import Turtle, Screen
from random import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("forest green")

#drawing a square
"""for i in range(0,4):
    timmy.forward(100)
    timmy.rt(90)"""

#drawing a dashed line
"""for i in range(0,5):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)"""

#drawing multiple shapes from the same origin point
"""sides = [3, 4, 5, 6, 7, 8, 9, 10]
timmy.pendown()
for shapes in sides:
    angles = 180 - ((shapes-2)*180)/shapes
    r = random()
    g = random()
    b = random()
    timmy.pencolor((r,g,b))
    for draw in range(shapes):
        timmy.rt(angles)
        timmy.forward(100)"""

#


screen = Screen()
screen.exitonclick()
