from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffe = CoffeeMaker()
money = MoneyMachine()

while True:
    drinks = menu.get_items()
    order = input(f"What drink would you like? {drinks} ").lower().strip()
    if order == "off":
        break
    elif order == "report":
        coffe.report()
        money.report()
    else:
        drink_ordered = menu.find_drink(order)
        if drink_ordered == None:
            continue
        
        enough_resources = coffe.is_resource_sufficient(drink_ordered)
        if enough_resources == False:
            continue
        else:
            print(f"It is ${drink_ordered.cost}")
            enough_money = money.make_payment(drink_ordered.cost)

            if enough_money == False:
                continue
            else:
                coffe.make_coffee(drink_ordered)
    
    

    