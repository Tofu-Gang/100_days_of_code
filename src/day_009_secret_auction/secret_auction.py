from sys import maxsize

from utils import clear_screen

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

def run_program() -> None:
    """

    """

    print(LOGO)
    print("Welcome to the secret auction program.")
    bids = {}

    while True:
        name = input("What is your name? >")
        bid = int(input("What is your bid? >$"))
        bids[name] = bid
        print("Are there any other bidders? Type \"(y)es\" or \"(n)o\":")
        others = input("> ")

        if others.lower() in ("n", "no"):
            break
        elif others.lower() in ("y", "yes"):
            clear_screen()
        else:
            pass

    max_bid = max(bids.values())
    max_names = tuple(filter(lambda key: bids[key] == max_bid, bids.keys()))

    if len(max_names) == 1:
        print(f"The winner is {max_names[0]} with a bid of ${max_bid}.")
    else:
        print(f"Oh no, a draw! Multiple people bid ${max_bid}:")
        print(", ".join(max_names))


########################################################################################################################
