def create_enemy():
    game_level = 3
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)


create_enemy()
# print(new_enemy)  # NameError
