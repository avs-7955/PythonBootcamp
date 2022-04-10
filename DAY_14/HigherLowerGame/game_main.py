import game_art
import game_data
import random
import os
def clear(): os.system('cls')


def higher_lower(score):
    clear()
    print(game_art.logo)
    if(score > 0):
        print(f"You're right!!!! \nCurrent score: {score}\n")
    player_a = random.choice(game_data.data)
    print(
        f"Compare A: {player_a['name']}, a {player_a['description']}, from {player_a['country']}.")
    print(game_art.vs)
    player_b = random.choice(game_data.data)
    print(
        f"Compare B: {player_b['name']}, a {player_b['description']}, from {player_b['country']}.")
    if(player_a['follower_count'] > player_b['follower_count']):
        msg = 'A'
    else:
        msg = 'B'

    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    if(user_answer == msg):
        higher_lower(score+1)
    else:
        clear()
        print(game_art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return


higher_lower(0)
