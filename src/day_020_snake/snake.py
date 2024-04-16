from turtle import Turtle, Screen


########################################################################################################################

class Snake:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    TURTLE_SQUARE_SIDE = 21

########################################################################################################################

    def __init__(self):
        """

        """

        self._screen = Screen()
        self._screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self._screen.bgcolor("black")
        self._screen.title("SNAKE")
        self._snake = []
        self._expand_snake()
        self._expand_snake()
        self._expand_snake()
        self._screen.exitonclick()

########################################################################################################################

    def _expand_snake(self) -> None:
        """

        """

        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(0 - len(self._snake) * self.TURTLE_SQUARE_SIDE, 0)
        self._snake.append(turtle)


########################################################################################################################

def run_program() -> None:
    """

    """

    Snake()

########################################################################################################################
