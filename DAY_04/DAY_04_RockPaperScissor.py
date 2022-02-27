import random as rd

rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_select = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if(user_select == 0):
    print(rock)
elif(user_select == 1):
    print(paper)
else:
    print(scissors)

signs_list = [rock, paper, scissors]

computer_select = rd.choice(signs_list)

print(computer_select)

index = signs_list.index(computer_select)

if(user_select == 0 and index == 2) or (user_select == 1 and index == 0) or (user_select == 2 and index == 1):
    print("You win!!!")
elif(user_select == index):
    print("It's a draw!")
else:
    print("You lose.")
