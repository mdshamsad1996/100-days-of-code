"""Coffee machine exercise"""

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


current_resource = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}


def process_the_coins():

    """Returns the total coins inserted"""

    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):

    """Return true if order made otherwise return False"""

    if money_recieved < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = round(money_recieved - drink_cost, 2)
    print(f"Here is ${change} in chnage.")
    current_resource["Money"] += drink_cost

    return True


def is_ingredients_sufficient(order_ingredients):

    """Return true if ingridients are suffiecient else return False"""

    for item in order_ingredients:
        if order_ingredients[item] > current_resource[item.capitalize()]:
            print(f"Sorry there is no enough {item}.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):

    """Deduct the required inggredients from cureent resource"""

    for item in order_ingredients:
        current_resource[item.capitalize()] -= order_ingredients[item]
    print(f"Here is your {drink_name} coffe. Enjoy!")


def print_report():
    """Print the current resource"""
    print(f"Water : {current_resource['Water']}ml\n"\
          f"Milk : {current_resource['Milk']}ml\n"\
          f"Coffee : {current_resource['Coffee']}gm\n"\
          f"Money : ${current_resource['Money']}")


if __name__ == '__main__':
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino):")
        if user_input.lower() == 'report':
            print_report()
        elif user_input.lower() == 'off':
            exit()
        else:
            drink = MENU[user_input.lower()]
            if is_ingredients_sufficient(drink['ingredients']):
                payment = process_the_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(user_input.lower(), drink['ingredients'])
