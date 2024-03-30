from os import sep, listdir
from os.path import dirname, realpath
from typing import Tuple, Union
from math import floor

from constants import EXIT_MESSAGE, SRC_DIR_NAME


########################################################################################################################

def round_up(number: float, decimals: int = 0) -> float:
    """
    :param number: a float number to round up
    :param decimals: to how many spaces round up
    :return: the number rounded up to a specified number of digits
    """

    multiplier = 10 ** decimals
    return floor(number * multiplier + 0.5) / multiplier


########################################################################################################################

def extract_day_number_from_dir_name(dir_name: str) -> int:
    """
    :param dir_name: name of a directory in the src folder
    :return: extracted slice from the directory name between 4 and 6 (both inclusive), converted to int
    """

    day_number = dir_name[4:7]
    return int(day_number)


########################################################################################################################

def prefix_day_number_with_zeroes(day_number: str) -> str:
    """
    :param day_number: a string of a day number (no validations are in place)
    :return: string of the input day_number prefixed with zeroes so the result has length of 3 or more
    """

    return (3 - len(day_number)) * "0" + day_number


########################################################################################################################

def _get_src_directories() -> Tuple[str, ...]:
    """
    Get a list of all directories in the src/ folder; there is always one directory for each challenge.

    :return: list of directories names in the src/ folder
    """

    return tuple(listdir(dirname(realpath(__file__)) + sep + SRC_DIR_NAME))


########################################################################################################################

def _get_implemented_days() -> Union[Tuple[()], Tuple[int, ...]]:
    """
    :return: tuple of numbers of days for which a challenge is already implemented
    """

    return tuple(map(extract_day_number_from_dir_name, _get_src_directories()))


########################################################################################################################

def _get_day_number() -> str:
    """
    Request a day number from the user. If it isn't valid, tell the user why. Repeat this process until the user inputs
    a valid day number. Finally, prefix the day number with zeroes, so it is exactly three characters long.

    :return: a day number (between 1 and 100, both inclusive) as a string, exactly three characters long
    """

    while True:
        # request numbers until a valid one is input by the user
        day = input("What day's challenge do you want to run?\n> ")

        # Valid day number must only use numerals [0-9] and nothing else.
        # Furthermore, the day must be between 1 and 100 (both inclusive).
        try:
            assert day.isnumeric()
        except AssertionError:
            # there are some non-numeric characters in the day number string; there must be none
            print("The day number can only contain numerals [0-9] and no other characters.")
            continue
        try:
            assert 1 <= int(day) <= 100
        except AssertionError:
            # the day number is not between 1 and 100 (both inclusive)
            print("The day number can only be between 1 and 100 (both inclusive).")
            continue
        try:
            assert int(day) in _get_implemented_days()
        except AssertionError:
            if len(_get_implemented_days()) > 0:
                # there are some challenge(s) implemented, but this one is not
                print("This challenge is not yet implemented. Implemented ones are:")
                print(", ".join(map(lambda day_number: str(day_number), _get_implemented_days())))
                continue
            else:
                # there are no challenges implemented yet
                print("No challenges implemented.", EXIT_MESSAGE)
                exit(0)
        # the day number is definitely valid and the challenge is implemented, break the loop
        break
    # prefix the day number with zeroes, so it is always exactly three characters longs
    return prefix_day_number_with_zeroes(day)


########################################################################################################################

def run_program() -> None:
    """
    Get a day number from the user and use it in dynamic import of that day's challenge function "run_program()", which
    is also called at the end of this function.
    This name always has to be used for the challenge entry point function in the "main" Python script of the challenge.
    Furthermore, the directory name for each challenge has to be placed in the src/ folder and follow the format
    day_XXX_NAME_OF_THE_CHALLENGE. Finally, the same NAME_OF_THE_CHALLENGE has to be chosen for the "main" Python script
    of the day's challenge.
    """

    # get a list of all directories names in the src/ folder
    directories = _get_src_directories()
    # get a day number from the user and prefix this string with "day_", so we have the first part of the requested
    # challenge directory name "day_XXX", where XXX is the day number chosen by the user
    day = _get_day_number()
    # get the directory which contains "day_XXX"
    directory = next(filter(lambda dir_name: "day_" + day in dir_name, directories))
    # the main script of the challenge has to be named same as its directory, minus the "day_XXX_" part; omit the first
    # eight characters from the challenge directory name to get the name of the "main" module file of the challenge.
    filename = directory[8:]
    # dynamically import the "main" challenge module
    module = __import__(SRC_DIR_NAME + "." + directory + "." + filename, fromlist=[""])
    # call the "main" function of the challenge
    module.run_program()


########################################################################################################################
