from os import getcwd, sep, listdir
from signal import signal, SIGINT
from types import FrameType
from typing import Tuple

########################################################################################################################

EXIT_MESSAGE = "Exiting..."


########################################################################################################################

def _handler_sigint(signum: int, frame: FrameType) -> None:
    """
    :param signum: unused
    :param frame: unused

    A very simple function which is called when Ctrl+C is pressed. It overrides standard behavior, which is sending a
    SIGINT signal followed by throwing a KeyboardInterrupt error. Instead, an information about the situation is printed
    and then the program is terminated with return code 1.
    """

    print("Ctrl+C was pressed!", EXIT_MESSAGE)
    exit(1)


########################################################################################################################

def _get_src_directories() -> Tuple[str, ...]:
    """
    Get a list of all directories in the src/ folder; there is always one directory for each challenge.

    :return: List of directories names in the src/ folder
    """

    cwd = getcwd()
    return tuple(listdir(cwd + sep + "src"))


########################################################################################################################

def _get_implemented_days() -> Tuple[()] | Tuple[int, ...]:
    """
    :return: tuple of numbers of days for which a challenge is already implemented
    """

    return tuple(map(lambda dir_name: int(dir_name[4:7]), _get_src_directories()))


########################################################################################################################

def _is_day_implemented(day: int) -> bool:
    """
    :param day: day/challenge number
    :return: True if this day's challenge is already implemented, False otherwise
    """

    return day in _get_implemented_days()


########################################################################################################################

def _get_day_number() -> str:
    """
    Request a day number from the user. If it isn't valid, tell the user why. Repeat this process until the user inputs
    a valid day number. Finally, prefix the day number with zeroes, so it is exactly three characters long.

    :return: a day number (between 1 and 100, both inclusive) as a string, exactly three characters long
    """

    while True:
        # request numbers until a valid one is input by the user
        day = input("What day's challenge do you want to run?\n")

        # Valid day number must only use numerals [0-9] and nothing else.
        # Furthermore, the day must be between 1 and 100 (both inclusive).
        try:
            assert day.isnumeric()
        except AssertionError:
            print("The day number can only contain numerals [0-9] and no other characters.")
            continue
        try:
            assert 1 <= int(day) <= 100
        except AssertionError:
            print("The day number can only be between 1 and 100 (both inclusive).")
            continue
        try:
            assert _is_day_implemented(int(day))
        except AssertionError:
            if len(_get_implemented_days()) > 0:
                print("This challenge is not yet implemented. Implemented ones are:")
                print(", ".join(map(lambda day_number: str(day_number), _get_implemented_days())))
                continue
            else:
                print("No challenges implemented.", EXIT_MESSAGE)
                exit(0)
        # the day number is definitely valid and the challenge is implemented, break the loop
        break
    # prefix the day number with zeroes, so it is always exactly three characters longs
    return (3 - len(day)) * "0" + day


########################################################################################################################

def _run_program() -> None:
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
    day = "day_" + _get_day_number()
    # get the directory which contains "day_XXX"
    directory = next(filter(lambda dir_name: day in dir_name, directories))
    # the main script of the challenge has to be named same as its directory, minus the "day_XXX_" part; omit the first
    # eight characters from the challenge directory name to get the name of the "main" module file of the challenge.
    filename = directory[8:]
    # dynamically import the "main" challenge module
    module = __import__("src." + directory + "." + filename, fromlist=[""])
    # call the "main" function of the challenge
    module.run_program()


########################################################################################################################

if __name__ == "__main__":
    """
    Show the welcome message, then request a challenge day number and call the challenge "main" function.
    """

    # register the SIGINT signal handler which overrides the default behavior (throwing a KeyboardInterrupt error)
    signal(SIGINT, _handler_sigint)
    print("100 Days of Code")
    print("The Complete Python Pro Bootcamp")
    # get the desired challenge day number from the user, dynamically import the needed module and
    # call the main challenge function
    _run_program()


########################################################################################################################
