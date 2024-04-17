from turtle import Turtle, Screen
from random import randint
from time import sleep

from .constants import STEP, SPEED


########################################################################################################################

class Ball(Turtle):
    WIDTH = 20

########################################################################################################################

    def __init__(self, screen: Screen):
        """
        Create the pong ball.
        """

        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self._screen = screen
        # set the ball direction randomly
        angle = randint(0, 359)
        self.left(angle)

########################################################################################################################
