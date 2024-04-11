from turtle import Turtle, Screen


########################################################################################################################

def dashed_line(turtle: Turtle) -> None:
    """
    Draw a dashed line.

    :param turtle: a Turtle object
    """

    turtle.left(90)
    for _ in range(30):
        turtle.forward(5)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()


########################################################################################################################


def run_program() -> None:
    """

    """

    timmy = Turtle()
    dashed_line(timmy)
    screen = Screen()
    screen.exitonclick()


########################################################################################################################
