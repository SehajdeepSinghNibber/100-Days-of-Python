import art

MENU={"Espresso":{
    "ingredients":{
        "water":50,
        "coffee":18,
    },
    "cost":1.5,
    },
    "Latte":{
        "ingredients":{
        "water":200,
        "milk":150,
        "coffee":24,
    },
    "cost":2.5,
    },

    "Cappuccino":{
    "ingredients":{
        "water":250,
        "milk":100,
        "coffee":24,
    },
    "cost":3.0,
    }
    }

profit=0
Resources={
    "water":300,
    "milk":200,
    "coffee":100,
}

def checker(coffee):
    ingredients = MENU[coffee]["ingredients"]
    for item in ingredients:
        if Resources.get(item) < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make_coffee(coffee):
    global profit
    ingredients = MENU[coffee]["ingredients"]
    for item in ingredients:
        Resources[item] -= ingredients[item]
    profit+=MENU[coffee]["cost"]

def money_returned(taken, costs):
    if taken < costs:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(taken - costs, 2)
    print(f"Here is ${change} in change.")
    return True


is_on=True
while is_on:
    print(art.art)
    choice=input("What would you like? (espresso/latte/cappuccino):").title()

    if choice=="False":
        exit()
    elif choice=="Report":

       print(f"Water: {Resources['water']}ml")
       print(f"Milk: {Resources.get('milk', 0)}ml")
       print(f"Coffee: {Resources['coffee']}g")
       print(f"Profit: ${profit}")


    elif choice in MENU:
        if checker(choice):
            Quarter = float(input("Please enter the Quarters: "))
            Dime = float(input("Please enter the Dimes: "))
            Nickel = float(input("Please enter the Nickel: "))
            Penny = float(input("Please enter the Penny: "))

            money_taken=Quarter*0.25+Dime*0.10+Nickel*0.05+Penny*0.01

            cost = MENU[choice]["cost"]
            if money_returned(money_taken, cost):
                make_coffee(choice)
        else:
            continue
    else:
        print("Please enter valid input!")