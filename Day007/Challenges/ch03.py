import random


def get_guess():
    user_guess = input('Enter a letter: ').lower()
    while len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter a single letter!")
        user_guess = input('Enter a letter: ').lower()
    return user_guess


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = ['_'] * word_length

while '_' in display:
    print(display)
    guess = get_guess()
    for idx in range(word_length):
        letter = chosen_word[idx]
        if letter == guess:
            display[idx] = letter

print(display)
print('You win!')
