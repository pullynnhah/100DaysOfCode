import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input('Enter a letter: ').lower()
while len(guess) != 1 or not guess.isalpha():
    print("Please enter a single letter!")
    guess = input('Enter a letter: ').lower()

for letter in chosen_word:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')

