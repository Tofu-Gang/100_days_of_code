from turtle import Turtle, Screen
from random import choice

from .constants import NORTH, SOUTH


########################################################################################################################

class Paddle(Turtle):
    HEIGHT_FACTOR = 4
    WIDTH = 20
    HEIGHT = WIDTH * HEIGHT_FACTOR
    # number of pixels the paddles move; a step for their movement
    STEP = 10

########################################################################################################################

    def __init__(self):
        """
        Create a pong paddle.
        """

        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(1, self.HEIGHT_FACTOR)
        self._screen = Screen()

########################################################################################################################

    @property
    def top_y(self) -> int:
        """

        :return:
        """

        return self.pos()[1] + self.HEIGHT / 2

########################################################################################################################

    @property
    def bottom_y(self) -> int:
        """

        :return:
        """

        return self.pos()[1] - self.HEIGHT / 2


########################################################################################################################

class LeftPaddle(Paddle):

    def __init__(self):
        """

        """

        super().__init__()
        self._screen.onkeypress(self._move_up, "Up")
        self._screen.onkeypress(self._move_down, "Down")
        self.goto(-self._screen.window_width() / 2 + Paddle.WIDTH, 0)
        # rotate the paddle vertically
        self.setheading(NORTH)

########################################################################################################################

    def _move_up(self) -> None:
        """

        """

        self.setheading(NORTH)
        self.forward(self.STEP)
        self._screen.update()

########################################################################################################################

    def _move_down(self) -> None:
        """

        """

        self.setheading(SOUTH)
        self.forward(self.STEP)
        self._screen.update()

########################################################################################################################


class RightPaddle(Paddle):

    def __init__(self):
        """

        """

        super().__init__()
        # try to place the right paddle in the same distance from its edge as is the left one, the screen geometry works
        # weird, that's why there is the 1.4 coefficient
        self.goto(self._screen.window_width() / 2 - Paddle.WIDTH * 1.4, 0)
        self.setheading(choice((NORTH, SOUTH)))

########################################################################################################################

    def move(self) -> None:
        """

        """

        if self.pos()[1] > self._screen.window_height() / 2:
            self.setheading(SOUTH)
        elif self.pos()[1] < -self._screen.window_height() / 2:
            self.setheading(NORTH)
        self.forward(self.STEP)
        self._screen.update()

########################################################################################################################
