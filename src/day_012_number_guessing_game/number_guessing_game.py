from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
NUMBER_RANGE_FROM = 1
NUMBER_RANGE_TO = 100


########################################################################################################################

def _set_difficulty() -> int:
    """
    Ask the user about the difficulty and return number of possible attempts accordingly.

    :return: 10 attempts for easy difficulty, 5 attempts for hard difficulty
    """

    while True:
        print("Choose a difficulty. Type \"(e)asy\" or \"(h)ard\":")
        difficulty = input("> ").strip().lower()
        if difficulty in ("e", "easy"):
            return EASY_ATTEMPTS
        elif difficulty in ("h", "hard"):
            return HARD_ATTEMPTS
        else:
            print("Invalid value. Try again.")


########################################################################################################################

def _get_guess() -> int:
    """
    :return: guess collected from the user
    """

    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Invalid value. Integer required.")


########################################################################################################################

def run_program() -> None:
    """
    Play the number guessing game.
    """

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {NUMBER_RANGE_FROM} and {NUMBER_RANGE_TO}.")
    number = randint(NUMBER_RANGE_FROM, NUMBER_RANGE_TO)
    attempts = _set_difficulty()

    while True:
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = _get_guess()

            if guess > number:
                print("Too high.")
            elif guess < number:
                print("Too low.")
            else:
                print(f"You got it! The answer was {number}.")
                break

            attempts -= 1
            print("Guess again.")
        else:
            print(f"You've run out of guesses, you lose. The answer was {number}.")
            break

########################################################################################################################
