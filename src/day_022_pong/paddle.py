from turtle import Turtle

from .constants import NORTH


########################################################################################################################

class Paddle(Turtle):
    WIDTH = 20

########################################################################################################################

    def __init__(self):
        """
        Create a pong paddle.
        """

        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(1, 4)
        # rotate the paddle vertically
        self.setheading(NORTH)


########################################################################################################################
