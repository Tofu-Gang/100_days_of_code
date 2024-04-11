from turtle import Turtle, Screen, colormode
from random import randint


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

def draw_shape(turtle: Turtle, side_size: int, sides_count: int) -> None:
    """
    Draw a shape with specified number and size of sides. Each shape is drawn with a different, random color.

    :param turtle: a Turtle object
    :param side_size: size of a shape side
    :param sides_count: number of shape sides
    """

    colormode(255)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.pencolor((r, g, b))
    angle = 360 / sides_count
    for _ in range(sides_count):
        turtle.forward(side_size)
        turtle.right(angle)


########################################################################################################################


def run_program() -> None:
    """

    """

    timmy = Turtle()
    draw_shape(timmy, 100, 3)
    draw_shape(timmy, 100, 4)
    draw_shape(timmy, 100, 5)
    draw_shape(timmy, 100, 6)
    draw_shape(timmy, 100, 7)
    draw_shape(timmy, 100, 8)
    draw_shape(timmy, 100, 9)
    draw_shape(timmy, 100, 10)
    dashed_line(timmy)
    screen = Screen()
    screen.exitonclick()


########################################################################################################################
