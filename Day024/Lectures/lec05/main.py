with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("New text.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
