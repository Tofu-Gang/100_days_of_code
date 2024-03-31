########################################################################################################################

def _cross_road() -> str:
    """
    :return:
    """

    print("You're at a cross road. Where do you want to go?")
    print("- Type \"(L)eft\" to go left.")
    print("- Type \"(R)ight\" to go right.")

    while True:
        direction = input("> ")
        if direction.upper() in ("L", "LEFT", "R", "RIGHT"):
            return direction
        else:
            print("Invalid input. [L|LEFT] or [R|RIGHT] required (case insensitive).")
            continue


########################################################################################################################

def _lake() -> str:
    """

    :return:
    """

    print("You come to a lake. There is an island in the middle of the lake. What do you do?")
    print("- Type \"(W)ait\" to wait for a boat.")
    print("- Type \"(S)wim\" to swim across.")

    while True:
        action = input("> ")
        if action.upper() in ("W", "WAIT", "S", "SWIM"):
            return action
        else:
            print("Invalid input. [W|WAIT] or [S|SWIM] required (case insensitive).")
            continue


########################################################################################################################

def _island() -> str:
    """

    """

    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
    print("Which colour do you choose?")
    print("- Type \"(R)ed\" to open the red door.")
    print("- Type \"(Y)ellow\" to open the yellow door.")
    print("- Type \"(B)lue\" to open the blue door.")

    while True:
        door = input("> ")
        if door.upper() in ("R", "RED", "Y", "YELLOW", "B", "BLUE"):
            return door
        else:
            print("Invalid input. [R|RED], [Y|YELLOW] or [B|BLUE] required (case insensitive).")
            continue


########################################################################################################################

def _print_treasure() -> None:
    """

    """

    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    ''')


########################################################################################################################

def run_program() -> None:
    """
    Collect both demanded user inputs and generate a possible band name from those inputs.
    """

    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    direction = _cross_road()
    if direction.upper() in ("L", "LEFT"):
        action = _lake()
        if action.upper() in ("W", "WAIT"):
            door = _island()
            if door.upper() in ("R", "RED"):
                print("It's a room full of fire. Game Over.")
            elif door.upper() in ("Y", "YELLOW"):
                print("You found the treasure! You Win!")
                _print_treasure()
            elif door.upper() in ("B", "BLUE"):
                print("You enter a room of beasts. Game Over.")
        elif action.upper() in ("S", "SWIM"):
            print("You got attacked by an angry trout. Game Over.")
    elif direction.upper() in ("R", "RIGHT"):
        print("You fell into a hole. Game Over.")

########################################################################################################################
