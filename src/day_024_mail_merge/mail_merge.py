from os.path import dirname, realpath, join
from os import mkdir

OUTPUT_DIR = "Output"
READY_TO_SEND_DIR = "ReadyToSend"
INPUT_DIR = "Input"
LETTERS_DIR = "Letters"
NAMES_DIR = "Names"
STARTING_LETTER_FILE = "starting_letter.txt"
NAMES_FILE = "invited_names.txt"
NAMES_PATH = join(dirname(realpath(__file__)), INPUT_DIR, NAMES_DIR, NAMES_FILE)
STARTING_LETTER_PATH = join(dirname(realpath(__file__)), INPUT_DIR, LETTERS_DIR, STARTING_LETTER_FILE)
READY_TO_SEND_PATH = join(dirname(realpath(__file__)), OUTPUT_DIR, READY_TO_SEND_DIR)


########################################################################################################################

def run_program() -> None:
    """
    Read names from a file, then create a personalized letter for each name and save them as txt files.
    """

    with open(NAMES_PATH, "r") as f:
        names = tuple(line.strip() for line in f.readlines())

    with open(STARTING_LETTER_PATH, "r") as f:
        letter = f.read()

    # the output folders are not tracked by git; create them if they do not exist
    try:
        mkdir(join(dirname(realpath(__file__)), OUTPUT_DIR))
    except FileExistsError:
        pass
    try:
        mkdir(READY_TO_SEND_PATH)
    except FileExistsError:
        pass

    for name in names:
        with open(join(READY_TO_SEND_PATH, name + ".txt"), "w") as f:
            f.write(letter.replace("[name]", name))


########################################################################################################################
