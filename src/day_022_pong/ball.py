from turtle import Turtle, Screen
from random import randint

from .constants import NORTH, SOUTH


########################################################################################################################

class Ball(Turtle):
    WIDTH = 20
    # number of pixels the ball moves; a step for its movement
    STEP = 10

########################################################################################################################

    def __init__(self):
        """
        Create the pong ball.
        """

        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self._screen = Screen()

########################################################################################################################

    def launch(self) -> None:
        """

        """

        self.goto(0, 0)
        angle = randint(0, 359)
        self.left(angle)

########################################################################################################################

    def move(self) -> None:
        """

        """

        if self.pos()[1] > self._screen.window_height() / 2:
            if self.heading() > NORTH:
                self.setheading(SOUTH - abs(NORTH - self.heading()))
            elif self.heading() < NORTH:
                self.setheading((SOUTH + abs(NORTH - self.heading())) % 360)
            else:
                # exactly vertical, make the angle slightly off so the ball is not stuck on the same trajectory
                self.setheading(randint(SOUTH - 5, SOUTH + 5))
        elif self.pos()[1] < -self._screen.window_height() / 2:
            if self.heading() > SOUTH:
                self.setheading(NORTH - abs(SOUTH - self.heading()))
            elif self.heading() < SOUTH:
                self.setheading((NORTH + abs(SOUTH - self.heading())) % 360)
            else:
                # exactly vertical, make the angle slightly off so the ball is not stuck on the same trajectory
                self.setheading(randint(NORTH - 5, NORTH + 5))

        self.forward(self.STEP)
        self._screen.update()

########################################################################################################################
