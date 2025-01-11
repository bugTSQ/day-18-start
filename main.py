from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
timmy.color("forest green")
timmy.speed(0)
screen = Screen()

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
"""timmy.pensize(5)
direction = [0, 90, 180, 270]
count = 0
for _ in range(0,200):
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor((r,g,b))
    timmy.seth(random.choice(direction))
    timmy.forward(20)"""

#Draw a spirograph
"""for _ in range(72):
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor((r, g, b))
    timmy.circle(100)
    timmy.rt(5)"""

#Hirsch painting
screen.colormode(255)
timmy.penup()
color_list = []
count = 0
colors = colorgram.extract("hirstspotpainting.png", 10)

for i in range(10):
    temp_colors = colors[i]
    color_code = temp_colors.rgb
    color_list.append((color_code.r,color_code.g,color_code.b))


y_set = -300
x_set = -300
timmy.goto(x_set,y_set)
displace = 40

for y in range(16):
    for x in range(16):
        timmy.color(random.choice(color_list))
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        x_set += displace
        timmy.goto(x_set,y_set)
    y_set += displace
    x_set = -300
    timmy.goto(x_set, y_set)




#move to point
#draw circle
#fill color




screen.exitonclick()
