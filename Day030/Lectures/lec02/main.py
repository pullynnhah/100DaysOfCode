# FileNotFound
try:
    file = open("file.txt")
except:
    file = open("file.txt", "w")
    file.write("Something\n")
