import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(turtle, gap_size):
    rounds = 360 // gap_size
    for _ in range(rounds):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(tim.heading() + gap_size)


tim = t.Turtle()
t.colormode(255)
tim.speed(0)

draw_spirograph(tim, 5)



screen = t.Screen()
screen.exitonclick()
