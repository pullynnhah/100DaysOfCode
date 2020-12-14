import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, 'Up')

game_is_on = True
count = 0
car_manager = CarManager()

while game_is_on:
    count += 1
    if count % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()
    time.sleep(0.1)
    screen.update()
    random.shuffle(car_manager.all_cars)
    if player.end_line():
        scoreboard.update_level()
        player.goto_beginning()
        car_manager.update_level()

    if car_manager.check_collision(player):
        game_is_on = False
        scoreboard.game_over()



screen.exitonclick()
