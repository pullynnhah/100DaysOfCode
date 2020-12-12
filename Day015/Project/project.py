import coffee_machine_data as cmd


def report(resources):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']

    print(f'Water: {water}ml')
    print(f'Milk: {milk}ml')
    print(f'Coffee: {coffee}g')
    print(f'Money: ${money:.2f}')


def check_resources(menu, resources, coffee):
    enough_resources = True
    for ingredient in menu[coffee]['ingredients']:
        if menu[coffee]['ingredients'][ingredient] > resources[ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            enough_resources = False
    return enough_resources


def make_coffee(menu, resources, coffee):
    for ingredient in menu[coffee]['ingredients']:
        resources[ingredient] -= menu[coffee]['ingredients'][ingredient]
    resources['money'] += menu[coffee]['cost']


def get_coins():
    print('Please insert coins.')

    coins = int(input('How many quarters? ')) * 0.25
    coins += int(input('How many dimes? ')) * 0.10
    coins += int(input('How many nickels? ')) * 0.05
    coins += int(input('How many pennies? ')) * 0.01

    return coins


def coffee_machine():
    machine_resources = cmd.resources
    while True:
        choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if choice not in ['report', 'off', 'espresso', 'latte', 'cappuccino']:
            print('Invalid option please enter one of the following:')
            print('report - off - espresso - latte - cappuccino')
        elif choice == 'off':
            return
        elif choice == 'report':
            report(machine_resources)
        else:
            keep_going = check_resources(cmd.MENU, machine_resources, choice)
            if keep_going:
                coins = get_coins()

                coin_diff = coins - cmd.MENU[choice]['cost']
                if coin_diff < 0:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    make_coffee(cmd.MENU, machine_resources, choice)
                    if coin_diff != 0:
                        print(f'Here is ${coin_diff:.2f} in change.')
                    print(f'Here is your {choice} ☕. Enjoy!')


coffee_machine()
