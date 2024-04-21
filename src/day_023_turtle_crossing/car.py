from turtle import Turtle, Screen

from utils import random_color


########################################################################################################################

class Car(Turtle):
    WIDTH = 20
    LENGTH_FACTOR = 2
    LENGTH = WIDTH * LENGTH_FACTOR
    WEST = 180

########################################################################################################################

    def __init__(self, x: int, y: int, step: int):
        """
        Create a car. Set a random color, modify the shape, so it is a 2:1 rectangle.
        :param x: horizontal position
        :param y: vertical position
        :param step: how many pixels the cars moves forward in one step
        """

        super().__init__(shape="square")
        self.setheading(self.WEST)
        self.color(random_color())
        self.shapesize(1, self.LENGTH_FACTOR)
        self.penup()
        self.goto(x, y)
        self._screen = Screen()
        self._step = step

########################################################################################################################

    def move(self) -> None:
        """
        Move the car forward. Hide it if it went all the way through the game window and reached the left window border.
        It will be removed then.
        """

        if self.pos()[0] < -self._screen.window_width() / 2 - self.LENGTH / 2:
            self.hideturtle()
        else:
            self.forward(self._step)
        self._screen.update()

########################################################################################################################
