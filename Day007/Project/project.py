import random

import hangman_art
import hangman_words


def get_guess():
    user_guess = input('Enter a letter: ').lower()
    while len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter a single letter!")
        user_guess = input('Enter a letter: ').lower()
    return user_guess


print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

# Create blanks
display = ['_'] * word_length
letters_guessed = []
print(f"{' '.join(display)}")
while '_' in display and lives != 0:
    guess = get_guess()
    if guess in letters_guessed:
        print(f"Ops! You've guessed letter: '{guess}' before.")
    elif guess not in chosen_word:
        print(f"Ops! Letter: '{guess}' is not in the word.")
        lives -= 1
    else:
        for idx in range(word_length):
            letter = chosen_word[idx]
            if letter == guess:
                display[idx] = letter
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])

if lives == 0:
    print(hangman_art.loser)
    print(f'The word was: {chosen_word}!')
else:
    print(hangman_art.winner)



