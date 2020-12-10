player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(f'potion_strength = {potion_strength}')
        print(f'player_health = {player_health}')

    drink_potion()


# drink_potion()  # NameError
game() 
print(player_health)
