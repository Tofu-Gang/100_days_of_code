########################################################################################################################

def run_program() -> None:
    """
    Get the user's city name and their pet's name. Connect those two together to make a possible band name.
    """

    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    print("Your band name could be {} {}".format(city, pet_name))


########################################################################################################################
