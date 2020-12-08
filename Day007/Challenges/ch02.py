import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is: {chosen_word}.')
display = ['_'] * word_length
print(display)

guess = input('Enter a letter: ').lower()
while len(guess) != 1 or not guess.isalpha():
    print("Please enter a single letter!")
    guess = input('Enter a letter: ').lower()

for idx in range(word_length):
    if chosen_word[idx] == guess:
        display[idx] = chosen_word[idx]

print(display)
