from string import printable
from random import choice, shuffle


########################################################################################################################

def run_program() -> None:
    """

    """

    print("Welcome to the PyPassword Generator!")
    print("How many letters would you like in your password?")
    letters_count = int(input("> "))
    print("How many symbols would you like?")
    symbols_count = int(input("> "))
    print("How many numbers would you like?")
    numbers_count = int(input("> "))

    letters = list(choice(printable[10:62]) for _ in range(letters_count))
    numbers = list(choice(printable[0:10]) for _ in range(numbers_count))
    symbols = list(choice(printable[62:94]) for _ in range(symbols_count))

    password = letters + numbers + symbols
    shuffle(password)
    print("Here is your password: " + "".join(password))

########################################################################################################################
