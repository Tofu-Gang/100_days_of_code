from turtle import Turtle, Screen
from random import randint

from .constants import NORTH, SOUTH, WEST, EAST
from .paddle import Paddle


########################################################################################################################

class Ball(Turtle):
    WIDTH = 20
    # number of pixels the ball moves; a step for its movement
    STEP = 10

########################################################################################################################

    def __init__(self, paddle_left: Paddle, paddle_right: Paddle):
        """
        Create the pong ball.
        """

        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self._screen = Screen()
        self._paddle_left = paddle_left
        self._paddle_right = paddle_right

########################################################################################################################

    def launch(self) -> None:
        """

        """

        self.goto(0, 0)
        angle = randint(135, 225)
        self.left(angle)

########################################################################################################################

    def move(self) -> None:
        """

        """

        # bounce from top and bottom walls
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
        # bounce from paddles
        elif self.pos()[0] < self._paddle_left.pos()[0] + self.WIDTH and self._paddle_left.bottom_y <= self.pos()[1] <= self._paddle_left.top_y:
            if self.heading() > WEST:
                self.setheading(360 - abs(WEST - self.heading()))
            elif self.heading() < WEST:
                self.setheading(abs(WEST - self.heading()))
            else:
                # exactly horizontal, make the angle slightly off so the ball is not stuck on the same trajectory
                self.setheading(randint(355, 365) % 360)
        elif self.pos()[0] > self._paddle_right.pos()[0] - self.WIDTH and self._paddle_right.bottom_y <= self.pos()[1] <= self._paddle_right.top_y:
            if self.heading() > EAST:
                self.setheading(WEST - self.heading())
            elif self.heading() < 360:
                self.setheading(WEST + (360 - self.heading()))
            else:
                # exactly horizontal, make the angle slightly off so the ball is not stuck on the same trajectory
                self.setheading(randint(WEST - 5, WEST + 5))

        self.forward(self.STEP)
        self._screen.update()

########################################################################################################################
