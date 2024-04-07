from random import choice
from typing import Dict

from .data import DATA

LOGO = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

VS = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


########################################################################################################################

def _print_comparison(data_first: Dict[str, str | int], data_second: Dict[str, str | int]) -> None:
    """
    Print the compare display for the user. Include all available data except for the second subject follower count.

    :param data_first: first subject to compare follower count (revealed)
    :param data_second: second subject to compare follower count (hidden)
    """

    name_first = data_first["name"]
    description_first = data_first["description"]
    country_first = data_first["country"]
    follower_count_first = data_first["follower_count"]
    print(f"{name_first}, a {description_first} from {country_first}, has {follower_count_first} followers.")
    print(VS)
    name_second = data_second["name"]
    description_second = data_second["description"]
    country_second = data_second["country"]
    print(f"{name_second}, a {description_second} from {country_second}, has how many followers?")


########################################################################################################################

def _get_user_comparison() -> str:
    """
    :return: user comparison choice, any from (h, higher, l, lower)
    """

    while True:
        print("Type \"(h)igher\" or \"(l)ower\":")
        comparison = input("> ").strip().lower()

        if comparison in ("h", "higher", "l", "lower"):
            return comparison
        else:
            print("Invalid value. Try again.")


########################################################################################################################

def run_program() -> None:
    """
    Play the Higher/Lower game.
    """

    print(LOGO)
    score = 0
    data_first = choice(DATA)
    DATA.remove(data_first)

    while len(DATA) > 0:
        data_second = choice(DATA)
        DATA.remove(data_second)
        _print_comparison(data_first, data_second)
        comparison = _get_user_comparison()
        followers_first = data_first["follower_count"]
        follower_second = data_second["follower_count"]

        if ((comparison in ("h", "higher") and follower_second >= followers_first) or
                (comparison in ("l", "lower") and follower_second < followers_first)):
            score += 1
            print(f"You're right! Current score: {score}")
            data_first = data_second
            print("Press Enter to continue...")
            input()
        else:
            print(f"Sorry, that's wrong. Final score: {score}. Game over.")
            break


########################################################################################################################
