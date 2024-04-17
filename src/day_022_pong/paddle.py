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
        self._screen.onkeyrelease(self._reset_movement, "Up")
        self._screen.onkeyrelease(self._reset_movement, "Down")
        self.goto(-self._screen.window_width() / 2 + Paddle.WIDTH, 0)
        # rotate the paddle vertically
        self.setheading(NORTH)
        self._movement_delta = 0

########################################################################################################################

    def _move_up(self) -> None:
        """

        """

        self.setheading(NORTH)
        self._movement_delta = 1

########################################################################################################################

    def _move_down(self) -> None:
        """

        """

        self.setheading(SOUTH)
        self._movement_delta = 1

########################################################################################################################

    def _reset_movement(self) -> None:
        """

        """

        self._movement_delta = 0

########################################################################################################################

    def move(self) -> None:
        """

        """

        # border values for y position of the paddle
        top_y = self._screen.window_height() / 2 - self.HEIGHT / 2
        bottom_y = -self._screen.window_height() / 2 + self.HEIGHT / 2

        if ((bottom_y <= self.pos()[1] <= top_y) or
                (self.pos()[1] < bottom_y and self.heading() == NORTH) or
                (self.pos()[1] > top_y and self.heading() == SOUTH)):
            # allow paddle movement only between top and bottom borders of the window;
            # while paddle is right on the window border, allow movement only out of the border
            self.forward(self.STEP * self._movement_delta)

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
