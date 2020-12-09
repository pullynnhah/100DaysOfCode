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
answer = calc_func(num1, num2)
print(f"{num1} {operation} {num2} = {answer}")
