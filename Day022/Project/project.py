from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    collided_horizontal_wall = ball.is_collision_wall()
    collided_right = ball.is_collision_right()
    collided_left = ball.is_collision_left()
    collided_left_paddle = ball.is_collision_paddle(left_paddle)
    collided_right_paddle = ball.is_collision_paddle(right_paddle)

    if collided_horizontal_wall:
        ball.bounce_y()
    if collided_left_paddle or collided_right_paddle:

        ball.bounce_x()
    if collided_left or collided_right:
        ball.reset_position()
        if collided_left:
            scoreboard.right_score += 1
        else:
            scoreboard.left_score += 1
        scoreboard.write_score()
    if scoreboard.is_game_over():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
