import art
import os
def clear(): os.system('cls')  # To clear screen on Windows System


flag = True
bid_dictionary = {}
print(art.logo)
print("Welcome to the secret auction program.")
while(flag):
    name = input(f"What is your name?: ")
    bid_Amount = int(input(f"What's your bid?: $"))
    bid_dictionary[name] = bid_Amount
    flag = input(
        f"Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if (flag == "no"):
        flag = False
    clear()


value = 0
winner_name = ''
for bidder in bid_dictionary:
    if(value < bid_dictionary[bidder]):
        value = bid_dictionary[bidder]
        winner_name = bidder

print(f"The winner of the action is {winner_name} by betting ${value}.")
