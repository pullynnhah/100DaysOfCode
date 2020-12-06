water_level = int(input('Water level? '))
if water_level > 80:
    print('Drain water')
else:
    print('Continue')
print()

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You an ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
print()

print(height > 120)
print(height == 120)
