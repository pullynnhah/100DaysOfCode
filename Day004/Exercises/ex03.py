# Don't change the code below
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map_ = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Write your code below this row
y = int(position[0]) - 1
x = int(position[1]) - 1
map_[x][y] = 'X'

# Don't change the code below
print(f"{row1}\n{row2}\n{row3}")
