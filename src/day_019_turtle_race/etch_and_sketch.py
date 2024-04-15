from turtle import Turtle, Screen


########################################################################################################################

class EtchAndSketch:

    def __init__(self):
        """

        """

        self._timmy = Turtle()
        self._screen = Screen()
        self._screen.onkeypress(lambda: self._timmy.forward(10), "w")
        self._screen.onkeypress(lambda: self._timmy.backward(10), "s")
        self._screen.onkeypress(lambda: self._timmy.left(5), "a")
        self._screen.onkeypress(lambda: self._timmy.right(5), "d")
        self._screen.onkeypress(self._clear, "c")
        self._screen.listen()
        self._screen.exitonclick()

########################################################################################################################

    def _clear(self):
        """

        :return:
        """

        self._timmy.penup()
        self._timmy.clear()
        self._timmy.home()
        self._timmy.pendown()


########################################################################################################################
