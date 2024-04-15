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

        screen = Screen()
        screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        screen.bgcolor("black")
        screen.title("SNAKE")
        snake = [Turtle(shape="square"), Turtle(shape="square"), Turtle(shape="square")]
        [turtle.color("white") for turtle in snake]
        [turtle.penup() for turtle in snake]
        [snake[i].goto(0 - i * self.TURTLE_SQUARE_SIDE, 0) for i in range(len(snake))]
        screen.exitonclick()


########################################################################################################################

def run_program() -> None:
    """

    """

    Snake()

########################################################################################################################
