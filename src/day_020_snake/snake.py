from turtle import Turtle, Screen
from time import sleep


########################################################################################################################

class Snake:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    TURTLE_SQUARE_SIDE = 21
    SNAKE_SPEED = 10

########################################################################################################################

    def __init__(self):
        """

        """

        self._screen = Screen()
        self._screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self._screen.bgcolor("black")
        self._screen.title("SNAKE")
        self._screen.tracer(0)
        self._snake = []
        self._expand_snake()
        self._expand_snake()
        self._expand_snake()
        self._screen.update()

########################################################################################################################

    def _expand_snake(self) -> None:
        """

        """

        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(0 - len(self._snake) * self.TURTLE_SQUARE_SIDE, 0)
        self._snake.append(segment)

########################################################################################################################

    def _move_snake(self) -> None:
        """

        """

        [self._snake[i].goto(self._snake[i - 1].pos()) for i in reversed(range(1, len(self._snake)))]
        # TODO: update snake direction here
        self._snake[0].forward(self.TURTLE_SQUARE_SIDE)
        self._screen.update()
        sleep(1 / self.SNAKE_SPEED)

########################################################################################################################

    def start_game(self) -> None:
        """

        """

        for _ in range(10):
            self._move_snake()

########################################################################################################################

    def end_game(self) -> None:
        """

        """

        self._screen.exitonclick()


########################################################################################################################

def run_program() -> None:
    """

    """

    game = Snake()
    game.start_game()
    game.end_game()


########################################################################################################################
