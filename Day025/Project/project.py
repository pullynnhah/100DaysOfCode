import pandas
import turtle

WIDTH_SCREEN = 725
HEIGHT_SCREEN = 491
STATES_COUNT = 50
FONT_STATE = ('Letters for Learners', 12, 'bold')
FONT_GAME_OVER = ('Letters for Learners', 50, 'bold')
QUESTION = "Name an U.S. State:"

data = pandas.read_csv('states.csv')

states = data['state'].tolist()
xs = data['x'].tolist()
ys = data['y'].tolist()

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(WIDTH_SCREEN, HEIGHT_SCREEN)

image = "us_states.gif"
screen.addshape(image)
turtle.shape(image)
turtle.colormode(255)

writer = turtle.Turtle()
writer.hideturtle()
writer.up()

status = 'null'
guessed = []
stop = False
while len(guessed) < 50 or not stop:
    title = f"{len(guessed)}/{STATES_COUNT} States Correct"
    guess = screen.textinput(title=title, prompt=QUESTION).title()
    if guess == 'Exit':
        break
    if guess in states and guess not in guessed:
        guessed.append(guess)
        idx = states.index(guess)
        writer.goto(xs[idx], ys[idx])
        writer.write(guess, font=FONT_STATE, align='center')

states_to_learn = []
for state in states:
    if state in guessed:
        states_to_learn.append(state)

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv('states_to_learn.csv')
