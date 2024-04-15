from turtle import Turtle, Screen
from random import randint

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
TURTLE_WIDTH = 10
TURTLE_HEIGHT = 27
TURTLES_DISTANCE = 40
COLORS = ("red", "orange", "yellow", "green", "blue", "purple")

########################################################################################################################


def run_program() -> None:
    """

    """

    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    turtles = tuple(Turtle(shape="turtle") for _ in range(len(COLORS)))
    [turtles[i].color(COLORS[i]) for i in range(len(turtles))]
    [turtle.penup() for turtle in turtles]
    [turtles[i].goto(-(SCREEN_WIDTH / 2) + TURTLE_WIDTH,
                     (2 * TURTLES_DISTANCE + TURTLES_DISTANCE / 2) - i * TURTLES_DISTANCE)
     for i in range(len(turtles))]
    [turtle.pendown() for turtle in turtles]
    [turtle.pensize(5) for turtle in turtles]

    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

    while all([turtle.pos()[0] < SCREEN_WIDTH / 2 - TURTLE_HEIGHT for turtle in turtles]):
        [turtle.forward(randint(1, 10)) for turtle in turtles]

    winning_turtle = next(filter(lambda turtle: turtle.pos()[0] >= SCREEN_WIDTH / 2 - TURTLE_HEIGHT, turtles))

    if user_bet.upper() == winning_turtle.color()[0].upper():
        message = "You win!"
    else:
        message = "You lost."
    message += f" The winner was {winning_turtle.color()[0]}."

    turtle = Turtle()
    turtle.color("black")
    turtle.penup()
    turtle.goto(-SCREEN_WIDTH / 4, turtles[-1].pos()[1] - 2 * TURTLES_DISTANCE)
    turtle.pendown()
    turtle.write(message, font=("Verdana", 15, "normal"), move=True)

    screen.exitonclick()


########################################################################################################################
