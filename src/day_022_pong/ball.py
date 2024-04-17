from turtle import Turtle
from random import randint
from time import sleep

from .constants import STEP


########################################################################################################################

class Ball(Turtle):
    WIDTH = 20
    SPEED = 50

########################################################################################################################

    def __init__(self, screen):
        """
        Create the pong ball.
        """

        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self._is_moving = False

        self._screen = screen

########################################################################################################################

    def start_moving(self) -> None:
        """
        Choose a random direction and move the ball in that direction.
        """

        self._is_moving = True
        angle = randint(0, 359)
        self.left(angle)

        while self._is_moving:
            self.forward(STEP)
            self._screen.update()
            sleep(1 / self.SPEED)


########################################################################################################################
