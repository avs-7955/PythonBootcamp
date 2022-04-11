MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def make_coffee(order):
    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["milk"] -= MENU[order]["ingredients"]["milk"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    print("Here is your latte. Enjoy!")


def process_coins(order):
    global money
    print("Please insert the coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many penniess?"))
    money_deposited = (quarters * 0.25) + (dimes * 0.10)
    money_deposited += (nickles * 0.05) + (pennies * 0.01)
    (nickles * 0.05) + ((pennies * 0.01))
    if(money_deposited > MENU[order]['cost']):
        money += MENU[order]['cost']
        refund = round((money_deposited - MENU[order]['cost']), 2)
        if(refund > 0):
            print(f"Here is ${refund} dollars in change.")
        make_coffee(order)
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return


flag = 1
while(flag):
    user_input = input(
        "What would you like? (espresso/latte/cappuccino/): ").lower()

    if(user_input == 'report'):
        for resource in resources:
            print(f"{resource.title()}: {resources[resource]}")
        print(f"Money: ${money}")

    elif(user_input != 'report' and user_input != 'off'):
        print(MENU[user_input]['ingredients'])
        if(MENU[user_input]["ingredients"]["water"] < resources["water"]):
            if(MENU[user_input]["ingredients"]["milk"] < resources["milk"]):
                if(MENU[user_input]["ingredients"]["coffee"] < resources["coffee"]):
                    process_coins(user_input)
                else:
                    print("Sorry there is not enough coffee.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough water.")

    elif(user_input == 'off'):
        flag = 0
