from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        options = menu.get_items()
        choice = input(f'What would you like? ({options}): ').lower()
        if choice == 'off':
            return
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            coffee = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(coffee):
                if money_machine.make_payment(coffee.cost):
                    coffee_maker.make_coffee(coffee)


coffee_machine()
