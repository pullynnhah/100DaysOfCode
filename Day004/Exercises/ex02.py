import random

names_string = input("Give me everybody's names, separated by a space. ")
names = names_string.split()

index = random.randint(0, len(names) - 1)
print(f'{names[index]} is going to buy the meal today!')
