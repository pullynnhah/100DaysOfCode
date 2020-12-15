# Observation: You need to run the codes below on the https://reeborg.ca/
# More info is at the lec04.md file

# First
move()
move()
move()
turn_left()
move()
move()
move()

# Second
move()
move()
turn_left()
turn_left()
move()
move()
turn_left()
turn_left()


# Third
def move_twice():
    move()
    move()


def turn_around():
    turn_left()
    turn_left()


move_twice()
turn_around()
move_twice()
turn_around()


# Forth
def turn_right():
    turn_left()
    turn_left()
    turn_left()


turn_right()


# Fifth
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def draw_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


draw_square()
