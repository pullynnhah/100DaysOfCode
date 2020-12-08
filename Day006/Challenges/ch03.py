# Observation: You need to run the code below on the
# https://reeborg.ca/ website on the ch03.md file.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
