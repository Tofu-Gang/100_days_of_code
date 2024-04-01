########################################################################################################################

def run_program() -> None:
    """
    Let Reeborg out of the maze.
    """

    print("""
To solve this challenge, go to the following link:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Then, paste the following code and let Reeborg out of the maze.

########################################################################################################################

def turn_right():
    \"\"\"
    Turn Reeborg right.
    \"\"\"
    
    turn_left()
    turn_left()
    turn_left()


########################################################################################################################
    
def fix_beginning():
    \"\"\"
    Avoid the infinite loop in following the right-hand wall.
    \"\"\"
    
    while front_is_clear():
        move()
    turn_left()

########################################################################################################################

# avoid infinite loop
fix_beginning()

# follow the right-hand wall and reach the goal
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    else:
        if front_is_clear():
            move()
        else:
            turn_left()
    
########################################################################################################################
    """)

########################################################################################################################
