from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_down(self):
        x = self.xcor()
        y = self.ycor() - 20
        if y > -250:
            self.goto(x, y)

    def go_up(self):
        x = self.xcor()
        y = self.ycor() + 30
        if y < 250:
            self.goto(x, y)
