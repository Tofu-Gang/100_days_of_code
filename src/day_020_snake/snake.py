from turtle import Turtle, Screen
from time import sleep
from random import randint


########################################################################################################################

class Snake:
    TURTLE_SQUARE_SIDE = 20
    GRID_WIDTH = 30
    GRID_HEIGHT = 30
    SCREEN_WIDTH = TURTLE_SQUARE_SIDE * GRID_WIDTH
    SCREEN_HEIGHT = TURTLE_SQUARE_SIDE * GRID_HEIGHT
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

        self._food = Turtle("circle")
        self._food.color("blue")
        self._food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self._food.speed("fastest")
        self._food.penup()

        self._score = 0
        self._info_turtle = Turtle()

########################################################################################################################

    def _spawn_food(self) -> None:
        """

        """

        while True:
            x = randint(int(-self.GRID_WIDTH / 2) + 1, int(self.GRID_WIDTH / 2) - 1) * self.TURTLE_SQUARE_SIDE
            y = randint(int(-self.GRID_HEIGHT / 2) + 1, int(self.GRID_HEIGHT / 2) - 1) * self.TURTLE_SQUARE_SIDE

            if (x, y) not in [segment.pos() for segment in self._snake]:
                self._food.goto((x, y))
                break

########################################################################################################################

    def _update_score(self) -> None:
        """

        """

        self._info_turtle.reset()
        self._info_turtle.hideturtle()
        self._info_turtle.penup()
        self._info_turtle.color("white")
        self._info_turtle.goto(0, self.SCREEN_HEIGHT / 2 - self.TURTLE_SQUARE_SIDE * 2)
        self._info_turtle.write(f"Score: {self._score}", align="center", font=("Courier", 24, "normal"))

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
        self._snake[0].color("red")

########################################################################################################################

    def _is_crashed(self) -> bool:
        """

        :return:
        """

        head_pos_x = self._snake[0].pos()[0]
        head_pos_y = self._snake[0].pos()[1]

        return (head_pos_x <= -self.SCREEN_WIDTH / 2 or
                head_pos_x >= self.SCREEN_WIDTH / 2 or
                head_pos_y <= -self.SCREEN_HEIGHT / 2 or
                head_pos_y >= self.SCREEN_HEIGHT / 2)# or
                # head_pos_x in (segment.pos()[0] for segment in self._snake[1:]) or
                # head_pos_y in (segment.pos()[1] for segment in self._snake[1:]))

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

        self._spawn_food()
        self._update_score()

        while not self._is_crashed():
            self._move_snake()
            distance = int(self._snake[0].distance(self._food.pos()))

            if distance == 0:
                self._score += 1
                self._update_score()
                self._expand_snake()
                self._spawn_food()

########################################################################################################################

    def end_game(self) -> None:
        """

        """

        self._info_turtle.goto(0, 0)
        self._info_turtle.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
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
