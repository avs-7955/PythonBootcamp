alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(start_text, letter_shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        cipher_text += alphabet[(position+letter_shift) % 26]
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, letter_shift):
    start_text = ""
    for letter in text:
        position = alphabet.index(letter)
        start_text += alphabet[(position-letter_shift) % 26]
    print(f"The decoded text is {start_text}")


if (direction == 'encode'):
    encrypt(text, shift)
elif(direction == 'decode'):
    decrypt(text, shift)
