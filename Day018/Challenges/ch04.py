from turtle import Turtle, Screen
from random import shuffle, choice

tim = Turtle()
tim.pensize(5)
tim.speed(0)

colors = ['blue', 'cyan', 'red', 'deep pink',
          'gold', 'coral', 'indigo', 'lime']

angles = [0, 90, 180, 270]

for _ in range(25):
    shuffle(colors)
    for color in colors:
        tim.color(color)
        tim.forward(25)
        tim.setheading(choice(angles))

screen = Screen()
screen.exitonclick()
