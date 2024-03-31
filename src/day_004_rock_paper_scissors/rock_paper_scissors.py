from random import choice


########################################################################################################################

def _draw_rock() -> None:
    """
    Draw a "rock" hand.
    """

    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """)


########################################################################################################################

def _draw_paper() -> None:
    """
    Draw a "paper" hand.
    """

    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """)


########################################################################################################################

def _draw_scissors() -> None:
    """
    Draw a "scissors" hand.
    """

    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """)


########################################################################################################################

def _draw_hand(hand: str) -> None:
    """
    Draw the chosen hand.

    :param hand: the chosen hand
    """

    if hand.upper() in ("R", "r"):
        _draw_rock()
    elif hand.upper() in ("P", "p"):
        _draw_paper()
    elif hand.upper() in ("S", "s"):
        _draw_scissors()


########################################################################################################################

def _get_result(player_hand: str, computer_hand: str) -> None:
    """
    Print the result of the game of Rock, Paper, Scissors based on what the player and the computer chose.

    :param player_hand: player choice
    :param computer_hand: computer choice
    """

    player_hand = player_hand.upper()
    computer_hand = computer_hand.upper()

    if player_hand == computer_hand:
        print("Draw!")
    elif ((player_hand == "R" and computer_hand == "S") or
          (player_hand == "P" and computer_hand == "R") or
          (player_hand == "S" and computer_hand == "P")):
        print("You win!")
    elif ((player_hand == "R" and computer_hand == "P") or
          (player_hand == "P" and computer_hand == "S") or
          (player_hand == "S" and computer_hand == "R")):
        print("You lose!")


########################################################################################################################

def run_program() -> None:
    """
    Play Rock, Paper, Scissors.
    """

    print("Welcome to Rock, Paper, Scissors!")
    while True:
        print("What do you choose? Type R/r for rock, P/p for paper or S/s for scissors; Ctrl+C to exit:")
        player_hand = input("> ")

        if player_hand.upper() in ("R", "r", "P", "p", "S", "s"):
            _draw_hand(player_hand)
            print("Computer chose:")
            computer_hand = choice(("R", "P", "S"))
            _draw_hand(computer_hand)
            _get_result(player_hand, computer_hand)
            print("Press Enter to play a new game...")
            input()


########################################################################################################################
