import wrong_type

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01,
}


def enough_resources(drink, menu, resources):
    ingredients = menu[drink]["ingredients"]
    not_enough = False
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry there's not enough {item.title()}.")
            not_enough = True
    return not_enough


def make_coffee(drink, menu, resources):
    ingredients = menu[drink]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]


def get_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    pennies = float(input("How many pennies: "))
    total = (quarters * coins["quarters"] +
             dimes * coins["dimes"] +
             nickles * coins["nickles"] +
             pennies * coins["pennies"])
    return total


def process_payment(total, cost):
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
    return True


def print_report(resources):
    print("Resources Report:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def main():
    while True:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        coffee_type = wrong_type.wrong_type(
            coffee_type,
            ["espresso", "latte", "cappuccino", "report", "off"],
            "What would you like? (espresso/latte/cappuccino): ",
            "english"
        )

        if coffee_type == "off":
            break
        elif coffee_type == "report":
            print_report(resources)
        elif coffee_type in MENU:
            if enough_resources(coffee_type, MENU, resources):
                continue

            cost = MENU[coffee_type]["cost"]
            print(f"The cost is: ${cost}")
            total_inserted = get_coins()

            if not process_payment(total_inserted, cost):
                continue

            make_coffee(coffee_type, MENU, resources)
            resources["money"] += cost
            print(f"Enjoy your {coffee_type} ☕\n")


if __name__ == "__main__":
    main()
