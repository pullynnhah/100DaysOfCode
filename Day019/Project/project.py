import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def stripe_write(turtle_object, string, font):
    for character in string:
        turtle_object.color(random_color())
        turtle_object.write(character, move=True, font=font)


t.colormode(255)
screen = t.Screen()
screen.setup(width=500, height=400)
screen.title('Turtle Race')
user_bet = screen.textinput(
    title='Make your bet',
    prompt='Which turtle will win the race? Enter a color of the rainbow: '
)

tim = t.Turtle()
tim.hideturtle()

tim.penup()
tim.goto(-220, 70)
stripe_write(tim, 'Turtle Race', ('MamaeQueNosFaz', 80, 'normal'))

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
y = -170

turtles = []
for idx in range(7):
    turtle = t.Turtle('turtle')
    turtle.color(colors[idx])
    turtle.penup()
    turtle.goto(-230, y)
    turtles.append(turtle)
    y += 40

race_not_over = True
no_winners = True
winner = ''
while race_not_over:
    random.shuffle(turtles)
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 230 and no_winners:
            winner = turtle.pencolor()
            no_winners = False
            race_not_over = False

if winner == user_bet:
    print(f"You've won! The '{winner}' turtle is the winner!")
else:
    print(f"You've lost! The '{winner}' turtle is the winner!")
screen.exitonclick()

