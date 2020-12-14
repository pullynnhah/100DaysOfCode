import random
import turtle


class Scoreboard(turtle.Turtle):
    ALIGNMENT = 'center'
    FONT_SCORE = ('Letters for Learners', 22, 'normal')
    FONT_GAME_OVER = ('Letters for Learners', 80, 'bold')
    FONT_GAME_OVER_SCORE = ('Letters for Learners', 50, 'bold')
    COLORS = ['deep pink', 'cyan', 'red', 'violet', 'black',
              'gold', 'blue', 'lawn green', 'salmon']

    FINAL_TEXT = 'GAME OVER'

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('cyan')
        self.score = 0
        self.write_score()

    def write_score(self):
        self.goto(0, 270)
        text = f'Score: {self.score}'
        self.write(text, font=self.FONT_SCORE, align=self.ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(-250, 0)
        self.speed(1)
        for idx in range(len(self.FINAL_TEXT)):
            color = self.COLORS[idx]
            char = self.FINAL_TEXT[idx]
            self.color(color)
            self.write(char, font=self.FONT_GAME_OVER, move=True)
        self.goto(0, -200)
        self.color('orange')
        text = f'Final Score: {self.score}'
        self.write(text, align=self.ALIGNMENT, font=self.FONT_GAME_OVER_SCORE)


