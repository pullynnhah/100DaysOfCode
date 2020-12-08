from caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == 'decode':
        shift_amount *= -1
    end_text = ''
    for char in start_text:
        if char in alphabet:
            index = (alphabet.index(char) - shift_amount) % len(alphabet)
            end_text += alphabet[index]
        else:
            end_text += char
    print(f'The {cipher_direction}d text is: {end_text}')


def caesar_cipher():
    print("Type 'encode' to encrypt, type 'decode' to decrypt:")
    direction = input()
    print("Type your message:")
    text = input().lower()
    print("Type the shift number:")
    shift = int(input())
    caesar(text, shift, direction)


print(logo)

restart = 'yes'

while restart == 'yes':
    caesar_cipher()
    restart = input('Do you wish to continue? "yes" or "no": ').lower()
print("Goodbye!!!")
