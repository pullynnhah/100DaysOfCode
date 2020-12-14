import turtle
import random


class Car(turtle.Turtle):
    COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    STARTING_MOVE_DISTANCE = 5
    MOVE_INCREMENT = 10

    def __init__(self):
        super().__init__()
        self.color(random.choice(self.COLORS))
        self.shape('square')
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(300, random.randint(-250, 250))
        self.level = 1

    def move(self, level):
        self.forward(self.STARTING_MOVE_DISTANCE + (
                    level - 1) * self.MOVE_INCREMENT)

    def check_car_collision(self, player):
        return self.distance(player) < 20


class CarManager:
    def __init__(self):
        self.level = 1
        self.all_cars = []

    def create_car(self):
        self.all_cars.append(Car())

    def update_level(self):
        self.level += 1

    def move_cars(self):
        for car in self.all_cars:
            car.move(self.level)

    def check_collision(self, player):
        for car in self.all_cars:
            if car.check_car_collision(player):
                return True
        return False
