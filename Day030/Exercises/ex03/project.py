import pandas

data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

while True:
    word = input('Enter an word: ').upper()
    try:
        spelling_word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the english alphabet, please.")
    else:
        break

print(f'The NATO code for {word} is:')
print(' - '.join(spelling_word))
