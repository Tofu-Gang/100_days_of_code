from utils import clear_screen


class SecretAuction:
    LOGO = """
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    """

########################################################################################################################

    def __init__(self):
        """
        Initialize the secret auction. Make space for storing bids with the names of bidders.
        """

        self._bids = {}

########################################################################################################################

    def _collect_bid(self) -> None:
        """
        Ask the user for their name and bid value. Store the bid.
        """

        name = input("What is your name? >")
        while True:
            try:
                bid = int(input("What is your bid? >$"))
                self._bids[name] = bid
                break
            except ValueError:
                print("Invalid value. Integer required.")

########################################################################################################################

    def _are_other_bidders(self) -> bool:
        """
        Ask the user whether there are any other bidders.

        :return: True if the auction should continue, False if all bidders made their bids
        """

        while True:
            print("Are there any other bidders? Type \"(y)es\" or \"(n)o\":")
            others = input("> ")

            if others.lower() in ("n", "no"):
                return False
            elif others.lower() in ("y", "yes"):
                return True
            else:
                print("Invalid value. Only \"(y)es\" or \"(n)o\" is permitted.")

########################################################################################################################

    def _print_result(self) -> None:
        """
        After all the bids are collected, print the top bid value and name(s) of the bidder(s). Draw between more
        bidders is possible.
        """

        max_bid = max(self._bids.values())
        max_names = tuple(filter(lambda key: self._bids[key] == max_bid, self._bids.keys()))

        if len(max_names) == 1:
            print(f"The winner is {max_names[0]} with a bid of ${max_bid}.")
        else:
            print(f"Oh no, a draw! Multiple people bid ${max_bid}:")
            print(", ".join(max_names))

########################################################################################################################

    def run_auction(self) -> None:
        """
        Run secret auction. Let all bidders make their bids one by one, then reveal the top bid value and name(s) of the
        bidder(s). Draw between more bidders is possible.
        """

        print(self.LOGO)
        print("Welcome to the secret auction program.")

        while True:
            self._collect_bid()

            if self._are_other_bidders():
                clear_screen()
                continue
            else:
                break

        self._print_result()


########################################################################################################################

def run_program() -> None:
    """
    Run secret auction. Let all bidders make their bids one by one, then reveal the top bid value and name(s) of the
    bidder(s). Draw between more bidders is possible.
    """

    SecretAuction().run_auction()


########################################################################################################################
