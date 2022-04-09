import random
import art
import os
def clear(): os.system('cls')


card_values = {
    'A': 11,
    'K': 10,
    'J': 10,
    'Q': 10,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
}
cards_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'K', 'Q']


def drawing_cards(times):
    cards = []
    for i in range(times):
        cards.append(random.choice(cards_list))
        i = i + 1

    # print(cards)                                       for debugging
    return cards


def sum_of_cards(dealt_cards):
    sum = 0
    for indiv_cards in dealt_cards:
        sum = sum + card_values[indiv_cards]
        # print(indiv_cards)                             for debugging
    return sum


flag = ''
flag = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
if (flag == 'y'):
    clear()
    print(art.logo)
    user_cards = drawing_cards(2)
    print(f"Your cards: {user_cards}")
    user_sum = sum_of_cards(user_cards)
    print(user_sum)

    dealer_cards = drawing_cards(2)
    print(f"Computer's first card: {dealer_cards[0]}")
    dealer_sum = sum_of_cards(dealer_cards)
    print(dealer_sum)
    next_chance = input("Type 'y' to get another card, type 'n'to pass:")
    if (next_chance == 'y'):
        draw_extra = (drawing_cards(1))
        user_cards.append(draw_extra[0])
        draw_extra = (drawing_cards(1))
        dealer_cards.append(draw_extra[0])

        user_sum = sum_of_cards(user_cards)
        print(user_cards)
        dealer_sum = sum_of_cards(dealer_cards)
        print(dealer_cards)

        if (user_sum > 21):
            print("You lose!")
        elif(dealer_sum > 21):
            print("You win! The dealer got busted!")
        else:
            next_chance = input(
                "Type 'y' to get another card, type 'n'to pass:")
            if(next_chance == 'n'):
                if(user_sum > dealer_sum):
                    print("You win!!!! You got more than dealer.")
                else:
                    print("You lost!! The dealer got more than you...")

else:
    print("Sorry to see you go!")


# sum = card_values[cards[0]] + card_values[cards[1]]

# if sum > 21:
#     drawing_cards()
