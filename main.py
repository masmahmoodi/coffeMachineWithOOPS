from menu import Menu
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

off = False

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

while not off:
    option = menu.get_items()
    choice = input(f"what would you like ({option}) ")
    if choice == "off":
        off = True
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
#
