from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = []
body_pos = [(-40, 0), (-20, 0), (0, 0)]
for pos in body_pos:
    turtle = Turtle('square')
    turtle.penup()
    turtle.goto(pos)
    turtle.color('white')
    snake.append(turtle)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for idx in range(len(snake) - 1, 0, -1):
        x = snake[idx - 1].xcor()
        y = snake[idx - 1].ycor()
        snake[idx].goto(x, y)
    snake[0].forward(20)

screen.exitonclick()
