with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="w") as file:
    file.write("New text.\n")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
