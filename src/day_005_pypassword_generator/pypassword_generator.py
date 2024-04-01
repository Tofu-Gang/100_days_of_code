from random import choice, shuffle

from constants import LETTERS, NUMBERS, SYMBOLS


########################################################################################################################

def _generate_password(letters_count: int, numbers_count: int, symbols_count: int) -> str:
    """
    :param letters_count: how many letters in the password
    :param numbers_count: how many numbers in the password
    :param symbols_count: how many symbols in the password
    :return: a random password with specified amounts of letters, numbers and symbols
    """

    letters = list(choice(LETTERS) for _ in range(letters_count))
    numbers = list(choice(NUMBERS) for _ in range(numbers_count))
    symbols = list(choice(SYMBOLS) for _ in range(symbols_count))

    password = letters + numbers + symbols
    shuffle(password)
    return "".join(password)


########################################################################################################################

def run_program() -> None:
    """
    Generate a random password. Ask the user how many letters, numbers and symbols should be in it.
    """

    print("Welcome to the PyPassword Generator!")

    while True:
        print("How many letters would you like in your password?")
        try:
            letters_count = int(input("> "))
            break
        except ValueError:
            print("Invalid value. Integer required.")

    while True:
        print("How many numbers would you like?")
        try:
            numbers_count = int(input("> "))
            break
        except ValueError:
            print("Invalid value. Integer required.")

    while True:
        print("How many symbols would you like?")
        try:
            symbols_count = int(input("> "))
            break
        except ValueError:
            print("Invalid value. Integer required.")

    password = _generate_password(letters_count, numbers_count, symbols_count)
    print("Here is your password: " + password)

########################################################################################################################
