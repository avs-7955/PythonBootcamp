import art
from random import *

NUMBER = randint(1, 100)


print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")


def game(attempts):
    global NUMBER
    if(attempts == 0):
        print(f"You lose! The number was {NUMBER}.")
        return
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    if(guessed_number > NUMBER):
        print("Too high.\nGuess again.")
        game(attempts-1)
    elif(guessed_number < NUMBER):
        print("Too low.\nGuess again.")
        game(attempts-1)
    else:
        print(f"You got it! The answer was {NUMBER}.")


level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if(level == 'easy'):
    game(10)
else:
    game(5)
