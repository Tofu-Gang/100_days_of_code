from turtle import Screen, Turtle
from random import randint
from time import sleep


########################################################################################################################

class Ball(Turtle):
    WIDTH = 20
    SPEED = 50
    STEP = 5

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
            self.forward(self.STEP)
            self._screen.update()
            sleep(1 / self.SPEED)


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

        self._ball = Ball(self._screen)
        self._ball.start_moving()

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
