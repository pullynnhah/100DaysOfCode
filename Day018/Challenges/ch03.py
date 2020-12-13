from turtle import Turtle, Screen
from random import shuffle


def calc_angle(sides):
    return 360 / sides


def draw_shape(turtle, length, sides, color):
    turtle.color(color)
    angle = calc_angle(sides)
    for _ in range(sides):
        turtle.fd(length)
        turtle.right(angle)


def set_start_position(turtle, x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


def main():
    tim = Turtle()
    tim.pensize(3)
    set_start_position(tim, -150, 150)

    colors = ['blue', 'cyan', 'red', 'hot pink',
              'gold', 'coral', 'indigo', 'lime']
    shuffle(colors)

    sides = 3
    for color in colors:
        draw_shape(tim, 100, sides, color)
        sides += 1

    screen = Screen()
    screen.exitonclick()


main()
