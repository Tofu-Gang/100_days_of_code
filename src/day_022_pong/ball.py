from turtle import Turtle, Screen
from random import randint


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
        # set the ball direction randomly
        angle = randint(0, 359)
        self.left(angle)

########################################################################################################################

    def move(self) -> None:
        """

        """

        self.forward(self.STEP)
        self._screen.update()

########################################################################################################################
