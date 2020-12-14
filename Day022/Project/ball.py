from turtle import Turtle


class Ball(Turtle):
    SCREEN_HEIGHT = 600

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()

        self.is_right = True
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def is_collision_wall(self):
        return abs(self.ycor()) > 290

    def is_collision_paddle(self, paddle):
        return abs(self.xcor()) > 320 and self.distance(paddle) < 50

    def is_collision_right(self):
        return self.xcor() > 380

    def is_collision_left(self):
        return self.xcor() < -380

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
