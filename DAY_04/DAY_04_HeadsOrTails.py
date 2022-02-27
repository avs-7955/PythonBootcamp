import random
print("Welcome to the coin-toss program.")

choice = random.randint(1, 2)
# Using the randint from the random module to get the random number.
# randint() = integer output inclusive of the numbers inside the bracket.
# random() = float, output from 0.0000000... - 0.999999....
if(choice == 1):
    print("Heads")
else:
    print("Tails")
