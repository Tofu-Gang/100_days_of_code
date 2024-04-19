from turtle import Screen
from time import sleep

from .player import Player


########################################################################################################################

class TurtleCrossing:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    SPEED = 50

########################################################################################################################

    def __init__(self):
        """
        Set up the screen.
        """

        self._screen = Screen()
        self._screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self._screen.title("TURTLE CROSSING")
        self._screen.onkeypress(self._end_game, "Escape")
        self._screen.tracer(0)
        self._screen.listen()

        self._player = Player()
        self._player.goto(0, -self.SCREEN_HEIGHT / 2 + Player.WIDTH)
        self._screen.update()

        self._game_going = True

########################################################################################################################

    def start_game(self) -> None:
        """
        Start the game.
        """

        while self._game_going:
            self._player.move()
            sleep(1 / self.SPEED)

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
