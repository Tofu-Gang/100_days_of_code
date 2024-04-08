
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

        """

        self._water = 0
        self._milk = 0
        self._coffee = 0
        self._money = 0
        self._recipe = None

########################################################################################################################

    def _print_report(self) -> None:
        """

        """

        print(f"Water: {self._water}ml")
        print(f"Milk: {self._milk}ml")
        print(f"Coffee: {self._coffee}g")
        print(f"Money: ${self._money}")

########################################################################################################################

    def _fill_everything(self) -> None:
        """

        """

        self._water = self.WATER_CAPACITY
        self._milk = self.MILK_CAPACITY
        self._coffee = self.COFFEE_CAPACITY
        print("Water, milk and coffee filled.")

########################################################################################################################

    def _insert_money(self, pennies: int, nickels: int, dimes: int, quarters: int) -> bool:
        """

        :param pennies:
        :param nickels:
        :param dimes:
        :param quarters:
        :return:
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

        """

        self._water -= self.RECIPES[self._recipe][self.KEY_WATER]
        self._milk -= self.RECIPES[self._recipe][self.KEY_MILK]
        self._coffee -= self.RECIPES[self._recipe][self.KEY_COFFEE]
        print(f"Here is your {self._recipe.lower()} :) Enjoy!")

########################################################################################################################

    def _can_coffee_be_made(self) -> bool:
        """

        :return:
        """

        return (self.RECIPES[self._recipe][self.KEY_WATER] <= self._water and
                self.RECIPES[self._recipe][self.KEY_MILK] <= self._milk and
                self.RECIPES[self._recipe][self.KEY_COFFEE] <= self._coffee)

########################################################################################################################

    def operate(self) -> None:
        """

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
                    self._recipe = None
                else:
                    if self.RECIPES[self._recipe][self.KEY_WATER] > self._water:
                        print("Sorry there is not enough water.")
                    if self.RECIPES[self._recipe][self.KEY_MILK] > self._milk:
                        print("Sorry there is not enough milk.")
                    if self.RECIPES[self._recipe][self.KEY_COFFEE] > self._coffee:
                        print("Sorry there is not enough coffee.")
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

    """

    CoffeeMachine().operate()


########################################################################################################################
