# Initial values.
import resource as rs

print(rs.logo)
choice = True
amount=0
res = rs.resources


def transaction(p_option):
    global amount
    print("Please insert coins!")
    coins = {
        "qts": int(input("How many quarters? : ")),
        "dim": int(input("How many dimes? : ")),
        "nkl": int(input("How many nickles? : ")),
        "pen": int(input("How many pennies? : "))
    }
    tot_dol = (
            (coins["qts"] * 0.25) +
            (coins["dim"] * 0.1) +
            (coins["nkl"] * 0.05) +
            (coins["pen"] * 0.01)
    )
    cost = rs.MENU[p_option]["cost"]
    if tot_dol > cost:
        chg = round(tot_dol - cost, 2)
        print(
            f"Please take the change {chg} " )
        amount += cost
        operation(p_option,cost)
    elif tot_dol == cost:
        print("Hey you gave the correct amount! ")
        amount += cost
        operation(p_option,cost)
    else:
        print("Sorry ! Coins are not sufficient ! ")


def operation(po_option, po_cost):
    if po_option == "espresso":
        if res["water"] >= rs.MENU[po_option]["ingredients"]["water"] and res["coffee"] >= rs.MENU[po_option]["ingredients"]["coffee"]:
            res["water"] = res["water"] - rs.MENU[po_option]["ingredients"]["water"]
            res["coffee"] = res["coffee"] - rs.MENU[po_option]["ingredients"]["coffee"]
            print(f"And enjoy your {po_option}")
        else:
            print(f"Sorry there is no sufficient resources to produce {po_option}")
            print(f"Please take your amount {po_cost}")
    else:
        if res["water"] >= rs.MENU[po_option]["ingredients"]["water"] and res["milk"] >= rs.MENU[po_option]["ingredients"]["milk"]  and res["coffee"] >= rs.MENU[po_option]["ingredients"]["coffee"]:
            res["water"] = res["water"] - rs.MENU[po_option]["ingredients"]["water"]
            res["milk"] = res["milk"] - rs.MENU[po_option]["ingredients"]["milk"]
            res["coffee"] =  res["coffee"] - rs.MENU[po_option]["ingredients"]["coffee"]
            print(f"And enjoy your {po_option}")
        else:
            print(f"Sorry there is no sufficient resources to produce {po_option}")
            print(f"Please take your amount {po_cost}")


while choice:
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if option.lower() == "off":
        choice = False
    elif option.lower() == "report":
        print(f"Water : {res['water']}ml")
        print(f"Milk : {res['milk']}ml")
        print(f"Coffee : {res['coffee']}g")
        print(f"Money ${amount}")
    else:
        transaction(option)

