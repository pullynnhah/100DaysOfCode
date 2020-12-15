path = "/home/paula/PycharmProjects/100DaysOfCode/Day024/Lectures/lec07/Desktop"
with open(f'{path}/my_file.txt') as file:
    contents = file.read()
    print(contents)

with open("../../Lectures/lec07/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
