def function(**kwargs):
    print(kwargs)
    print(type(kwargs))


def other_function(**kwargs):
    for key, value in kwargs.items():
        print(f'Key: {key}, Value: {value}')


def another_function(**kwargs):
    print(kwargs['add'])
    print(kwargs['mul'])


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['mul']
    print(f'n is {n}')


function(add='Addition', mul='Multiplication')
print()

other_function(add='Addition', mul='Multiplication')
print()

another_function(add='Addition', mul='Multiplication')
print()

calculate(10, add=10, mul=23)
print()


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


car1 = Car(make='Nissan', model='GT-R', colour='Red', seats='5')
print(car1.make)
print(car1.model)
print(car1.colour)
print(car1.seats)
print()

car2 = Car(make='Nissan', model='Skyline')
print(car2.make)
print(car2.model)
print(car2.colour)
print(car2.seats)
