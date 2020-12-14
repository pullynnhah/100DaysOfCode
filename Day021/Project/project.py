from turtle import Screen
from time import sleep

from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 10:
        food.move()
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall.
    collide_with_wall = snake.collision_with_wall(width=WIDTH, height=HEIGHT)

    # Detect collision with tail.
    collide_with_tail = snake.collision_with_tail()

    # Test any collision
    if collide_with_wall or collide_with_tail:
        game_is_on = False
        score_board.game_over()


screen.exitonclick()
