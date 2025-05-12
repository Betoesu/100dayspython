import wrong_type
def enough_resources(drink, menu, resources):
    ingredients = menu[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry There's Not Enough {item.title()}")
            not_enough = True
            return not_enough
            
        elif ingredients[item] <= resources[item]:
            return
        
        


    
    
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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money": 0
}

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01,
    
}

while True:
    coffe_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    coffe_type = wrong_type.wrong_type(coffe_type,["espresso", "latte", "cappuccino", "report", "off"], "What would you like? (espresso/latte/cappuccino): ", "english")
    


    if coffe_type in ["espresso", "latte", "cappuccino"]:
        not_enough = enough_resources(coffe_type, MENU, resources)
        cost_coffe = MENU[coffe_type]["cost"]

        if not_enough == True:
            continue
        print(f"${cost_coffe}")
        print("Please, Insert coins.")
        
        quarters_coin = float(input("How many quarters: "))
        dimes_coin = float(input("How many dimes: "))
        nickles_coin = float(input("How many nickles: "))
        pennies_coin = float(input("How many pennies: "))

        total = quarters_coin * coins["quarters"] + dimes_coin * coins["dimes"] + nickles_coin * coins["nickles"] + pennies_coin * coins["pennies"]

        if total < cost_coffe:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif total > cost_coffe:
            change = total - cost_coffe
            print(f"Here is ${round(change,2)} in change.")
            print(f"Enjoy your {coffe_type}")
            resources["money"] += cost_coffe
            print(resources)

        else:
            print(f"Enjoy your {coffe_type}")
            resources["money"] += cost_coffe
            print(resources)
    


        
    elif coffe_type == "report":
        print(resources)
    
    elif coffe_type == "off":
        break