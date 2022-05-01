import turtle
turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor("orange")

def drawcircle (radius):
    for i in range (15):
        turtle.circle(radius)
        radius=radius+8

def drawdesign ():
    for i in range (15):
        drawcircle(100)
        turtle.right(30)

drawdesign()
turtle.done