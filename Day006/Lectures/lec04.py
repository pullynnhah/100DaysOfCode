# Observation: You need to run the code below on the
# https://reeborg.ca/ website on the lec04.md file.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()
