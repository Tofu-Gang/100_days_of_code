########################################################################################################################

def run_program() -> None:
    """

    """

    # 3 flavours
    # - Espresso (50ml water, 18g coffee) $1.50
    # - Latte (200ml water, 24g coffee, 150ml milk) $2.50
    # - Cappuccino (250ml water, 24g coffee, 100ml milk) $3.00
    # the machine has 300ml water, 200ml milk and 100g of coffee
    # coins operated
    # - penny (1 cent)
    # - nickel (5 cents)
    # - dime (10 cents)
    # - quarter (25 cents)

    print("What would you like? (espresso/latte/cappuccino or report):")

    # print report
    print("Water: 300ml")
    print("Milk: 200ml")
    print("Coffee: 100g")
    print("Money: $0")

    # check if the resources are sufficient
    print("Sorry there is not enough water.")

    # process coins
    print("Please insert coins.")
    print("How many quarters?")
    print("How many dimes?")
    print("How many nickles?")
    print("How many pennies?")

    print("Sorry that's not enough money. Money refunded.")

    print("Here is $2.14 in change.")
    print("Here is your espresso :) Enjoy!")


########################################################################################################################
