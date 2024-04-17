from turtle import Turtle, Screen
from random import choice

from .constants import NORTH, SOUTH


########################################################################################################################

class Paddle(Turtle):
    # how many times is the height greater than the width
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
        :return: top y coordinate of the paddle
        """

        return self.pos()[1] + self.HEIGHT / 2

########################################################################################################################

    @property
    def bottom_y(self) -> int:
        """
        :return: bottom y coordinate of the paddle
        """

        return self.pos()[1] - self.HEIGHT / 2


########################################################################################################################

class LeftPaddle(Paddle):

    def __init__(self):
        """
        Create left paddle. Map up and down arrow keys to moving the paddle.
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
        Move the paddle up.
        """

        self.setheading(NORTH)
        self._movement_delta = 1

########################################################################################################################

    def _move_down(self) -> None:
        """
        Move the paddle down.
        """

        self.setheading(SOUTH)
        self._movement_delta = 1

########################################################################################################################

    def _reset_movement(self) -> None:
        """
        Stop moving the paddle.
        """

        self._movement_delta = 0

########################################################################################################################

    def move(self) -> None:
        """
        To remove the key repeat delay, the logic of moving the paddle had to change. Call this function repeatedly; a
        product of the step and movement delta is used as an argument in moving the paddle. The delta value is 1 while
        key up/down is pressed, and zero otherwise. This means that the product is zero while no key is pressed and the
        paddle does not move.
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
        Create the right paddle. It just moves up and down.
        """

        super().__init__()
        # try to place the right paddle in the same distance from its edge as is the left one, the screen geometry works
        # weird, that's why there is the 1.4 coefficient
        self.goto(self._screen.window_width() / 2 - Paddle.WIDTH * 1.4, 0)
        self.setheading(choice((NORTH, SOUTH)))

########################################################################################################################

    def move(self) -> None:
        """
        Call this function repeatedly; it moves the paddle continuously up and down.
        """

        if self.pos()[1] > self._screen.window_height() / 2:
            self.setheading(SOUTH)
        elif self.pos()[1] < -self._screen.window_height() / 2:
            self.setheading(NORTH)
        self.forward(self.STEP)
        self._screen.update()

########################################################################################################################
