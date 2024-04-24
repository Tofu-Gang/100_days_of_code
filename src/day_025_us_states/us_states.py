from turtle import Screen, Turtle, shape, mainloop, bye
from os.path import join, dirname, realpath
from pandas import read_csv


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

        """

        self._screen = Screen()
        self._screen.setup(width=self.MAP_WIDTH, height=self.MAP_HEIGHT)
        self._screen.title("U.S. States Game")
        self._screen.addshape(self.MAP_FILE_PATH)
        shape(self.MAP_FILE_PATH)

        self._screen.onscreenclick(self._check_user_state_name)
        self._screen.onkeypress(bye, "Escape")
        self._screen.listen()

        self._text_turtle = Turtle()
        self._text_turtle.penup()
        self._text_turtle.hideturtle()

        self._states_data = read_csv(self.STATES_FILE_PATH)
        mainloop()

########################################################################################################################

    def _check_user_state_name(self, *_) -> None:
        """

        :param _:
        """

        state_name = self._screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
        row = self._states_data[self._states_data["state"] == state_name]

        if len(row) == 1:
            self._text_turtle.goto(row.x.item(), row.y.item())
            self._text_turtle.write(state_name, font=("Courier", 12, "bold"))


########################################################################################################################

def run_program() -> None:
    """

    """

    US_States()


########################################################################################################################
