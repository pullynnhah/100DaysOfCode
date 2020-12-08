alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == 'decode':
        shift_amount *= -1
    end_text = ''
    for letter in start_text:
        index = (alphabet.index(letter) - shift_amount) % len(alphabet)
        end_text += alphabet[index]
    print(f'The {cipher_direction}d text is: {end_text}')


print("Type 'encode' to encrypt, type 'decode' to decrypt:")
direction = input()
print("Type your message:")
text = input().lower()
print("Type the shift number:")
shift = int(input())

caesar(text, shift, direction)
