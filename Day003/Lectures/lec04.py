a = 12
print(a > 15)
print(a > 10)
print(a > 10 and a < 13)
print(a > 15 and a < 13)
print()

print(not a > 15)
print()

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be OK. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == 'Y':
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

