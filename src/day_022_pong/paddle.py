from turtle import Turtle


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
        self.shapesize(4, 1)


########################################################################################################################
