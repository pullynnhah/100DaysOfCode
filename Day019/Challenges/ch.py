import math
import turtle as t
import random


MIN_X = -250
MIN_Y = -175
MAX_X = 250
MAX_Y = 180


def random_color():
    r = random.randint(0, 127)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def stripe_write(turtle, string, font):
    for character in string:
        turtle.color(random_color())
        turtle.write(character, move=True, font=font)


def draw_rectangle(turtle):
    turtle.fillcolor('white')
    turtle.goto(-250, -180)
    turtle.begin_fill()
    for _ in range(2):
        turtle.fd(500)
        turtle.circle(10, extent=90)
        turtle.fd(350)
        turtle.circle(10, extent=90)
    turtle.end_fill()


def draw_board(turtle, screen):
    turtle.penup()
    turtle.setheading(0)
    turtle.speed(0)
    screen.bgcolor('red')
    draw_rectangle(turtle)
    turtle.goto(-230, 180)
    stripe_write(turtle, "Etch-A-Sketch", ('Letters for Learners', 80, 'normal'))
    turtle.goto(-270, -230)
    turtle.dot(70, 'white')
    turtle.fd(540)
    turtle.dot(70, 'white')
    turtle.goto(0, 0)
    turtle.color('black')
    turtle.pendown()


def move_forwards():
    next_x = tim.xcor() + 5 * math.cos(math.radians(tim.heading()))
    next_y = tim.ycor() + 5 * math.sin(math.radians(tim.heading()))
    if MIN_X <= next_x <= MAX_X and MIN_Y <= next_y <= MAX_Y:
        tim.forward(5)


def move_backwards():
    next_x = tim.xcor() - 5 * math.cos(math.radians(tim.heading()))
    next_y = tim.ycor() - 5 * math.sin(math.radians(tim.heading()))
    if MIN_X <= next_x <= MAX_X and MIN_Y <= next_y <= MAX_Y:
        tim.backward(5)


def turn_clockwise():
    tim.setheading(tim.heading() - 5)


def turn_counter_clockwise():
    tim.setheading(tim.heading() + 5)


def clear_screen():
    tim.penup()
    tim.setheading(0)
    draw_rectangle(tim)
    tim.goto(0, 0)
    tim.fillcolor('black')
    tim.pendown()


tim = t.Turtle()
t.colormode(255)
canvas = t.Screen()
canvas.title('Etch-A-Sketch')

draw_board(tim, canvas)

canvas.listen()
canvas.onkey(key='w', fun=move_forwards)
canvas.onkey(key='s', fun=move_backwards)
canvas.onkey(key='a', fun=turn_counter_clockwise)
canvas.onkey(key='d', fun=turn_clockwise)
canvas.onkey(key='c', fun=clear_screen)

canvas.exitonclick()
