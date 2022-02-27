import random

names = input("Give me everybody's names, seperated by a comma.\n")
name_list = names.split(", ")
# Splitting the string obtained giving the seperator in the bracket.

random_choice = random.randint(0, len(name_list)-1)
# We are subtracting 1 because, the indexes start from 0.

print(f"{name_list[random_choice]} name's has been selected!!!")

# choice function in random module selects elemts from a list randomly.
# random_choice = random.choice(names_list)
