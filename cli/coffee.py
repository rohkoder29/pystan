#!/usr/bin/env python3

# creating the menu
# ingredients values in grams
# cost in dollars

MENU = {
    "espresso": {"ingredients": {"coffee": 20, "water": 50}, "cost": 1.75},
    "latte": {
        "ingredients": {"coffee": 25, "water": 150, "milk": 100},
        "cost": 2.75,
    },
    "capuccino": {
        "ingredients": {"coffee": 25, "water": 180, "milk": 100},
        "cost": 3.25,
    },
}

RESOURCES = {"coffee": 50, "water": 300, "milk": 200, "money": 0}

coffee_type = input(
    "What would you like? (espresso, latte, capuccino)? "
).lower()


def enough_coffe():
    return MENU[coffee_type]["ingredients"]["coffee"] < RESOURCES["coffee"]


def enough_water():
    return MENU[coffee_type]["ingredients"]["water"] < RESOURCES["water"]


def enough_milk():
    return MENU[coffee_type]["ingredients"]["milk"] < RESOURCES["milk"]


dollar = float(input("How many dollars do you have? "))


def enough_money():
    if isinstance(dollar, (float, int)):
        return dollar > MENU[coffee_type]["cost"]
    else:
        print("Bad entry.")


def coffee_machine_ok(coffee_type):
    if not enough_coffe():
        print(f"Not enough coffee to make a {coffee_type.title()}.")
        return False
    elif not enough_water():
        print(f"Not enough water to make a {coffee_type.title()}.")
        return False
    elif coffee_type != "espresso" and not enough_milk():
        print(f"Not enough milk to make a {coffee_type.title()}.")
        return False
    else:
        print("Okay, everything good. We can proceed.")
        return True


def coffee_shop(coffee_type, dollar):
    if coffee_type.strip() in ["espresso", "latte", "capuccino"]:
        if enough_money():
            if coffee_machine_ok(coffee_type):
                print(
                    "Okay give us a second while we are processing your command."
                )
            else:
                print("Sorry. We can't process your command at the moment.")
        else:
            print(
                f"Sorry. You don't have enough money to buy a {coffee_type.title()}."
            )
            buy_instead = [
                item for item in MENU if dollar >= MENU[item]["cost"]
            ]
            print(f"But you can buy {(buy_instead)} instead.")
    else:
        print("Sorry. We don't have that type of coffee.")


coffee_shop(coffee_type, dollar)
