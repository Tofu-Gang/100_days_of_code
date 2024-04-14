from turtle import Turtle, Screen

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
TURTLE_WIDTH = 10

########################################################################################################################


def run_program() -> None:
    """

    """

    timmy = Turtle(shape="turtle")
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
    print(user_bet)
    timmy.penup()
    timmy.goto(-(SCREEN_WIDTH / 2) + TURTLE_WIDTH, 0)
    screen.exitonclick()


########################################################################################################################
