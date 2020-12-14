import turtle


class Scoreboard(turtle.Turtle):
    FONT = ("Letters for Learners", 24, "normal")

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(-250, 260)
        self.write(f'Level: {self.level}', align='center', font=self.FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over.', align='center', font=self.FONT)
