def function(*args):
    print(args)
    print(type(args))
    for arg in args:
        print(arg, end=' ')
    print('\n')


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def other_function(*args):
    print(args[0])


function(3, 5, 6)
function(3, 5, 6, 7)

print(add(3, 5, 6))
print(add(3, 5, 6, 2, 1))
print(add(3, 5, 6, 2, 1, 7, 4, 3))
print()

other_function(1, 2, 3)
other_function(-1, 0, 1, 2, 3)
