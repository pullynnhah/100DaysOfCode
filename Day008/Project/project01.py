alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    encrypt_text = ''
    for letter in plain_text:
        index = (alphabet.index(letter) + shift_amount) % len(alphabet)
        encrypt_text += alphabet[index]
    print(f'The encoded text is: {encrypt_text}')


print("Type 'encode' to encrypt, type 'decode' to decrypt:")
direction = input()
print("Type your message:")
text = input().lower()
print("Type the shift number:")
shift = int(input())

if direction == 'encode':
    encrypt(text, shift)


