import os
import random
from blackjack_art import logo


deck = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}


def get_card():
    return random.choice(list(deck.keys()))


def calc_score(cards):
    score = 0
    for card in cards:
        score += deck[card]
    if 'A' in cards and score <= 11:
        score += 10
    return score


def get_computer_cards():
    cards = [get_card(), get_card()]
    while calc_score(cards) < 17:
        cards.append(get_card())
    return cards


def blackjack(cards):
    return len(cards) == 2 and calc_score(cards) == 21


def get_winner(result_dict):
    user_score = result_dict['user']['score']
    computer_score = result_dict['computer']['score']
    user_cards = result_dict['user']['cards']
    computer_cards = result_dict['computer']['cards']
    print(f'Your final hand: {user_cards}, final score: {user_score}')
    print(f'Computer final hand: {computer_cards}, final score: {computer_score}')
    print()

    if blackjack(user_cards) and blackjack(computer_cards):
        return 'You and the computer got a Blackjack'
    if blackjack(user_cards):
        return 'User Blackjack. User wins!!!'
    if blackjack(computer_cards):
        return 'Computer Blackjack. User loses!!!'
    if user_score == computer_score:
        return 'Draw'
    if user_score > 21:
        return 'User went over. User loses!!!'
    if computer_score > 21:
        return 'Computer went over. User wins!!!'
    if user_score > computer_score:
        return 'User wins!!!'
    return 'User loses!!!'


def display_cards(user_cards, computer_cards):
    print(f'Your cards: {user_cards}. Current score: {calc_score(user_cards)}')
    print(f'Computer first card: {computer_cards[0]}')
    print()


def game():
    user_cards = [get_card(), get_card()]
    computer_cards = get_computer_cards()
    user_score = calc_score(user_cards)
    computer_score = calc_score(computer_cards)
    display_cards(user_cards, computer_cards)
    more = 'y'
    while more == 'y' and user_score < 21 and computer_score < 21:
        more = input('Do you want one more card? "y" or "n": ')
        if more == 'y':
            user_cards.append(get_card())
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        display_cards(user_cards, computer_cards)

    return {
        'computer': {
            'cards': computer_cards,
            'score': computer_score
        },
        'user': {
            'cards': user_cards,
            'score': user_score
        }
    }


def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')


play = input('Play a game of blackjack? "y" or "n": ')
while play == 'y':
    print(logo)
    result = game()
    print(get_winner(result))
    play = input('Play a game of blackjack? "y" or "n": ')
    clear_screen()
