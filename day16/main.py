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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# Check resources sufficient
def check_resource(coffee):
    for i in MENU[coffee]["ingredients"]:
        if resources[i] < MENU[coffee]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

# Process coins
def process_coin(coffee):
    coin_flag = False
    while not coin_flag:
        print("Please insert coins.")
        quarter_count = int(input("How many quarters?"))
        dimes_count = int(input("How many dimes?"))
        nickles_count = int(input("How many nickles?"))
        pennies_count = int(input("How many pennies?"))

        money_in = 0.25 * quarter_count + 0.1 * dimes_count + 0.05 * nickles_count + 0.01 * pennies_count

        if money_in < MENU[coffee]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            coin_flag = True
            dollar_change = round(money_in - MENU[coffee]["cost"], 2)
            print(f'Here is ${dollar_change} dollars in change.')

def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


def make_coffee(coffee):
    for i in MENU[coffee]["ingredients"]:
        resources[i] -= MENU[coffee]["ingredients"][i]
    resources["money"] += MENU[coffee]["cost"]
    print(f'Here is your {coffee}. Enjoy!☕')


# Prompt user by asking “ What would you like? (espresso/latte/cappuccino)
power_flag = True

while power_flag:
    input_str = input("What would you like? (espresso/latte/cappuccino)").lower()

    if input_str not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
        print("Invaild choice. Please select again!")

    # Turn off the Coffee Machine by entering “ off ” to the prompt
    elif input_str == 'off':
        power_flag = False
        print("Machine is off.")

    # Print report
    elif input_str == 'report':
        print_report()

    else:
        if check_resource(input_str):
            process_coin(input_str)
            make_coffee(input_str)




