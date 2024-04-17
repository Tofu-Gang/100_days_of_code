from turtle import Screen, Turtle
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

        self._score_left = 0
        self._score_right = 0
        self._score_turtle = Turtle()
        self._update_score()
        self._paint_vertical_line()

        self._paddle_left = LeftPaddle()
        self._paddle_right = RightPaddle()
        self._screen.listen()

        self._ball = Ball(self._paddle_left, self._paddle_right)

########################################################################################################################

    def _paint_vertical_line(self) -> None:
        """

        """

        turtle = Turtle()
        turtle.hideturtle()
        turtle.color("white")
        turtle.pensize(10)
        turtle.penup()
        turtle.goto(0, -self._screen.window_height() / 2)
        turtle.setheading(90)

        while turtle.pos()[1] <= self._screen.window_height() / 2:
            turtle.pendown()
            turtle.goto(0, turtle.pos()[1] + 15)
            turtle.penup()
            turtle.goto(0, turtle.pos()[1] + 20)

########################################################################################################################

    def _update_score(self) -> None:
        """
        Show player score in the window.
        """

        self._score_turtle.reset()
        self._score_turtle.hideturtle()
        self._score_turtle.penup()
        self._score_turtle.color("white")
        self._score_turtle.penup()
        self._score_turtle.goto(-100, self._screen.window_height() / 2 - 100)
        self._score_turtle.write(self._score_left, align="center", font=("Courier", 40, "bold"))
        self._score_turtle.goto(100, self._screen.window_height() / 2 - 100)
        self._score_turtle.write(self._score_right, align="center", font=("Courier", 40, "bold"))

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
                if self._ball.pos()[0] < 0:
                    self._score_right += 1
                else:
                    self._score_left += 1
                self._update_score()
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
