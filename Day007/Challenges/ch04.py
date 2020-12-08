import random


def get_guess():
    user_guess = input('Enter a letter: ').lower()
    while len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter a single letter!")
        user_guess = input('Enter a letter: ').lower()
    return user_guess


stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
          r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
          r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
          r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
          r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
          r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
          r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ['_'] * word_length

while '_' in display and lives != 0:
    guess = get_guess()
    if guess not in chosen_word:
        lives -= 1
    else:
        for idx in range(word_length):
            letter = chosen_word[idx]
            if letter == guess:
                display[idx] = letter
    print(f"{' '.join(display)}")
    print(stages[lives])

if lives == 0:
    print('You lose!')
else:
    print('You win!')



