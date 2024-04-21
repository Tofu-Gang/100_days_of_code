from turtle import Screen, Turtle, colormode
from time import sleep
from random import randint

from .player import Player
from .car import Car


########################################################################################################################

class TurtleCrossing:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    FINISH_HEIGHT = 40
    LEVEL_PADDING_LEFT = 20
    LEVEL_PADDING_TOP = 40
    SPEED = 50
    CAR_STEP_FROM = 2
    CAR_STEP_TO = 5

########################################################################################################################

    def __init__(self):
        """
        Create the game:
        -set up the screen
        -create the player turtle
        -draw the finish area
        -create level counter
        -create ongoing game flag (escape keypress switches it to False, breaks the main game loop, ending the game)
        """

        self._screen = Screen()
        self._screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self._screen.title("TURTLE CROSSING")
        self._screen.onkeypress(self._end_game, "Escape")
        self._screen.tracer(0)
        self._screen.listen()
        colormode(255)

        self._player = Player()
        self._cars = []
        self._game_going = None
        self._level = None
        self._level_turtle = Turtle()
        self._draw_finish()

########################################################################################################################

    def _draw_finish(self) -> None:
        """
        Draw the finish area.
        """

        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.fillcolor("green")
        turtle.goto(-self.SCREEN_WIDTH / 2, 300)
        turtle.begin_fill()
        turtle.forward(self.SCREEN_WIDTH)
        turtle.right(90)
        turtle.forward(self.FINISH_HEIGHT)
        turtle.right(90)
        turtle.forward(self.SCREEN_WIDTH)
        turtle.right(90)
        turtle.forward(self.FINISH_HEIGHT)
        turtle.end_fill()

########################################################################################################################

    def _draw_info(self) -> None:
        """
        Draw the level number.
        """

        self._level_turtle.reset()
        self._level_turtle.hideturtle()
        self._level_turtle.penup()
        self._level_turtle.goto(-self.SCREEN_WIDTH / 2 + self.LEVEL_PADDING_LEFT,
                                self.SCREEN_HEIGHT / 2 - self.LEVEL_PADDING_TOP)
        self._level_turtle.write(f"Level: {self._level}", font=("Courier", 20, "bold"))

########################################################################################################################

    def _is_player_behind_finish_line(self) -> bool:
        """
        :return: True if the player is behind the level finish line, False otherwise
        """

        return self._player.pos()[1] >= self.SCREEN_HEIGHT / 2 - self.FINISH_HEIGHT - Player.WIDTH / 2

########################################################################################################################

    def _add_car(self) -> None:
        """
        Create a car at a random vertical position and a random speed.
        """

        x = int(self.SCREEN_WIDTH / 2) + Car.LENGTH / 2
        y = randint(int(-self.SCREEN_HEIGHT / 2 + Car.WIDTH),
                    int(self.SCREEN_HEIGHT / 2 - self.FINISH_HEIGHT - Car.WIDTH))
        step = randint(self.CAR_STEP_FROM, self.CAR_STEP_TO + self._level)
        self._cars.append(Car(x, y, step))

########################################################################################################################

    def _create_car_roll(self) -> bool:
        """
        :return: True if another car should be created, False otherwise
        """

        return randint(0, 50) == 0

########################################################################################################################

    def start_game(self) -> None:
        """
        Start the game on the first level.
        """

        self._game_going = True
        self._level = 1
        self._start_level()

        while self._game_going:
            if self._is_player_behind_finish_line():
                self._finish_level()
                self._start_level()

            [car.move() for car in self._cars]
            self._cars = list(filter(lambda car: car.isvisible(), self._cars))
            self._player.move()
            if self._create_car_roll():
                self._add_car()
            sleep(1 / self.SPEED)

        self._screen.bye()

########################################################################################################################

    def _start_level(self) -> None:
        """
        Move player to the starting position and draw the new level number.
        """

        self._player.goto(0, -self.SCREEN_HEIGHT / 2 + Player.WIDTH)
        self._draw_info()
        self._screen.update()

########################################################################################################################

    def _finish_level(self) -> None:
        """
        Increment level counter and remove all cars.
        """

        self._level += 1
        [car.hideturtle() for car in self._cars]

########################################################################################################################

    def _end_game(self) -> None:
        """
        End the game.
        """

        self._game_going = False


########################################################################################################################

def run_program() -> None:
    """
    Play the Turtle Crossing game.
    """

    game = TurtleCrossing()
    game.start_game()


########################################################################################################################
