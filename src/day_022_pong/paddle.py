from turtle import Turtle, Screen
from random import choice


########################################################################################################################

class Paddle(Turtle):
    # an angle for an UP direction
    NORTH = 90
    # an angle for a DOWN direction
    SOUTH = 270
    WIDTH = 20
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
        self.shapesize(1, 4)
        self._screen = Screen()


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
        self.setheading(self.NORTH)

########################################################################################################################

    def _move_up(self) -> None:
        """

        """

        self.setheading(self.NORTH)
        self.forward(self.STEP)
        self._screen.update()

########################################################################################################################

    def _move_down(self) -> None:
        """

        """

        self.setheading(self.SOUTH)
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
        self.setheading(choice((self.NORTH, self.SOUTH)))

########################################################################################################################

    def move(self) -> None:
        """

        """

        if self.pos()[1] > self._screen.window_height() / 2:
            self.setheading(self.SOUTH)
        elif self.pos()[1] < -self._screen.window_height() / 2:
            self.setheading(self.NORTH)
        self.forward(self.STEP)
        self._screen.update()

########################################################################################################################
