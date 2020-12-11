import os
import random
import game_art
import game_data


def set_index_list(index_a):
    """This create a list with the indexes of the elements of game_data.data
    removing index_a from it. If index_a is -1 doesn't remove anything."""
    indexes = list(range(len(game_data.data)))
    if index_a != -1:
        indexes.pop(index_a)
    return indexes


def clear_screen():
    """This function will clear the console"""
    os.system("cls" if os.name == 'nt' else 'clear')


def display_person(person):
    """This function will display a person info for
     the game and return its number of followers."""
    name = person['name']
    followers = person['follower_count']
    description = person['description']
    country = person['country']
    print(f'{name}, a(n) {description}, from {country}.')
    return followers


def get_person(indexes, index_a):
    """This function gives a person index."""
    if len(indexes) == 0:
        indexes = set_index_list(index_a)
    return indexes.pop(random.randint(0, len(indexes) - 1))


def compare_choice(followers_a, followers_b, is_a):
    """This function computes if the user has chosen
    correctly. Returning True if yes, False if no."""
    if is_a:
        return followers_a >= followers_b
    return followers_b >= followers_a


def game():
    """This function simulates one round of
    the game and returns the user score."""
    indexes = set_index_list(-1)
    score = 0
    a = get_person(indexes, -1)
    while True:
        b = get_person(indexes, a)
        print(game_art.logo)
        if score != 0:
            print(f"You're right! Current score: {score}")
        print('Compare A:', end=' ')
        followers_a = display_person(game_data.data[a])
        print(game_art.vs)
        print('Against B:', end=' ')
        followers_b = display_person(game_data.data[b])
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct = compare_choice(followers_a, followers_b, choice == 'a')
        clear_screen()
        if correct:
            score += 1
        else:
            return score
        a = b


final_score = game()
print(f"Sorry that's wrong. Final score: {final_score}")
