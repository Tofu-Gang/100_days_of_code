from turtle import Turtle, Screen

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
TURTLE_WIDTH = 10
TURTLES_DISTANCE = 40
COLORS = ("red", "orange", "yellow", "green", "blue", "purple")

########################################################################################################################


def run_program() -> None:
    """

    """

    turtles = tuple(Turtle(shape="turtle") for _ in range(len(COLORS)))
    [turtles[i].color(COLORS[i]) for i in range(len(turtles))]
    [turtle.penup() for turtle in turtles]
    [turtles[i].goto(-(SCREEN_WIDTH / 2) + TURTLE_WIDTH, (2 * TURTLES_DISTANCE + TURTLES_DISTANCE / 2) - i * TURTLES_DISTANCE) for i in range(len(turtles))]
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
    print(user_bet)
    screen.exitonclick()


########################################################################################################################
