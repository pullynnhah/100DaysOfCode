import turtle
import random


class Food(turtle.Turtle):
    FOOD_COLORS = ['red', 'orange', 'yellow', 'green',
                   'dodger blue', 'indigo', 'violet']

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.change_color()
        self.speed('fastest')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.move()

    def move(self):
        self.change_color()
        self.goto(random.randint(-260, 260), random.randint(-260, 260))

    def change_color(self):
        self.color(random.choice(self.FOOD_COLORS))
