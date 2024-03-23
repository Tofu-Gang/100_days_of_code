from types import FrameType

from constants import EXIT_MESSAGE


########################################################################################################################

def handler_sigint(signum: int, frame: FrameType) -> None:
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
