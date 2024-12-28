from turtle import Turtle, Screen
import random

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
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor((r,g,b))
    for draw in range(shapes):
        timmy.rt(angles)
        timmy.forward(100)"""

#random walk program
timmy.pensize(5)
direction = [0, 90, 180, 270]
count = 0
for _ in range(0,200):
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor((r,g,b))
    timmy.seth(random.choice(direction))
    timmy.forward(20)



screen = Screen()
screen.exitonclick()
