# Observation: You need to run the code below on the
# https://reeborg.ca/ website on the ch01.md file.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for _ in range(6):
    hurdle()
