from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

if __name__ =='__main__': 
    is_on = True
    while is_on:
        options = menu.get_items()
        user_input = input(f"What would you like? ({options}) ")
        if user_input.lower() == 'report':
            coffee_maker.report()
            money_machine.report()

        elif user_input.lower() == 'off':
            is_on = False
            
        else:

            drink = menu.find_drink(user_input.lower())

            if drink is None:
                is_on = False

            elif coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):

                coffee_maker.make_coffee(drink)


        
