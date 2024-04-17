from turtle import Screen
from time import sleep

from .paddle import LeftPaddle, RightPaddle
from .ball import Ball


########################################################################################################################

class Pong:
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768
    # movement speed of the ball and the right paddle
    SPEED = 50

########################################################################################################################

    def __init__(self):
        """
        Set up the screen.
        """

        self._screen = Screen()
        self._screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self._screen.bgcolor("black")
        self._screen.title("PONG")
        self._screen.tracer(0)

        self._paddle_left = LeftPaddle()
        self._paddle_right = RightPaddle()

        self._screen.listen()
        self._ball = Ball()

########################################################################################################################

    def start_game(self) -> None:
        """

        """

        self._ball.launch()

        while True:
            self._paddle_right.move()
            self._ball.move()
            if (self._ball.pos()[0] < -self._screen.window_width() / 2 or
                    self._ball.pos()[0] > self._screen.window_width() / 2):
                self._ball.launch()
            sleep(1 / self.SPEED)

########################################################################################################################

    def end_game(self) -> None:
        """
        End the game.
        """

        self._screen.exitonclick()


########################################################################################################################

def run_program() -> None:
    """
    Play the Pong game.
    """

    game = Pong()
    game.start_game()
    game.end_game()


########################################################################################################################
