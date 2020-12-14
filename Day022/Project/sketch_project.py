from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Turtle('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)


def go_up():
    x = right_paddle.xcor()
    y = right_paddle.ycor() + 20
    right_paddle.goto(x, y)


def go_down():
    x = right_paddle.xcor()
    y = right_paddle.ycor() - 20
    right_paddle.goto(x, y)


screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
