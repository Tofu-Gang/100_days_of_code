from turtle import Screen, Turtle, shape, mainloop, bye
from os.path import join, dirname, realpath
from typing import Union
from pandas import read_csv, DataFrame
from time import sleep


########################################################################################################################

class US_States:
    MAP_FILE_NAME = "blank_states_img.gif"
    STATES_FILE_NAME = "50_states.csv"
    MISSING_STATES_FILE_NAME = "states_to_learn.csv"
    MAP_FILE_PATH = join(dirname(realpath(__file__)), MAP_FILE_NAME)
    STATES_FILE_PATH = join(dirname(realpath(__file__)), STATES_FILE_NAME)
    MISSING_STATES_FILE_PATH = join(dirname(realpath(__file__)), MISSING_STATES_FILE_NAME)
    MAP_WIDTH = 725
    MAP_HEIGHT = 491

########################################################################################################################
    def __init__(self):
        """
        Set up the window with an image of a map of the USA. Create turtles for writing text in the window. Establish
        connection between mouse key press and escape key and their respective functions (guess a state name dialog and
        closing the window). Keep track of the player score (how many states are guessed correctly so far). Load the
        states data from a csv file (state labels and their position in the map).
        """

        self._screen = Screen()
        self._screen.setup(width=self.MAP_WIDTH, height=self.MAP_HEIGHT)
        self._screen.title("U.S. States Game")
        self._screen.addshape(self.MAP_FILE_PATH)
        shape(self.MAP_FILE_PATH)

        self._screen.onscreenclick(self._check_user_state_name)
        self._screen.onkeypress(self._exit, "Escape")
        self._screen.listen()

        self._state_name_turtle = Turtle()
        self._state_name_turtle.penup()
        self._state_name_turtle.hideturtle()

        self._info_turtle = Turtle()
        self._clear_info()

        self._states_data = read_csv(self.STATES_FILE_PATH)
        self._correct_guesses = []
        mainloop()

########################################################################################################################

    @property
    def _score(self) -> int:
        """
        :return: player score (number of correct guesses so far)
        """

        return len(self._correct_guesses)

########################################################################################################################

    @property
    def _is_win(self) -> bool:
        """
        :return: True if the game is win, False otherwise
        """

        return self._score == len(self._states_data)

########################################################################################################################

    def _clear_info(self) -> None:
        """
        Clear all info text (anything other than state labels) and prepare the text turtle for writing another message.
        """

        self._info_turtle.reset()
        self._info_turtle.penup()
        self._info_turtle.hideturtle()

########################################################################################################################

    def _draw_wrong_guess(self) -> None:
        """
        Inform the user about their wrong guess.
        """

        self._info_turtle.color("red")
        self._info_turtle.goto(0, 0)
        self._info_turtle.write("WRONG!", align="center", font=("Courier", 40, "bold"))
        sleep(2)
        self._clear_info()

########################################################################################################################

    def _draw_win(self) -> None:
        """
        Inform the user about winning the game.
        """

        self._info_turtle.color("red")
        self._info_turtle.goto(0, 0)
        self._info_turtle.write("YOU WIN!", align="center", font=("Courier", 40, "bold"))

########################################################################################################################

    def _write_state_name(self, x: int, y: int, state_name: str) -> None:
        """
        Write a state name in the map.

        :param x: horizontal position of the label
        :param y: vertical position of the label
        :param state_name: state name
        """

        self._state_name_turtle.goto(x, y)
        self._state_name_turtle.write(state_name, font=("Courier", 8, "bold"))

########################################################################################################################

    def _get_user_guess(self) -> Union[str, None]:
        """
        Show a popup window, let the user guess a US state name.

        :return: user guess in Title case or None if the user closed the window manually
        """

        try:
            return self._screen.textinput(title=f"{self._score}/{len(self._states_data)} States Correct",
                                          prompt="What's another state's name?").title()
        except AttributeError:
            return None

########################################################################################################################

    def _check_user_state_name(self, *_) -> None:
        """
        Show popup window where the user can guess a US state name. Correct guess results in revealing the state label
        in the map; wrong guess causes an information which disappears after some time. If all the states are revealed,
        inform the user and do nothing further.

        :param _: since this is connected to Screen.onscreenclick(), there are unused params with x and y mouse
        positions where the mouse press event occurred
        """

        if not self._is_win:
            state_name = self._get_user_guess()
            # do nothing if the user closed the popup window (in which case the state_name IS None)
            if state_name is not None:
                state_name = state_name.title()
                row = self._states_data[self._states_data["state"] == state_name]

                if len(row) == 1 and state_name not in self._correct_guesses:
                    # correct guess
                    self._write_state_name(row.x.item(), row.y.item(), state_name)
                    self._correct_guesses.append(state_name)

                    if self._is_win:
                        # all states guessed correctly
                        self._draw_win()
                else:
                    # wrong guess
                    self._draw_wrong_guess()
        # for some reason pressing the escape key does no longer work after at least one mouse key press in the window
        # and this function call, this ensures the escape key connection with turtle.bye() again
        self._screen.listen()

########################################################################################################################

    def _exit(self) -> None:
        """
        Exit the game. Save a csv file with all the US states that weren't guessed.
        """

        if not self._is_win:
            DataFrame({
                "Missing States": tuple(filter(lambda state_name: state_name not in self._correct_guesses,
                                               self._states_data["state"].to_list()))
            }).to_csv(self.MISSING_STATES_FILE_PATH)
        bye()


########################################################################################################################

def run_program() -> None:
    """
    Play the US states guessing game.
    """

    US_States()


########################################################################################################################
