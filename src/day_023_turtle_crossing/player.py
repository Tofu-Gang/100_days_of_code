from turtle import Turtle, Screen


########################################################################################################################

class Player(Turtle):
    NORTH = 90
    WIDTH = 20
    STEP = 5

########################################################################################################################

    def __init__(self):
        """

        """

        super().__init__(shape="turtle")
        self.setheading(self.NORTH)
        self.penup()

        self._screen = Screen()
        self._screen.onkeypress(self._start_movement, "Up")
        self._screen.onkeyrelease(self._stop_movement, "Up")

        self._movement_delta = 0

########################################################################################################################

    def _start_movement(self) -> None:
        """

        """

        self._movement_delta = 1

########################################################################################################################

    def _stop_movement(self) -> None:
        """

        """

        self._movement_delta = 0

########################################################################################################################

    def move(self) -> None:
        """

        """

        self.forward(self.STEP * self._movement_delta)
        self._screen.update()

########################################################################################################################
