from turtle import Turtle, Screen, colormode
from random import randint


########################################################################################################################

def random_color() -> tuple[int, int, int]:
    """
    :return:
    """

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


########################################################################################################################

def run_program() -> None:
    """
    Paint an image similar to Damien Hirst's "spots"; 10x10 dots in random colors.
    """

    timmy = Turtle()
    timmy.speed("fastest")
    timmy.penup()
    timmy.hideturtle()

    colormode(255)
    screen = Screen()
    screen.setup(470, 450)
    screen.bgcolor((244, 244, 244))

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            timmy.setx(x)
            timmy.sety(y)
            color = random_color()
            timmy.dot(20, color)
            timmy.forward(40)

    screen.exitonclick()


########################################################################################################################
