
from signal import signal, SIGINT

from signal_handlers import handler_sigint
from utils import run_program


########################################################################################################################

if __name__ == "__main__":
    """
    Show the welcome message, then request a challenge day number and call the challenge "main" function.
    """

    # register the SIGINT signal handler which overrides the default behavior (throwing a KeyboardInterrupt error)
    signal(SIGINT, handler_sigint)
    print("100 Days of Code")
    print("The Complete Python Pro Bootcamp")
    # get the desired challenge day number from the user, dynamically import the needed module and
    # call the main challenge function
    run_program()


########################################################################################################################
