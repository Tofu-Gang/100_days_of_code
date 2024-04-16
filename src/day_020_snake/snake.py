from turtle import Turtle, Screen
from time import sleep


########################################################################################################################

class Snake:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    TURTLE_SQUARE_SIDE = 21
    SNAKE_SPEED = 10
    EAST = 0
    NORTH = 90
    WEST = 180
    SOUTH = 270
    STARTING_SNAKE_LENGTH = 3

########################################################################################################################

    def __init__(self):
        """
        Create the game window and set it up; create the snake and set up controls of the snake.
        """

        self._screen = Screen()
        self._screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self._screen.bgcolor("black")
        self._screen.title("SNAKE")
        self._screen.tracer(0)

        self._snake = []
        [self._expand_snake() for _ in range(self.STARTING_SNAKE_LENGTH)]
        self._screen.update()

        self._screen.onkeypress(
            lambda: self._snake[0].setheading(self.NORTH
                                              if self._goes_horizontally()
                                              else self._snake[0].heading()), "Up")
        self._screen.onkeypress(
            lambda: self._snake[0].setheading(self.SOUTH
                                              if self._goes_horizontally()
                                              else self._snake[0].heading()), "Down")
        self._screen.onkeypress(
            lambda: self._snake[0].setheading(self.WEST
                                              if self._goes_vertically()
                                              else self._snake[0].heading()), "Left")
        self._screen.onkeypress(
            lambda: self._snake[0].setheading(self.EAST
                                              if self._goes_vertically()
                                              else self._snake[0].heading()), "Right")
        self._screen.listen()

########################################################################################################################

    def _expand_snake(self) -> None:
        """
        Add another segment of the snake at its end (or in the screen center if there are no segments yet).
        """

        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()

        if len(self._snake) > 0:
            # position of the snake's tail
            new_segment_pos = self._snake[-1].pos()
            # move the snake
            self._move_snake()
            # move the new segment where the snake's tail used to be
            segment.goto(new_segment_pos)
        else:
            # no segments yet, just place the first segment in the center of the screen
            segment.goto((0, 0))

        self._snake.append(segment)

########################################################################################################################

    def _goes_horizontally(self) -> bool:
        """
        :return: True if the snake is heading right or left, False otherwise
        """

        return int(self._snake[0].heading()) in (self.EAST, self.WEST)

########################################################################################################################

    def _goes_vertically(self) -> bool:
        """
        :return: True if the snake is heading up or down, False otherwise
        """

        return int(self._snake[0].heading()) in (self.NORTH, self.SOUTH)

########################################################################################################################

    def _move_snake(self) -> None:
        """
        Move snake by one length unit.
        """

        [self._snake[i].goto(self._snake[i - 1].pos()) for i in reversed(range(1, len(self._snake)))]
        self._snake[0].forward(self.TURTLE_SQUARE_SIDE)
        self._screen.update()
        sleep(1 / self.SNAKE_SPEED)

########################################################################################################################

    def start_game(self) -> None:
        """

        """

        for _ in range(100):
            self._move_snake()

########################################################################################################################

    def end_game(self) -> None:
        """

        """

        self._screen.exitonclick()


########################################################################################################################

def run_program() -> None:
    """
    Play the snake game.
    """

    game = Snake()
    game.start_game()
    game.end_game()


########################################################################################################################
