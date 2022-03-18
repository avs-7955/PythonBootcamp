import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

status = "yes"


def caesar(start_text, letter_shift, direction):
    converted_text = ""
    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            if(direction == 'encode'):
                converted_text += alphabet[(position+letter_shift) % 26]
            else:
                converted_text += alphabet[(position-letter_shift) % 26]
        else:
            converted_text += character

    print(f"The {direction}d text is {converted_text}")


while(status == "yes"):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    status = input(
        "Type 'yes' if you wanna go again. Otherwise type 'no'.\n").lower()

print("Goodbye! See ya later!!")
