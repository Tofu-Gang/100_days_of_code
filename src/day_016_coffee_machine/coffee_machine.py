from .menu import Menu, MenuItem
from .coffee_maker import CoffeeMaker
from .money_machine import MoneyMachine


########################################################################################################################

def run_program() -> None:
    """
    Make coffee machine from the code by Angela Yu.
    """

    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        print(f"What would you like? ({menu.get_items()}):")
        choice = input("> ").strip()

        if choice.lower() in ("r", "report"):
            coffee_maker.report()
            money_machine.report()
        elif choice.lower() in ("f", "fill"):
            coffee_maker.resources["water"] = 300
            coffee_maker.resources["milk"] = 200
            coffee_maker.resources["coffee"] = 100
        elif choice.lower() == "off":
            print("Shutting the coffee machine off.")
            break
        else:
            menu_item = menu.find_drink(choice.lower())

            if menu_item is not None:
                transaction_successful = money_machine.make_payment(menu_item.cost)

                if transaction_successful:
                    coffee_maker.make_coffee(menu_item)


########################################################################################################################
