from turtle import Turtle, Screen

tim = Turtle()

for _ in range(15):
    tim.fd(10)
    tim.up()
    tim.fd(10)
    tim.down()

screen = Screen()
screen.exitonclick()
