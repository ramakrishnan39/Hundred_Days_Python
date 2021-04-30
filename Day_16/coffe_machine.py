from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
go_menu = Menu()
go_cm = CoffeeMaker()
go_mm = MoneyMachine()

while is_on:
    choice = input(f" What would you like to have ({go_menu.get_items()}) ? : ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        go_cm.report()
        go_mm.report()
    else:
        ch_item = go_menu.find_drink(choice)
        if ch_item :
            if go_cm.is_resource_sufficient(ch_item):
                if go_mm.make_payment(ch_item.cost):
                    go_cm.make_coffee(ch_item)
