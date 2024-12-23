from turtle import Turtle, Screen

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
sides = [3, 4, 5, 6, 7, 8, 9, 10]
timmy.pendown()
for shapes in sides:
    angles = 360/shapes
    for draw in range(shapes):
        timmy.rt(angles)
        timmy.forward(100)


screen = Screen()
screen.exitonclick()
