########################################################################################################################

def _get_user_input(message: str) -> str:
    """
    :param message: a message that is printed before getting user input
    :return: user input that needs no validations, prompted with the message from the only param of this function
    """

    return input(message)


########################################################################################################################

def generate_band_name(city_name: str, pet_name: str) -> str:
    """
    :param city_name: user's city name
    :param pet_name: user's pet's name

    Connect the two strings from params together to make a possible band name. Having params instead of just calling
    the input() function directly here and returning the possible band name instead of printing it for unit testing
    purposes (avoiding mocking).

    :return: a possible band name created by connecting the two param strings together
    """

    return "{} {}".format(city_name, pet_name)


########################################################################################################################

def run_program() -> None:
    """
    Collect both demanded user inputs and generate a possible band name from those inputs.
    """

    print("Welcome to the Band Name Generator.")
    city_name = _get_user_input("What's the name of the city you grew up in?\n> ")
    pet_name = _get_user_input("What's your pet's name?\n> ")
    print("Your band name could be", generate_band_name(city_name, pet_name) + ".")


########################################################################################################################
