from requests import get
from random import choice


class Hangman:
    DICT_SITE = "https://www.mit.edu/~ecprice/wordlist.10000"

    LOGO = """ 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
    """

    # by Joan Stark, from https://www.asciiart.eu/holiday-and-events/fireworks
    WIN = """
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
        *
        *
    """

    # from https://emojicombos.com/poop-ascii-art
    POOP = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⢿⣇⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡶⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀⢻⣿⠁⠀⠀⠀⠀⠀⠘⢷⡄⠀⠀⠀⠀⠀
⠐⠴⣗⣦⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⢠⣶⠟⠛⠉⠀⠀⠀⢠⡄⠀⠀⠈⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠉⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⢀⣼⠇⠀⢀⣼⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⢹⣷⠀⠀⠀⠀⣿⠁⠀⠠⣏⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡘⠀⠀⠀⢘⡇⠀⠀⠀⠀⠀⠱⢄⠀⠀⠀⠘⡆⠀⠀⢰⡟⠁⠀⠀⠀⠀⠹⣷⡄⠀⠙⢦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠇⠀⠀⢀⡾⠃⠀⠀⠀⠀⠀⠀⡶⣤⠀⠈⠁⠀⠀⠀⠘⣗⠀⠀⠀⠀⠀⠀⢈⡿⠀⠀⠀⠃⠀⠀⢀⠀⠀
⠀⠀⠀⢠⠟⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⣰⠃⢸⡀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠰⠤⠿⠒⠂
⠀⠀⠀⣞⠀⠀⠀⢸⡇⠀⠀⠀⠀⣠⡴⠟⠁⠀⠈⠳⠦⣤⣀⠀⠀⠀⠁⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⠀⠀⠀⠀⠧⠀⠀⠀⢰⡟⠀⠀⠀⠐⠼⢟⣲⡐⠈⣻⣤⣤⣀⠀⠀⠀⠀⠀⠙⢶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠐⠀⢀⠀⠀⠀⠀⡉⠉⠉⢠⡘⠙⣿⣦⡀⠀⠀⠀⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣿⣦⡀⠈⠐⠀⠄⠀⠀⠀⠀⠀⣀⣀⢈⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⣠⠌⠉⠓⠒⠀⠀⠀⠀⠐⠊⠊⠇⠿⠀⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠯⣷⡀⡜⢡⠆⠰⠂⠀⠀⠀⠀⠒⠦⠄⠌⠙⠲⢻⠉⡿⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⠟⢠⠇⢩⠃⠀⠀⠀⠀⠀⠀⠤⠃⠀⠀⠀⠀⠀⠹⣄⠀⡈⠙⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⠟⡋⠁⠀⠀⠀⠀⠀⠀⣰⠓⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⢀⡈⡆⠳⣌⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⡟⠱⠡⠃⠐⠂⡄⠀⠀⠠⠄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠆⢹⣴⣀⣳⣷⣶⠾⠟⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠉⠉⣉⡙⡛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⢣⡑⠈⢻⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡇⢹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠁⠀⠀⡀⢰⢠⠀⡆⠀⠆⠀⡄⢄⢶⠼⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣷⡀⠘⡟⡆⡄⡀⠀⠀⠀⢀⠀⠀⠰⠀⠀⠀⠀⠐⣶⠄⡇⠾⠘⠀⢉⡄⢠⢧⢧⢸⠀⣰⡟⢀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣼⣷⡄⠀⣡⠁⢀⠈⡀⠀⠈⠐⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠃⠘⠢⠘⠊⢈⣡⣴⠟⡠⠋⡰⠃⡄⠀⠀
⠀⠀⣸⠕⢋⡽⠻⣶⣅⣇⠈⠰⠁⡇⠄⢰⠀⠀⠀⠀⠠⢠⣴⠠⠀⠃⠀⠀⢀⣀⣤⣴⡾⢟⡿⢣⠞⣡⠞⢀⡜⠁⠀⠀
⠀⠀⡴⠊⢁⡠⠚⠉⢉⡿⠛⢿⠷⢶⣶⣶⣦⣤⣤⣤⣤⣶⣶⣶⠶⡾⠿⠛⡿⠋⡩⠋⠠⠋⡴⢃⡜⠁⠀⠎⠀⠈⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠚⠁⠐⠋⠀⠊⠀⠘⠁⠀⠁⠀⠈⠀⠘⠁⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """

    STAGES = ["""
  +---+
  |   |
      |
      |
      |
      |
=========
        """, """
  +---+
  |   |
  O   |
      |
      |
      |
=========
        """, """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
        """, """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
        """, """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
        """, """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
        """, """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
        """]

########################################################################################################################

    def __init__(self):
        """

        """

        self._stage = 0
        self._word = self._get_random_word()
        self._guessed_letters = []

########################################################################################################################

    def _get_random_word(self) -> str:
        """
        :return: a random word from a free web dictionary
        """

        response = get(self.DICT_SITE)
        words = response.content.splitlines()
        return choice(words).decode("utf-8")

########################################################################################################################

    def _print_word(self) -> None:
        """

        """

        print(" ".join(letter if letter in self._guessed_letters else "_" for letter in self._word))

########################################################################################################################

    def _print_already_guessed(self) -> None:
        """

        """

        print("You already guessed " + ", ".join(letter for letter in self._guessed_letters) + ".")

########################################################################################################################

    def _is_lost(self) -> bool:
        """
        :return:
        """

        return self._stage == len(self.STAGES) - 1

########################################################################################################################

    def _is_win(self) -> bool:
        """
        :return:
        """

        return all(letter in self._guessed_letters for letter in self._word)

########################################################################################################################

    def play(self) -> None:
        """

        """

        print(self.LOGO)

        while True:
            self._print_word()
            if len(self._guessed_letters) > 0:
                self._print_already_guessed()
            print(self.STAGES[self._stage])

            if self._is_lost():
                print("You lost!")
                print(f"The word was {self._word.upper()}.")
                break
            else:
                guess = input("Guess a letter:\n> ").strip()

                if len(guess) != 1 or not guess.isalpha():
                    print("Type a single letter.")
                elif guess in self._guessed_letters:
                    print("You have already guessed that.")
                else:
                    self._guessed_letters.append(guess)

                    if guess in self._word:
                        print(f"Correct! {guess} is in the word!")

                        if self._is_win():
                            print(f"You revealed the word {self._word.upper()}! You win!")
                            break
                    else:
                        print(f"You guessed {guess}, that's not in the word. You lose a life.")
                        self._stage += 1

            print("Press Enter to continue...")
            input()

        if self._is_win():
            print(self.WIN)
        elif self._is_lost():
            print(self.POOP)


########################################################################################################################

def run_program() -> None:
    """

    """

    Hangman().play()

########################################################################################################################
