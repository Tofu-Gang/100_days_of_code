from turtle import Screen, Turtle


########################################################################################################################

class Paddle(Turtle):
    WIDTH = 20

    def __init__(self):
        """
        Create a pong paddle.
        """

        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(4, 1)


########################################################################################################################

class Pong:
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768

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

        self._paddle_left = Paddle()
        self._paddle_left.goto(-self.SCREEN_WIDTH / 2 + Paddle.WIDTH, 0)
        self._paddle_right = Paddle()
        # try to place the right paddle in the same distance from its edge as is the left one, the screen geometry works
        # weird, that's why there is the 1.4 coefficient
        self._paddle_right.goto(self.SCREEN_WIDTH / 2 - Paddle.WIDTH * 1.4, 0)

        self._screen.update()

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
    game.end_game()


########################################################################################################################
