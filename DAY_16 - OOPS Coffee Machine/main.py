from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

obj_money_machine = MoneyMachine()
obj_coffee_machine = CoffeeMaker()
obj_menu = Menu()

is_on = True

while(is_on):
    options = obj_menu.get_items()
    choice = input(f"What would you like to drink? ({options}): ")
    if (choice == 'off'):
        is_on = False
    elif (choice == 'report'):
        # Printing report
        obj_coffee_machine.report()
        obj_money_machine.report()
    else:
        drink = obj_menu.find_drink(choice)
        if (obj_coffee_machine.is_resource_sufficient(drink)) and (obj_money_machine.make_payment(drink.cost)):
            obj_coffee_machine.make_coffee(drink)
