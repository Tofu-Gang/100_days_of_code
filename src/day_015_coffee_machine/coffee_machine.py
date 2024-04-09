
class CoffeeMachine:
    ESPRESSO = "ESPRESSO"
    LATTE = "LATTE"
    CAPPUCCINO = "CAPPUCCINO"

    KEY_WATER = "WATER"
    KEY_COFFEE = "COFFEE"
    KEY_MILK = "MILK"
    KEY_COST = "COST"

    WATER_CAPACITY = 300
    COFFEE_CAPACITY = 100
    MILK_CAPACITY = 200

    PENNY_VALUE = 0.01
    NICKEL_VALUE = 0.05
    DIME_VALUE = 0.1
    QUARTER_VALUE = 0.25

    RECIPES = {
        ESPRESSO: {
            KEY_WATER: 50,
            KEY_COFFEE: 18,
            KEY_MILK: 0,
            KEY_COST: 1.5
        }, LATTE: {
            KEY_WATER: 200,
            KEY_COFFEE: 24,
            KEY_MILK: 150,
            KEY_COST: 2.5
        }, CAPPUCCINO: {
            KEY_WATER: 250,
            KEY_COFFEE: 24,
            KEY_MILK: 100,
            KEY_COST: 3
        }
    }

    def __init__(self):
        """
        The coffee machine has tanks for water and milk and a compartment for coffee and money.
        """

        self._water = 0
        self._milk = 0
        self._coffee = 0
        self._money = 0
        # stores the recipe selected by the user
        self._recipe = None

########################################################################################################################

    def _print_report(self) -> None:
        """
        Prints how much water, milk, coffee and money is in the coffee machine.
        """

        print(f"Water: {self._water}ml")
        print(f"Milk: {self._milk}ml")
        print(f"Coffee: {self._coffee}g")
        print(f"Money: ${self._money}")

########################################################################################################################

    def _fill_everything(self) -> None:
        """
        Fill the water and milk tanks and the coffee compartment.
        """

        self._water = self.WATER_CAPACITY
        self._milk = self.MILK_CAPACITY
        self._coffee = self.COFFEE_CAPACITY
        print("Water, milk and coffee filled.")

########################################################################################################################

    def _insert_money(self, pennies: int, nickels: int, dimes: int, quarters: int) -> bool:
        """
        Insert money to the machine. If it is enough to pay for the coffee, accept it and return change if needed.

        :param pennies: pennies amount
        :param nickels: nickels amount
        :param dimes: dimes amount
        :param quarters: quarters amount
        :return: True if the transaction was successful, False otherwise
        """

        insert_total = sum((pennies * self.PENNY_VALUE,
                            nickels * self.NICKEL_VALUE,
                            dimes * self.DIME_VALUE,
                            quarters * self.QUARTER_VALUE))
        cost = self.RECIPES[self._recipe][self.KEY_COST]

        if insert_total == cost:
            self._money += insert_total
            return True
        elif insert_total > cost:
            change = insert_total - cost
            self._money += cost
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

########################################################################################################################

    def _make_coffee(self) -> None:
        """
        Make the coffee for the user. Deduct what was needed to make the coffee from the machine supplies.
        """

        self._water -= self.RECIPES[self._recipe][self.KEY_WATER]
        self._milk -= self.RECIPES[self._recipe][self.KEY_MILK]
        self._coffee -= self.RECIPES[self._recipe][self.KEY_COFFEE]
        print(f"Here is your {self._recipe.lower()} :) Enjoy!")

########################################################################################################################

    def _can_coffee_be_made(self) -> bool:
        """
        :return: True if there is enough water, milk and coffee for the selected recipe, False otherwise
        """

        return (self.RECIPES[self._recipe][self.KEY_WATER] <= self._water and
                self.RECIPES[self._recipe][self.KEY_MILK] <= self._milk and
                self.RECIPES[self._recipe][self.KEY_COFFEE] <= self._coffee)

########################################################################################################################

    def interact(self) -> None:
        """
        Interact with the coffee machine.
        """

        while True:
            print("What would you like? (espresso/latte/cappuccino or (r)eport or (f)ill):")
            choice = input("> ").strip()

            if choice.upper() in (self.ESPRESSO, self.LATTE, self.CAPPUCCINO):
                self._recipe = choice.upper()

                if self._can_coffee_be_made():
                    print("Please insert coins.")
                    quarters = int(input("How many quarters? "))
                    dimes = int(input("How many dimes?"))
                    nickles = int(input("How many nickles?"))
                    pennies = int(input("How many pennies?"))
                    paid = self._insert_money(pennies, nickles, dimes, quarters)
                    if paid:
                        self._make_coffee()
                else:
                    if self.RECIPES[self._recipe][self.KEY_WATER] > self._water:
                        print("Sorry there is not enough water.")
                    if self.RECIPES[self._recipe][self.KEY_MILK] > self._milk:
                        print("Sorry there is not enough milk.")
                    if self.RECIPES[self._recipe][self.KEY_COFFEE] > self._coffee:
                        print("Sorry there is not enough coffee.")
                self._recipe = None
            elif choice.lower() in ("r", "report"):
                self._print_report()
            elif choice.lower() in ("f", "fill"):
                self._fill_everything()
            elif choice.lower() == "off":
                print("Shutting the coffee machine off.")
                break


########################################################################################################################

def run_program() -> None:
    """
    Interact with the coffee machine.
    """

    CoffeeMachine().interact()


########################################################################################################################
