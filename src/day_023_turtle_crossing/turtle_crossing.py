from turtle import Screen

from .player import Player


########################################################################################################################

class TurtleCrossing:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600

########################################################################################################################

    def __init__(self):
        """
        Set up the screen.
        """

        self._screen = Screen()
        self._screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self._screen.title("TURTLE CROSSING")
        self._screen.tracer(0)

        self._player = Player()
        self._player.goto(0, -self.SCREEN_HEIGHT / 2 + Player.WIDTH)
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
    Play the Turtle Crossing game.
    """

    game = TurtleCrossing()
    game.end_game()


########################################################################################################################
