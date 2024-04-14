from turtle import Turtle, Screen


########################################################################################################################

class TurtleRace:
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 400

########################################################################################################################

    def __init__(self):
        """

        """

        self._timmy = Turtle()
        self._screen = Screen()
        self._screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self._user_bet = self._screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
        print(self._user_bet)
        self._screen.exitonclick()

########################################################################################################################


def run_program() -> None:
    """

    """

    TurtleRace()


########################################################################################################################
