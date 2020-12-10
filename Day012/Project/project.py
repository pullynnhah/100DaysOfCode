import random
import game_art


def eval_guess(secret, guess):
    if guess == secret:
        print(f'You got it! The answer was {secret}')
        return True
    if guess > secret:
        print('Too high.')
    else:
        print('Too low.')
    return False


def guessing_game(secret, attempts):
    for _ in range(attempts):
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        is_guess_correct = eval_guess(secret, guess)
        if is_guess_correct:
            return
        attempts -= 1
    print("You've run out of guesses, you lose.")


def play_game():
    print(game_art.logo)
    secret = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print(f'"{difficulty}" is not an option.')
        print("Please rerun the program and type a VALID option.")
        return
    guessing_game(secret, attempts)


play_game()
