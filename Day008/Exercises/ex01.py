# Write your code below this line
import math


def paint_calc(height, width, cover):
    cans = math.ceil(height * width / cover)
    cans_name = 'can'
    if cans != 1:
        cans_name += 's'
    print(f"You'll need {cans} {cans_name} of paint")


# Don't change the code below
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
