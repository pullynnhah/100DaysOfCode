import turtle


class Player(turtle.Turtle):
    STARTING_POSITION = (0, -280)
    MOVE_DISTANCE = 10
    FINISH_LINE_Y = 280

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.up()
        self.goto_beginning()

    def goto_beginning(self):
        self.goto(self.STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(self.MOVE_DISTANCE)

    def end_line(self):
        return self.ycor() > self.FINISH_LINE_Y




