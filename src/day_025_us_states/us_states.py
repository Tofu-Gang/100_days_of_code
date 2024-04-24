from turtle import Screen, Turtle, shape, mainloop, bye
from os.path import join, dirname, realpath
from pandas import read_csv
from time import sleep


########################################################################################################################

class US_States:
    MAP_FILE_NAME = "blank_states_img.gif"
    STATES_FILE_NAME = "50_states.csv"
    MAP_FILE_PATH = join(dirname(realpath(__file__)), MAP_FILE_NAME)
    STATES_FILE_PATH = join(dirname(realpath(__file__)), STATES_FILE_NAME)
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
        self._screen.onkeypress(bye, "Escape")
        self._screen.listen()

        self._state_name_turtle = Turtle()
        self._state_name_turtle.penup()
        self._state_name_turtle.hideturtle()

        self._info_turtle = Turtle()
        self._clear_info()

        self._states_data = read_csv(self.STATES_FILE_PATH)
        self._score = 0
        mainloop()

########################################################################################################################

    def _clear_info(self) -> None:
        """
        Clear all info text (anything other than state labels) and prepare the text turtle for writing another message.
        """

        self._info_turtle.reset()
        self._info_turtle.penup()
        self._info_turtle.hideturtle()

########################################################################################################################

    def _check_user_state_name(self, *_) -> None:
        """

        :param _:
        """

        if self._score < len(self._states_data):
            state_name = self._screen.textinput(title=f"{self._score}/{len(self._states_data)} States Correct",
                                                prompt="What's another state's name?")
            # do nothing if the user closed the popup window (in which case the state_name IS None)
            if state_name is not None:
                state_name = state_name.title()
                row = self._states_data[self._states_data["state"] == state_name]

                if len(row) == 1:
                    # correct guess
                    self._state_name_turtle.goto(row.x.item(), row.y.item())
                    self._state_name_turtle.write(state_name, font=("Courier", 12, "bold"))
                    self._score += 1

                    if self._score == len(self._states_data):
                        # all states guessed correctly
                        self._info_turtle.color("red")
                        self._info_turtle.goto(0, 0)
                        self._info_turtle.write("YOU WIN!", align="center", font=("Courier", 40, "bold"))
                else:
                    # wrong guess
                    self._info_turtle.color("red")
                    self._info_turtle.goto(0, 0)
                    self._info_turtle.write("WRONG!", align="center", font=("Courier", 40, "bold"))
                    sleep(2)
                    self._clear_info()
        # for some reason pressing the escape key does no longer work after at least one mouse key press in the window
        # and this function call, this ensures the escape key connection with turtle.bye() again
        self._screen.listen()


########################################################################################################################

def run_program() -> None:
    """

    """

    US_States()


########################################################################################################################
