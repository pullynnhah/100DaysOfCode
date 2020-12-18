import pandas

data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

word = input('Enter an word: ').upper()

spelling_word = [nato_dict[letter] for letter in word]

print(f'The NATO code for {word} is:')
print(' - '.join(spelling_word))
