from turtle import Turtle, Screen, colormode
from random import randint, choice


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

def random_color() -> tuple[int, int, int]:
    """
    :return:
    """

    colormode(255)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


########################################################################################################################

def draw_shape(turtle: Turtle, side_size: int, sides_count: int) -> None:
    """
    Draw a shape with specified number and size of sides. Each shape is drawn with a different, random color.

    :param turtle: a Turtle object
    :param side_size: size of a shape side
    :param sides_count: number of shape sides
    """

    turtle.pencolor(random_color())
    angle = 360 / sides_count
    for _ in range(sides_count):
        turtle.forward(side_size)
        turtle.right(angle)


########################################################################################################################

def random_walk(turtle: Turtle) -> None:
    """

    :param turtle:
    """

    turtle.pensize(10)

    for _ in range(200):
        turtle.pencolor(random_color())
        turtle.right(choice((90, 180, 270, 360)))
        turtle.forward(20)


########################################################################################################################

def draw_spirograph(turtle: Turtle) -> None:
    """

    :param turtle:
    """

    step = 5
    steps = int(360 / step)

    for _ in range(steps):
        color = random_color()
        turtle.pencolor(color)
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.right(step)


########################################################################################################################


def run_program() -> None:
    """

    """

    timmy = Turtle()
    timmy.speed("fastest")
    draw_spirograph(timmy)
    screen = Screen()
    screen.exitonclick()


########################################################################################################################
