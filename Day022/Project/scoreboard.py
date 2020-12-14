from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.write_score()
        self.write_score()
        self.draw_middle_line()

    def write_score(self):
        self.clear()
        self.goto(-160, 160)
        self.write(self.left_score, font=('MamaeQueNosFaz', 80, 'bold'))
        self.goto(100, 160)
        self.write(self.right_score, font=('MamaeQueNosFaz', 80, 'bold'))

    def draw_middle_line(self):
        self.goto(0, -320)
        self.pencolor('white')
        self.pensize(3)
        self.setheading(90)
        while self.ycor() <= 300:
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()

    def is_game_over(self):
        return self.left_score > 1 or self.right_score > 1

    def game_over(self):
        self.goto(0, 0)
        self.color('Hot Pink')
        self.write('Game Over.', align='center', font=('Letters for Learners', 60, 'bold'))
        self.goto(0, -100)
        self.color('Gold')
        if self.left_score > self.right_score:
            self.write('Left Player wins', align='center', font=('Letters for Learners', 60, 'bold'))
        else:
            self.write('Right Player wins', align='center', font=('Letters for Learners', 60, 'bold'))
