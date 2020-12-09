def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = int(input("What's the first number? "))
for symbol in operations:
    print(symbol, end=' ')
print()
operation = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number? "))

calc_func = operations[operation]
first_answer = calc_func(num1, num2)
print(f"{num1} {operation} {num2} = {first_answer}")

operation = input("Pick another operation:  ")
num3 = int(input("What's the next number? "))
calc_func = operations[operation]
# second_answer = calc_func(calc_func(num1, num2), num3)
second_answer = calc_func(first_answer, num3)
print(f"{first_answer} {operation} {num2} = {second_answer}")

