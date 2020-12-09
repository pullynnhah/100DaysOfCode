import calc_art


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


def calculator():
    num1 = float(input("What's the first number? "))
    user_choice = 'y'
    while user_choice == 'y':
        for symbol in operations:
            print(symbol, end=' ')
        print()
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        calc_func = operations[operation]
        result = calc_func(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        print(f"Type 'y' to continue calculating with {result},")
        print(f"'n' to start a new calculation: ")
        user_choice = input()
        if user_choice == 'n':
            calculator()
        num1 = result


print(calc_art.logo)
calculator()
