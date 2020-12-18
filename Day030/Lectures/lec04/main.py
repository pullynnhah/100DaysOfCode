file = None
try:
    file = open("file.txt")
    dictionary = {"key": "value"}
    print(dictionary["key"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something\n")
except KeyError as error:
    print(f"That key {error} not exist.")
else:
    print(file.read())
finally:
    print("File was closed")
    file.close()
    raise TypeError("This is an Error that I made up.")
