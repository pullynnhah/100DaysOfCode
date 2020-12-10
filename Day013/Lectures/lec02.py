# Reproduce the Bug:
# 2 bugs will happen because of a off by one error
# dice_num will never have a value of 0 and when it
# has a value of 6 dice_imgs[dice_num] will cause
# a IndexError

# from random import randint
#
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# from random import randint
#
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[6]) # IndexError

from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
