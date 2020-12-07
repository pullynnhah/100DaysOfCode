import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input(f"How many symbols would you like? "))
num_numbers = int(input(f"How many numbers would you like? "))

password = []
for num in range(num_letters):
    password.append(random.choice(letters))

for num in range(num_symbols):
    password.append(random.choice(symbols))

for num in range(num_numbers):
    password.append(random.choice(numbers))

# Easy way
easy_password = ''
for char in password:
    easy_password += char

# Hard way
random.shuffle(password)
hard_password = ''
for char in password:
    hard_password += char

print(f'The easy password is: {easy_password}')
print(f'The hard password is: {hard_password}')
