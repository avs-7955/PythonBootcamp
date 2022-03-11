import random
import hangman_art
import hangman_wordlist
import os
def clear(): os.system('cls')  # To clear screen on Windows System


clear()

display = []

chosen_word = random.choice(hangman_wordlist.wordlist)
print(f"The chosen word is {chosen_word}.")
for i in range(len(chosen_word)):
    display.append('_')
print(display)

end_of_game = False
number_of_lives = 6

print(hangman_art.logo)

while not end_of_game:
    guess_letter = input("Guess a letter: ")
    guess_letter = guess_letter.lower()

    clear()

    if guess_letter in display:
        print(f"You've already guessed {guess_letter}.")

    for position in range(len(chosen_word)):
        if (chosen_word[position] == guess_letter):
            display[position] = guess_letter
    print(display)

    if(guess_letter not in chosen_word):
        number_of_lives -= 1
        print(
            f"You guessed {guess_letter}, that's not in the word. You lose a life.")
        if(number_of_lives == 0):
            end_of_game = True
            print("You lose.")
            print(f"The correct word was {chosen_word}.")

    if '_' not in display:
        end_of_game = True
        print("You win...!!!")

    print(hangman_art.stages[number_of_lives])
