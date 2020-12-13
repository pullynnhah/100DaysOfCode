import turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim = turtle.Turtle()
turtle.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()
x = -250
y = 250
tim.goto(x, y)
count = 0
for _ in range(100):
    tim.dot(20, random_color())
    tim.forward(50)
    count += 1
    if count % 10 == 0:
        y -= 50
        tim.goto(x, y)

screen = turtle.Screen()
screen.exitonclick()
