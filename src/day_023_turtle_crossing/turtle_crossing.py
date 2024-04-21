from turtle import Screen, Turtle
from time import sleep

from .player import Player


########################################################################################################################

class TurtleCrossing:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    FINISH_HEIGHT = 40
    LEVEL_PADDING_LEFT = 20
    LEVEL_PADDING_TOP = 40
    SPEED = 50

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

        self._player = Player()
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

    def start_game(self) -> None:
        """
        Start the game on the first level.
        """

        self._game_going = True
        self._level = 1
        self._start_level()

        while self._game_going:
            if self._is_player_behind_finish_line():
                self._level += 1
                self._start_level()
            self._player.move()
            sleep(1 / self.SPEED)

########################################################################################################################

    def _start_level(self) -> None:
        """
        Move player to the starting position and draw the new level number.
        """

        self._player.goto(0, -self.SCREEN_HEIGHT / 2 + Player.WIDTH)
        self._draw_info()
        self._screen.update()

########################################################################################################################

    def _end_game(self) -> None:
        """
        End the game.
        """

        self._game_going = False
        self._screen.bye()


########################################################################################################################

def run_program() -> None:
    """
    Play the Turtle Crossing game.
    """

    game = TurtleCrossing()
    game.start_game()


########################################################################################################################
