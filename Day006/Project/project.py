# Observation: You need to run the code below on the
# https://reeborg.ca/ website on the project.md file.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def robot_move():
    # The if fix the edge cases
    if right_is_clear() and front_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


while not at_goal():
    robot_move()
