from turtle import Turtle, Screen

tim = Turtle()

for _ in range(4):
    tim.pencolor()
    tim.fd(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()
