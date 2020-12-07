import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
print()

print(my_module.pi)
print()

random_float = random.random()
print(random_float)
print(random_float * 5)
print()

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
